from django.db import models


class Poll(models.Model):
    poll_name = models.CharField(max_length=200, verbose_name='Название опроса')
    pub_date = models.DateTimeField(verbose_name='Дата и время начала опроса')
    end_date = models.DateTimeField(verbose_name='Дата и время окончания опроса')
    poll_description = models.CharField(max_length=200, verbose_name='Описание опроса')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name='questions', verbose_name='Название опроса', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, verbose_name='Вопрос')
    question_type = models.CharField(max_length=200, verbose_name='Тип вопроса')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', verbose_name='Вопрос', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name='Вариант ответа')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Вариант ответов'

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    user_id = models.IntegerField()
    poll = models.ForeignKey(Poll, related_name='poll', verbose_name='Опрос', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='question', verbose_name='Вопрос', on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, related_name='choice', on_delete=models.CASCADE, verbose_name='Вариант ответа', null=True)
    choice_text = models.CharField(max_length=200, verbose_name='Ответ', null=True)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.choice_text
