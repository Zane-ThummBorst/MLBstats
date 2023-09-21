from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import back

import json, datetime


def mlb(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())

def player(request):
    name = request.POST.get('tags')
    year = request.POST.get('year')
    if year == None: year = 2023
    stat = request.POST.get('stat')
    if stat == None and request.POST.get(name) == 'P':
        stat = 'pitching'
    elif stat == None:
        stat = 'hitting'
    try:
        print('here????')
        pb = back.playerInfo3(name, year, stat.lower())
        player_stats = pb[0]
        abbr = pb[1]
        player_info = back.lookup2(name, year)
    except:
        return render(request, 'playerNotFound.html')


    context = {
        'number': player_info['primaryNumber'],
        'team': player_info['team'],
        'position': player_info['position'],
        'debut': player_info['mlbDebutDate'],
        'nickname': player_info['nickName'],
        'playerStats': player_stats,
        'name': name,
        'abbr': abbr,
        'headshot': player_info['headshot']
    }
    return render(request, 'playerInfoB.html', context)

def search(request):
    f = open('sample.json')
    data = json.load(f)['list']
    f.close()
    date = datetime.date.today()
    year = []
    for i in range(1876,date.year + 1):
        year.append(i)
    return render(request, 'playerLookUpB.html', {'data': data,
                                                  'year': year})

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

