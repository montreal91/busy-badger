
# from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404

from .models import XQuestion


def index( request ):
    latest_question_list = XQuestion.objects.order_by( "-pub_date" )[ :10 ]
    context = { "latest_question_list": latest_question_list }
    return render( request, "polls/index.html", context )

def details( request, question_id ):
    question = get_object_or_404( XQuestion, pk=question_id)
    return render( request, "polls/detail.html", {"question": question})