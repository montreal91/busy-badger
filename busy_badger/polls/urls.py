
from django.conf.urls import url

from . import views

urlpatterns = [
    url( r"^$", views.XIndexView.as_view(), name="index" ),
    url( r"^(?P<pk>[0-9]+)/$", views.XDetailView.as_view(), name="details" ),
    url( r"^(?P<pk>[0-9]+)/res/$", views.XResultsView.as_view(), name="results" ),
    url( r"^(?P<question_id>[0-9]+)/vote/$", views.vote, name="vote" ),
]