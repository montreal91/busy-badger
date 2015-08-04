
from django.db import models

class XQuestion( models.Model ):
    question_text = models.CharField( max_length=200 )
    pub_date = models.DateTimeField( "date published" )

    def __str__( self ):
        return self.question_text

class XChoice( models.Model ):
    question = models.ForeignKey( XQuestion )
    choice_text = models.CharField( max_length=200 )
    votes = models.IntegerField( default=0 )

    def __str__( self ):
        return self.choice_text
