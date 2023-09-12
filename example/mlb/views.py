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
        pb = back.playerInfo(name)
        player_stats = pb[0]
        abbr = pb[1]
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
        'name': name,
        'abbr': abbr
    }
    return render(request, 'playerInfoB.html', context)

def search(request):
    # if request.method == "POST":
    #   print("woo woooooo")
    f = open('PlayerList.json')
    data = json.load(f)['list']

    template = loader.get_template('playerLookUpB.html')
    #return HttpResponse(template.render(), {'data': data})
    return render(request, 'playerLookUpB.html', {'data': data})

def roster_search(request):
    data = back.allTeams()
    return render(request, 'rosterSearch.html', {'data': data})

def roster_info(request):
    if request.method == 'POST':
        team = request.POST.get('tags')
        team_id = back.nameToTeamId(team)
        lineup = back.roster(team_id)
        record = back.teamRecord(team_id)
        return render(request, 'roster_info.html', {'lineup': lineup,
                                                    'team': team,
                                                    'record': record
                                                    })


