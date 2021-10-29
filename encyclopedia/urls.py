from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("wiki/<entry>", views.entry_view, name="entry"),

    path("search", views.search_view, name="search"),

    path("new_entry", views.new_entry_view, name="new_entry")

]
