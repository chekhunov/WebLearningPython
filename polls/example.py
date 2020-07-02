#from .models import Question
from polls.models import Question

first_question = Question.objects.first()
print(first_question)

