from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from main.models import Project, ResearchPaper, Team, Gallery

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ProjectListView(ListView):
    model = Project


class PaperListView(ListView):
    model = ResearchPaper


class TeamListView(ListView):
    model = Team

def contact(request):
    return render(request, 'contact.html')


class GalleryListView(ListView):
    model = Gallery