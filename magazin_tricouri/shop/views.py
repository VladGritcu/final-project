from shop.models import Tshirt 
from django.views.generic import ListView

class HomePageListView(ListView):
    template_name = "home_page.html"
    model = Tshirt

