from django.shortcuts import render, resolve_url

import requests

def index(request):
    url = "https://imdb8.p.rapidapi.com/auto-complete"

    

    movie_name = {"q":"wonder woman"}

    headers = {
        'x-rapidapi-key': "9652cc0a79msh4af94eb1191c581p1cbf32jsnca2fa1efd9a3",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=movie_name).json()

    movie = {
        'name' : response['d'][0]['l'],
        'image' : response['d'][0]['i']['imageUrl'],
        'staring' : response['d'][0]['s'],
        # 'v' : response['d'][0]['v'],
        # 'feature' : response['d'][0]['q']
       
    }

    print(movie)
    # print(response)


    context = {'movie' : movie}
    

    return render(request, 'index.html', context)


def search(request):

    url = "https://imdb8.p.rapidapi.com/auto-complete"

    if request.method == 'POST':
        get_movie = request.POST.get('movie_search')

        movie_name = {"q" : get_movie}

        headers = {
        'x-rapidapi-key': "9652cc0a79msh4af94eb1191c581p1cbf32jsnca2fa1efd9a3",
        'x-rapidapi-host': "imdb8.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=movie_name).json()

        movie = {
            'name' : response['d'][0]['l'],
            'image' : response['d'][0]['i']['imageUrl'],
            'staring' : response['d'][0]['s'],
        }

        context = {"movie" : movie}

    return render(request, 'search.html', context)


def genres(request):



    url = "https://data-imdb1.p.rapidapi.com/genres/"

    headers = {
        'x-rapidapi-key': "9652cc0a79msh4af94eb1191c581p1cbf32jsnca2fa1efd9a3",
        'x-rapidapi-host': "data-imdb1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers).json()

    genres = {
        'title' : response['Genres'][0]['genre']
    }

    context = {'genres' : genres}

    return render(request, 'index.html', context)
