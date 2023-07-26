from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import back
import json


def mlb(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())

def compare(request):
    template = loader.get_template('compare.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())

def player(request):
    name = request.POST.get('tags')
    print(name)
    try:
        player_stats = back.playerInfo(name)
        player_info = back.lookup(name)
    except:
        return render(request, 'playerNotFound.html')
    team = back.team(player_info.get('currentTeam').get('id'))
    try:
        nickname = player_info['nickName']
    except:
        nickname = "NONE"
    context = {
        'number': player_info['primaryNumber'],
        'team': team,
        'position': player_info['primaryPosition']['abbreviation'],
        'debut': player_info['mlbDebutDate'],
        'nickname': nickname,
        'playerStats': player_stats,
        'name': name
    }
    return render(request, 'playerInfo.html', context)

def search(request):
    # if request.method == "POST":
    #   print("woo woooooo")
    f = open('PlayerList.json')
    data = json.load(f)['list']

    template = loader.get_template('playerLookUp.html')
    #return HttpResponse(template.render(), {'data': data})
    return render(request, 'playerLookUp.html', {'data': data})


