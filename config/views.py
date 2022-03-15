from django.shortcuts import render


def error404(request, exception):
    return render(request, 'errors/error404.html', status=404)


def error500(request, *args, **kwargs):
    return render(request, 'errors/error500.html', status=500)
