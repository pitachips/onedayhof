from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Store, StoreImage, Review, ReviewImage
from .forms import StoreForm, StoreImageForm, ReviewForm, ReviewImageForm


def index(request):
    return render(request, 'hof/index.html', {})


@login_required
def store_list(request):
    store_list = Store.objects.all().order_by('-rating')

    ## 검색파트
    query_where = request.GET.get('where')
    query_what = request.GET.get('what')

    if query_where and query_what:
        store_list = store_list.filter(
            (Q(gu__contains=query_where) |
            Q(region__contains=query_where)) &
            (Q(atmosphere__contains=query_what) |
            Q(description__contains=query_what) |
            Q(contract_condition__contains=query_what))
        ).distinct()
    elif query_where and not query_what:
        store_list = store_list.filter(
            (Q(gu__contains=query_where) |
            Q(region__contains=query_where))
        ).distinct()
    elif not query_where and query_what:
        store_list = store_list.filter(
            (Q(atmosphere__contains=query_what) |
            Q(description__contains=query_what) |
            Q(contract_condition__contains=query_what))
        ).distinct()
    else:
        pass
    return render(request, 'hof/store_list.html', {})


@login_required
def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'hof/store_detail.html', {
        'store':store,
    })


@login_required
def store_new(request):
    if not request.user.is_staff and not request.user.profile.is_store_owner:
        return redirect('index')

    ImageFormSet = modelformset_factory(StoreImage, form=StoreImageForm, extra=3)

    if request.method == 'POST':
        storeForm = StoreForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=StoreImage.objects.none())

        if storeForm.is_valid() and formset.is_valid():
            store = storeForm.save(commit=False)
            store.owner = request.user
            store.save()
            store_images = formset.save(commit=False)
            for store_image in store_images:
                store_image.store = store
                store_image.save()
            messages.success(request, "업체가 성공적으로 등록되었습니다. 관리자의 승인 후에 실제로 홈페에지에 게시됩니다.")
            return redirect("/")
    else:
        storeForm = StoreForm()
        formset = ImageFormSet(queryset=StoreImage.objects.none())

    return render(request, 'hof/store_form.html', {
        'storeForm': storeForm,
        'formset': formset,
    })


@login_required
def store_edit(request,pk):
    store = get_object_or_404(Store, pk=pk)
    store_image = store.storeimage_set.all()
    ImageFormSet = modelformset_factory(StoreImage, form=StoreImageForm, extra=3)

    if request.method == 'POST':
        storeForm = StoreForm(request.POST, instance=store)
        formset = ImageFormSet(request.POST, request.FILES, queryset=store_image.all())

        if storeForm.is_valid() and formset.is_valid():
            store = storeForm.save(commit=False)
            store.owner = request.user
            store.save()
            store_images = formset.save(commit=False)
            for store_image in store_images:
                store_image.store = store
                store_image.save()
            messages.success(request, "업체가 성공적으로 등록되었습니다. 관리자의 승인 후에 실제로 홈페에지에 게시됩니다.")
            return redirect("/")
    else:
        storeForm = StoreForm(instance=store)
        formset = ImageFormSet(queryset=store_image.all())

    return render(request, 'hof/store_form.html', {
        'storeForm': storeForm,
        'formset': formset,
    })


@login_required
def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.user != store.owner:
        return redirect('index')

    store.delete()
    messages.error(request, "업체가 삭제되었습니다.")
    return redirect("hof:index")


@login_required
def review_new(request, store_id):
    store=Store.objects.get(pk=store_id)
    if (request.method =="POST"):
        form=ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.store = store
            review.author = request.user
            review.created_at = timezone.now()
            review.save()
            store.rating = store.rating*store.n_review + review.rating
            store.n_review += 1
            store.rating = store.rating/store.n_review
            store.save()
            return redirect(store_detail, pk=store_id)
    else:
        form = ReviewForm()
    return render(request, 'hof/review_form.html', {'form': form, 'store':store})


def review_edit(request, store_id, review_id):
    store = Store.objects.get(pk=store_id)
    review = Review.objects.get(pk=review_id)
    old_rating = review.rating
    if (request.method == "POST"):
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.store = store
            review.author = request.user
            review.save()
            store.rating = (store.rating*store.n_review - old_rating + review.rating)/store.n_review
            store.save()
            return redirect(store_detail, pk=store_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'hof/review_form.html', {'form': form, 'store':store})


def review_delete(request, store_id, review_id):
    store = Store.objects.get(pk=store_id)
    review = Review.objects.get(pk=review_id)
    review.delete()
    return redirect(store_detail, pk=store_id)


