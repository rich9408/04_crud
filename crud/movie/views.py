from django.shortcuts import render, redirect
from .models import Movie, Comment
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, "movie/list.html", {"movies":movies})
    
    
def new(request):
    if request.method == "POST":
        title = request.POST.get("title")
        title_en = request.POST.get("title_en")
        audience = request.POST.get("audience")
        open_date = request.POST.get("open_date")
        genre = request.POST.get("genre")
        watch_grade = request.POST.get("watch_grade")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        
        Movie.objects.create(title=title,title_en=title_en, audience=audience,open_date=open_date,
        genre=genre, watch_grade=watch_grade, score=score, poster_url=poster_url, description=description)
        
        return redirect("movies:list")
    
    else:
        return render(request,"movie/new.html")
        
    
def detail(request,id):
    movie = Movie.objects.get(id=id)
    return render(request, "movie/detail.html", {"movie":movie})
    
def update(request,id):
    
    movie = Movie.objects.get(id=id)
    
    if request.method == "POST":
        title = request.POST.get("title")
        title_en = request.POST.get("title_en")
        audience = request.POST.get("audience")
        open_date = request.POST.get("open_date")
        genre = request.POST.get("genre")
        watch_grade = request.POST.get("watch_grade")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        
        movie.title =title
        movie.title_en = title_en
        movie.audience = audience
        movie.open_date = open_date
        movie.genre = genre
        movie.watch_grade = watch_grade
        movie.score = score
        movie.poster_url = poster_url
        movie.description = description
        
        movie.save()
        
        return redirect("movies:detail", id)
        
    else:
        return render(request, "movie/update.html", {"movie":movie})
        

def delete(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("movies:list")
    
def comment(request, id):
    movie = Movie.objects.get(id=id)
    content = request.POST.get("content")
    
    Comment.objects.create(movie=movie,content=content)
    return redirect("movies:detail", id)