import typing as t

from django.core.management.base import BaseCommand

from core.models import Question, User


FAKE_QUESTION_DETAILED = """
Прохожу курс по машинному обучению с нуля, где алгоритмы пишутся вручную. Как в методе ближайших соседей посчитать евклидово расстояние всех точек тестовой выборки до точек обучающей выборки? Сделал такое с помощью циклов, но вычисляется очень долго, хотелось бы узнать как переделать на броадкастинг.

def euclid(self, data1, data2):
    d = []
    for i in range(len(data1)):
        d.append(sum((data2 - data1.iloc[i])**2) ** 0.5)
    return d   

def NN(self, X_test, X):
    distance = [{self.y.iloc[i]: self.euclid(X_test, X.iloc[i])} for i in range(len(X))]
    return distance
"""

class Command(BaseCommand):
    help = 'Генерация сущностей по модели Вопроса'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=100)

    def get_exist_user(self) -> t.Optional[User]:
        return User.objects.filter(is_superuser=True).first()

    def handle(self, *args, **options):
        count = options.get('count')
        count_exists_questions = Question.objects.all().count()
        questions_to_create = []
        for n in range(count):
            questions_to_create.append(Question(
                title=f"Вопрос #{count_exists_questions + n + 1}",
                detailed=FAKE_QUESTION_DETAILED,
                author=self.get_exist_user()
            ))

        Question.objects.bulk_create(questions_to_create, batch_size=100)
        print("Было создано {} вопрос в БД".format(len(questions_to_create)))
