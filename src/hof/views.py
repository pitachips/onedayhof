from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'hof/index.html', {})


def store_list(request):
    return render(request, 'hof/store_list.html', {})


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'hof/store_detail.html', {
        'store':store,
    })
