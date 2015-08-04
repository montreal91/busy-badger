
# from django.http import HttpResponse
# from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import XQuestion, XChoice


def index( request ):
    latest_question_list = XQuestion.objects.order_by( "-pub_date" )[ :10 ]
    cont = { "latest_question_list": latest_question_list }
    return render( request, "polls/index.html", cont )

def details( request, question_id ):
    question = get_object_or_404( XQuestion, pk=question_id )
    return render( request, "polls/detail.html", {"question": question} )

def vote( request, question_id ):
    p = get_object_or_404( XQuestion, pk=question_id )
    try:
        selected_choice = p.xchoice_set.get( pk=request.POST[ "choice" ] )
    except ( KeyError, XChoice.DoesNotExist ):
        cont = {
            "question": p,
            "error_message": "You didn't select a choice.",
        }
        return render( request, "polls/detail.html", cont )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect( reverse( "polls:results", args=( p.id, ) ) )

def results( request, question_id ):
    question = get_object_or_404( XQuestion, pk=question_id )
    return render( request, "polls/results.html", {"question": question } )