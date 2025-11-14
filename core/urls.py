from django.urls import path, re_path

from core.views import IndexView, AddQuestionView

urlpatterns = [
    path('', IndexView.as_view()),
    path('/ask', AddQuestionView.as_view()),
]