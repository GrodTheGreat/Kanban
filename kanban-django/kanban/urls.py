from django.urls import path

from . import views

urlpatterns = [
    path(route="", view=views.index, name="index"),
    path("base/", view=views.base),
]
