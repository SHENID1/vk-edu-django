import math
from aiohttp.web_urldispatcher import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse


# Create your views here.
def indexMain(request):
    # print(request)
    return render(request, '6.1/index.html')


def indexAnswer(request):
    # print(request)
    return render(request, '6.2/base.html')


class IndexView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.1/index.html'
    COUNT_FAKE_QUESTIONS = 15
    QUESTIONS_PER_PAGE = 5

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_fake_questions(self):
        return [{
            "id": i,
            "question_text": f"Вопрос #{i}",
            "question_detail_text": "You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions."
        } for i in range(1, self.COUNT_FAKE_QUESTIONS + 1)]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        page = int(self.request.GET.get('page', 1))
        context["page"] = page
        context["count_questions"] = self.COUNT_FAKE_QUESTIONS
        context["questions_per_page"] = self.QUESTIONS_PER_PAGE
        context["max_page"] = math.ceil(self.COUNT_FAKE_QUESTIONS / self.QUESTIONS_PER_PAGE)
        context['pages'] = [i for i in range(1, context["max_page"] + 1)]

        if page == 1:
            context['new_questions'] = self.get_fake_questions()[0: self.QUESTIONS_PER_PAGE]
        else:
            context['new_questions'] = self.get_fake_questions()[(page - 1) * self.QUESTIONS_PER_PAGE: ((
                                                                                                                page - 1) * self.QUESTIONS_PER_PAGE) + self.QUESTIONS_PER_PAGE]

        return context


class AddQuestionView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.2/base.html'

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(AddQuestionView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AddQuestionView, self).get_context_data(**kwargs)
        return context


class QuestionView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.3/base.html'

    def get_fake_data(self, id):
        return {
            "id": id,
            "question_title": f"Вопрос #{id}",
            "question_detail_text": "You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.",
            "author_rating": 5,
            "avatar_url": "https://i.pinimg.com/736x/41/6c/81/416c81ffd68216ad4a9c66932015aac4.jpg",
            "answers": [{
                "answer_text": "WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.",
                "correct": False,
                "rating": 5,
                "avatar_url": "https://i.pinimg.com/736x/41/6c/81/416c81ffd68216ad4a9c66932015aac4.jpg",
            },{
                "answer_text": "Python top",
                "correct": True,
                "rating": 6,
                "avatar_url": "https://cdn.discordapp.com/attachments/1061702220686577795/1437549172805861517/hyrax-rock-hyrax.gif?ex=6913a57f&is=691253ff&hm=fcc72870ecb0014f95067d281b2f3b798c3adde2742af4c02a7512cdfb37cfd7&",
            }
            ]
        }

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(QuestionView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        id = int(self.request.GET.get('id', 1))
        data = self.get_fake_data(id)
        context["avatar_url"] = data["avatar_url"]
        context["question_title"] = data["question_title"]
        context["question_detail_text"] = data["question_detail_text"]
        context["author_rating"] = data["author_rating"]
        context["answers"] = data["answers"]

        return context

class TopQuestionView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.4/base.html'
    COUNT_FAKE_QUESTIONS = 15
    QUESTIONS_PER_PAGE = 5

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(TopQuestionView, self).dispatch(request, *args, **kwargs)

    def get_fake_questions(self, tag):
        return [{
            "tag": tag,
            "id": i,
            "question_text": f"Вопрос #{i}",
            "question_detail_text": "You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions."
        } for i in range(1, self.COUNT_FAKE_QUESTIONS + 1)]

    def get_context_data(self, **kwargs):
        context = super(TopQuestionView, self).get_context_data(**kwargs)
        page = int(self.request.GET.get('page', 1))
        context["page"] = page
        context["count_questions"] = self.COUNT_FAKE_QUESTIONS
        context["questions_per_page"] = self.QUESTIONS_PER_PAGE
        context["max_page"] = math.ceil(self.COUNT_FAKE_QUESTIONS / self.QUESTIONS_PER_PAGE)
        context['pages'] = [i for i in range(1, context["max_page"] + 1)]

        if page == 1:
            context['new_questions'] = self.get_fake_questions()[0: self.QUESTIONS_PER_PAGE]
        else:
            context['new_questions'] = self.get_fake_questions()[(page - 1) * self.QUESTIONS_PER_PAGE: ((page - 1) * self.QUESTIONS_PER_PAGE) + self.QUESTIONS_PER_PAGE]

        return context
    def get_fake_data(self, tag):
        return {
            "tag": tag,  # ← используем переданный тег
            "questions": [{
                "id": 3,
                "question_text": f"Вопрос по тегу '{tag}'",
                "question_detail_text": "You have 18 unapplied migration(s)..."
            }]
        }


    def get_context_data(self, **kwargs):
        context = super(TopQuestionView, self).get_context_data(**kwargs)
        tag = self.request.GET.get('tag', "bender")
        data = self.get_fake_data(tag)
        context["tag"] = data["tag"]
        context["question"] = data["tag"]

        return context

class SettingsView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.5/base.html'

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(SettingsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        return context

class LoginView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.6/base.html'

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

class RegisterView(TemplateView):
    http_method_names = ['get', ]
    template_name = '6.7/base.html'

    def dispatch(self, request, *args, **kwargs):
        # print(request.GET)
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        return context
