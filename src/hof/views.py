from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory

from .models import Store, StoreImage
from .forms import StoreForm, StoreImageForm


def index(request):
    return render(request, 'hof/index.html', {})


def store_list(request):
    return render(request, 'hof/store_list.html', {})


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'hof/store_detail.html', {
        'store':store,
    })


def store_new(request):
    ImageFormSet = modelformset_factory(StoreImage, form=StoreImageForm, extra=3)

    if request.method == 'POST':
        storeForm = StoreForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=StoreImage.objects.none())
        if storeForm.is_valid() and formset.is_valid():
            store = storeForm.save(commit=False)
            store.owner = request.user
            store.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = StoreImage(post=post_form, image=image)
                photo.save()
            messages.success(request, "성공적")
            return redirect("/")
    else:
        storeForm = StoreForm()
        formset = ImageFormSet(queryset=StoreImage.objects.none())

    return render(request, 'hof/store_form.html', {
        'storeForm': storeForm,
        'formset': formset,
    })