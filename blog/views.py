from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'author': 'Me',
        'title': 'first post',
        'content': 'wefkjwae',
        'date_posted': '12/23/2020'
    },
    {
        'author': 'Me',
        'title': 'second post',
        'content': 'wefkweawefaweajwae',
        'date_posted': '12/24/2020'
    },
    {
        'author': 'Me',
        'title': 'third post',
        'content': 'wefkjwawefaweawefe',
        'date_posted': '12/25/2020'
    }
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
