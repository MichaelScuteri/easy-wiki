from django.urls import path
from . import views

urlpatterns = [
    path("", views.wiki_index, name="index"),
    path("entry/<slug:slug>/", views.wiki_page, name="entry-page"),
    path("upload/", views.upload, name="upload"),
    path("update/<slug:slug>/", views.upload, name='upload'),
    path("delete/<slug:slug>/", views.delete, name='delete')
]
