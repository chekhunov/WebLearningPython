from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
import random

from django.template import loader

from polls.models import Question


def index(request: WSGIRequest) -> HttpResponse:
    """
    this function
    :param request:
    :return:
    """
    response = HttpResponse
    dec = {'fs': 5, 'hg': 10}
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'example': 125,
        'dec': dec,
        'response': response,
    }

    print(template.render(context, request))
    return HttpResponse(template.render(context, request))


def example(request: WSGIRequest) -> HttpResponse:
    """

    :param request:
    :return:
    """
    return HttpResponse(f"result: {random.randint}")


def detail(request: WSGIRequest, question_id: int) -> HttpResponse:
    """

    :param request:
    :param question_id:
    :return:
    """
    return HttpResponse("You're looking at question %s." % question_id)


def results(request: WSGIRequest, question_id: int) -> HttpResponse:
    """

    :param request:
    :param question_id:
    :return:
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request: WSGIRequest, question_id: int) -> HttpResponse:
    """

    :param request:
    :param question_id:
    :return:
    """
    return HttpResponse("You're voting on question %s." % question_id)
