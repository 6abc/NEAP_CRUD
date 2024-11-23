from django.shortcuts import render
from neapolitan.views import CRUDView
from app1.models import Movie

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        try:
            data_dict = Movie.objects.all()
        except OperationalError:
            data_dict = []  # Fallback if the table does not exist

        return render(request, self.template_name, {"data_dict": data_dict})

@method_decorator(staff_member_required, name='dispatch')
class MovieView(CRUDView):
    model = Movie
    fields = ['title', 'year', 'director', 'poster', 'plot']
