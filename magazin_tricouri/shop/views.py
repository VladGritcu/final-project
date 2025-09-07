from shop.models import Tshirt 
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView


class HomepageListView(ListView):
    templat_name = "home_page.html"
    model = Tshirt

# Create your views here.
