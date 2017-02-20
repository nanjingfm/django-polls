from django.utils.deprecation import MiddlewareMixin
from polls.models import Question
class CommonMiddleware(MiddlewareMixin):
    # Check if client IP is allowed
    def process_view(self, request, view_func, view_args, view_kwargs):
        top5_questions = Question.objects.order_by('question_text')[:5]
        return None