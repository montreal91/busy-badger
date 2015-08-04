
from django.shortcuts           import render, get_object_or_404
from django.http                import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers   import reverse
from django.views               import generic

from .models                    import XQuestion, XChoice


class XIndexView( generic.ListView ):
    template_name       = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset( self ):
        return XQuestion.objects.order_by( "-pub_date" )[ :10 ]


class XDetailView( generic.DetailView ):
    model           = XQuestion
    template_name   = "polls/detail.html"


class XResultsView( generic.DetailView ):
    model           = XQuestion
    template_name   = "polls/results.html"


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
