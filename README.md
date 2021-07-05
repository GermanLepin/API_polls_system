# API_polls_system

## Описание ТЗ:

##### _Функционал для администратора системы:_
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

##### _Функционал для пользователей системы:_
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя


## Окружение проекта:
  * asgiref==3.3.1
  * Django==2.2.10
  * django-extensions==3.1.0
  * django-rest-authtoken==2.1.3
  * djangorestframework==3.12.4
  * Pillow==8.3.0
  * psycopg2==2.9.1
  * pytz==2020.5
  * sqlparse==0.4.1


Склонируйте репозиторий с помощью git

    https://github.com/GermanLepin/API_system_polling.git
Перейти в папку:
```bash
cd API_system_polling
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **req.txt**:
```bash
pip install -r req.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
* Введите требуемое имя пользователя, электронную почту и пароль:
```bash
Username (leave blank to use 'admin'): admin
Email address: pass
Password: admin
Password (again): admin
Superuser created successfully.
```

* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/


### _Документация API_ 
### Если вы пользователь MAC OS или LINUX, то можно импользовать при вызове команд или ординарные, или двойные кавычки 
(пример curl --location --request POST 'http://localhost:8000/api/login/')
### а если вы используете WINDOWS, то только двойные кавычки 
(пример curl --location --request POST "http://localhost:8000/api/login/")

### Чтобы получить токен пользователя: 
* Request method: GET
* URL: http://localhost:8000/api/login/
* Body: 
    * username: 
    * password: 
* Пример (используйте в username и password логин и пароль от суперюзера:
```
curl --location --request GET "http://localhost:8000/api/login/" \
--form "username=%username" \
--form "password=%password"
```

### Чтобы создать опрос:
* Request method: POST
* URL: http://localhost:8000/api/surveysApp/create/
* Header:
   *  Авторизация: Token userToken
* Body:
    * poll_name: название опроса
    * pub_date: дату публикации можно установить только при создании опроса, формат: YYYY-MM-DD HH:MM:SS
    * end_date: дата окончания опроса, формат: YYYY-MM-DD HH:MM:SS
    * poll_description: описание опроса
* Example: 
```
curl --location --request POST "http://localhost:8000/api/pollsApp/create/" \
--header "Authorization: Token %userToken" \
--form "poll_name=%poll_name" \
--form "pub_date=%pub_date" \
--form "end_date=%end_date" \
--form "poll_description=%poll_description"
```

### Обновить опрос:
* Request method: PATCH
* URL: http://localhost:8000/api/pollsApp/update/[survey_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * survey_id 
* Body:
    * poll_name: название опроса
    * end_date: дата окончания опроса, формат: YYYY-MM-DD HH:MM:SS
    * poll_description: описание опроса
* Example:
```
curl --location --request PATCH "http://localhost:8000/api/surveysApp/update/[survey_id]/" \
--header "Authorization: Token %userToken" \
--form "poll_name=%survey_name" \
--form "end_date=%end_date" \
--form "poll_description=%survey_description"
```

### Удалить опрос:
* Request method: DELETE
* URL: http://localhost:8000/api/pollsApp/update/[survey_id]
* Header:
    * Авторизация: Token userToken
* Param:
    * survey_id
Example:
```
curl --location --request DELETE "http://localhost:8000/api/surveysApp/update/[survey_id]/" \
--header "Authorization: Token %userToken"
```

### Посмотреть все опросы:
* Request method: GET
* URL: http://localhost:8000/api/surveysApp/view/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/surveysApp/view/' \
--header 'Authorization: Token %userToken'
```

### Просмотр текущих активных опросов:
* Request method: GET
* URL: http://localhost:8000/api/surveysApp/view/active/
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/surveysApp/view/active/' \
--header 'Authorization: Token %userToken'
```

### Создаем вопрос:
* Request method: POST
* URL: http://localhost:8000/api/question/create/
* Header:
    * Authorization: Token userToken
* Body:
    * survey: id of survey 
    * question_text: 
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Обновляем вопрос:
* Request method: PATCH
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Body:
    * survey: id of survey 
    * question_text: question
    * question_type: can be only `one`, `multiple` or `text`
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Удаляем вопрос:
* Request method: DELETE
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * question_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type \
```

### Создаем выбор:
* Request method: POST
* URL: http://localhost:8000/api/choice/create/
* Header:
    * Authorization: Token userToken
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновляем выбор:
* Request method: PATCH
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Body:
    * question: id of question
    * choice_text: choice
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновляем выбор:
* Request method: DELETE
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * choice_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Создаем ответ:
* Request method: POST
* URL: http://localhost:8000/api/answer/create/
* Header:
    * Authorization: Token userToken
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Обновляем ответ:
* Request method: PATCH
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Body:
    * survey: id of survey
    * question: id of question
    * choice: if question type is one or multiple then it’s id of choice else null
    * choice_text: if question type is text then it’s text based answer else null
* Example:
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'survey=%survey' \
--form 'question=%question' \
--form 'choice=%choice \
--form 'choice_text=%choice_text'
```

### Удаляем ответ:
* Request method: DELETE
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Authorization: Token userToken
* Param:
    * answer_id
* Example:
```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

### Просматриваем ответы пользователя:
* Request method: GET
* URL: http://localhost:8000/api/answer/view/[user_id]/
* Param:
    * user_id
* Header:
    * Authorization: Token userToken
* Example:
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
