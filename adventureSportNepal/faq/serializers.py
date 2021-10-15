from rest_framework import serializers
from .models import *

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        exclude = ('id', 'faq')
    

class FaqSerializer(serializers.ModelSerializer):
    question_and_answer = QuestionAnswerSerializer(many=True)

    class Meta:
        model = Faq
        fields = ('label', 'question_and_answer')