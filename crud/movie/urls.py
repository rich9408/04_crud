from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.list, name="list"),
    path("new/", views.new, name="new"),
    path("<int:id>/", views.detail, name="detail"),
    path("<int:id>/update/", views.update, name="update"),
    path("<int:id>/delete/", views.delete, name="delete"),
    
    path("<int:id>/comment/", views.comment, name="comment"),
]