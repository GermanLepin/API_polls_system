from django.urls import path
from Polling import apiviews


app_name = 'pollsApp'
urlpatterns = [
    path('login/', apiviews.login, name='login'),
    # Опросы
    path('pollsApp/create/', apiviews.poll_create, name='poll_create'),
    path('pollsApp/update/<int:poll_id>/', apiviews.poll_update, name='poll_update'),
    path('pollsApp/view/', apiviews.poll_view, name='poll_view'),
    path('pollsApp/view/active/', apiviews.active_poll_view, name='active_poll_view'),
    # Вопрос (question)
    path('question/create/', apiviews.question_create, name='question_create'),
    path('question/update/<int:question_id>/', apiviews.question_update, name='question_update'),
    # Выбор (choice)
    path('choice/create/', apiviews.choice_create, name='choice_create'),
    path('choice/update/<int:choice_id>/', apiviews.choice_update, name='choice_update'),
    # Ответ (answer)
    path('answer/create/', apiviews.answer_create, name='answer_create'),
    path('answer/view/<int:user_id>/', apiviews.answer_view, name='answer_view'),
    path('answer/update/<int:answer_id>/', apiviews.answer_update, name='answer_update')
]

