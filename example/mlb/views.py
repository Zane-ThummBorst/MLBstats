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
    MLBAMID = 1

    # can turn getting this id into a backend funtion
    f = open('razzball.json', encoding='utf-8')
    data = json.load(f)
    for player in data:
        if player['Name'] == name:
            MLBAMID = player['MLBAMID']
    f.close()
    headshot = 'https://midfield.mlbstatic.com/v1/people/' + str(MLBAMID) + '/spots/300'
    try:
        pb = back.playerInfo2(name, year, stat.lower())
        player_stats = pb[0]
        abbr = pb[1]
        player_info = back.lookup(name)
    except:
        return render(request, 'playerNotFound.html')

    team = back.team_name(player_info.get('currentTeam').get('id'))

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
        'abbr': abbr,
        'headshot': headshot
    }
    return render(request, 'playerInfoB.html', context)

def search(request):
    # if request.method == "POST":
    #   print("woo woooooo")
    f = open('PlayerList.json')
    data = json.load(f)['list']
    f.close()
    date = datetime.date.today()
    year = []
    for i in range(2003,date.year + 1):
        year.append(i)
    print(year)
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


