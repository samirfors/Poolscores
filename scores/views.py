from django.shortcuts import render_to_response, get_object_or_404
from scores.models import Tournament, Fixture
from django.http import Http404

def index(request):
	latest_tournaments = Tournament.objects.all().order_by('-date_played')[:10]
	return render_to_response('scores/index.html', {'latest_tournaments':latest_tournaments})

def detail(request, t_id):
	#t = get_object_or_404(Tournament, pk=t_id)
	fixtures = Fixture.objects.all();
	return render_to_response('scores/detail.html', {'fixtures':fixtures})
