from django.shortcuts import render, reverse
from django.views.generic import TemplateView, ListView, DetailView

from main.models import Project, ResearchPaper, Team, Gallery
from blog.models import Article

# Create your views here.
class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['articles'] = Article.objects.all()
        context['teams'] = Team.objects.all()
        context['projects'] = Project.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class PaperListView(ListView):
    model = ResearchPaper


class TeamListView(ListView):
    model = Team

def contact(request):
    return render(request, 'contact.html')


class GalleryListView(ListView):
    model = Gallery