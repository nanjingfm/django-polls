#coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.

@require_http_methods(['GET'])
def index(request):
    questions = Question.objects.order_by('-pub_date').filter(status=Question.ACTIVE)[:5]
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
            return HttpResponseRedirect(reverse('polls:detail', args=(question_id,)))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {
        'question': question
    })

def search(request):
    keywords = request.POST.get('keywords', None)
    if keywords is not None:
        questions = Question.objects.order_by('-pub_date').filter(question_text__contains=keywords.strip(' '))
        return render(request, "list.html", {
            'questions': questions,
            'searchkeywords': keywords
        })
    else:
        return HttpResponseRedirect(reverse('polls:index'))
