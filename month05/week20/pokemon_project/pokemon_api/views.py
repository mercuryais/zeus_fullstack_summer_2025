from django.shortcuts import render


def pokemon_list(request):
    return render(request, 'pokemon_api/pokemon_list.html')