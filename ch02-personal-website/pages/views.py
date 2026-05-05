from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView  

# Create your views here.

def home_page_view(request):
    return render(request, "home.html")

class AboutPageView(TemplateView):  # new
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context