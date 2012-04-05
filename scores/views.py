from django.shortcuts import render_to_response, get_object_or_404
from scores.models import Tournament, Fixture, Player, Winner
from django.http import Http404

def index(request):
	latest_tournaments = Tournament.objects.all().order_by('-date_played')[:10]
	#players_list = Player.objects.all()
	return render_to_response('scores/index.html', {'latest_tournaments':latest_tournaments})

def create(request):
	players_list = Player.objects.all()
	return render_to_response('scores/create.html', {'players_list':players_list})

def detail(request, t_id):
	#t = get_object_or_404(Tournament, pk=t_id)
	fixtures = Fixture.objects.filter(tournament_id__exact=t_id)
	return render_to_response('scores/detail.html', {'fixtures':fixtures})

def fixture(request, f_id):
	winner = Winner.objects.get(fixture_id=f_id)
	return render_to_response('scores/fixture.html', {'winner':winner})
