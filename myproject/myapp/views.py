from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Article, Team, Tournament  # Assurez-vous d'importer Team et Tournament
from .forms import ArticleForm

def home_view(request):
    articles = Article.objects.all()
    return render(request, 'myapp/home.html', {'articles': articles})

def teams_view(request):
    teams = Team.objects.all()
    return render(request, 'myapp/teams.html', {'teams': teams})

def tournaments_view(request):
    tournaments = Tournament.objects.all()
    return render(request, 'myapp/tournaments.html', {'tournaments': tournaments})

def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'myapp/add_article.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'myapp/edit_article.html', {'form': form})
