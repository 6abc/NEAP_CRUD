from django.shortcuts import render
from neapolitan.views import CRUDView
from app1.models import Movie

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
def HomeView(request):
    data = Movie.objects.all()
    return render(request, 'home.html', {'data_dict': data})

@method_decorator(staff_member_required, name='dispatch')
class MovieView(CRUDView):
    model = Movie
    fields = ['title', 'year', 'director', 'poster', 'plot']