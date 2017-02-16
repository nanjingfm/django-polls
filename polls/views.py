#coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.

@require_http_methods(['GET'])
def index(request):
    questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, "list.html", {
        'questions': questions
    })

@require_http_methods(['GET'])
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "vote.html", {
        'question': question
    })

@require_http_methods(['POST'])
def saveVote(request):
    question_id = request.POST.get('question_id', None)
    choice_id = request.POST.get('choice_id', None)

    if question_id is not None and choice_id is not None:
        question = get_object_or_404(Question, pk=question_id)
        choice = question.isChildChoice(choice_id)
        if not choice:
            return render(request, "vote.html", {
                'question': question,
                'error': '系统错误'
            })
        else:
            choice.votes += 1
            choice.save()
            return HttpResponseRedirect(reverse('polls:index'))

def detail(request):
    return render(request, "detail.html", {
        'question': '111'
    })