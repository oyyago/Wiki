from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path('new' , views.new_page, name="new" ),
    path('edit', views.edit, name="edit"),
    path('save', views.edit_save , name="save"),
    path('randon', views.random , name='random')
]

