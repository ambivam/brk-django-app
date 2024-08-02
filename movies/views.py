from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies':[
        {
            'id': 5,
            'title': 'The Godfather',
            'year': 1972,
        },
        {
            'id': 6,
            'title': 'The Shawshank Redemption',
            'year': 1994,
        },
        {
            'id': 7,
            'title': 'The Dark Knight',
            'year': 2008,
        },
    ]
}
    

def movies(request):
    return render(request,'movies/movies.html',data)

def home(request):
    return HttpResponse("Hello Home Page")