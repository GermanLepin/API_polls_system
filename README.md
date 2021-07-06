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

##### _Дополнительные сведения по проекту:_
- Изначально проект разрабатывался использую БД PostgreSQL, но при конечной отладке БД была изменена на SQLite3, в настройка остались закаментированные строчки подключения к PostgreSQL, поэтому при желании всегда можно сделать подключение к PostgreSQL.

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

## Инструкция по разворачиванию приложения:
Склонируйте репозиторий с помощью git

    https://github.com/GermanLepin/API_polls_system.git
Перейти в папку:
```bash
cd API_polls_system
```
## Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
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


### Документация API

* Если вы пользователь MAC OS или LINUX, то можно использовать при вызове команд или ординарные, или двойные кавычки 

  пример: curl --location --request POST 'http://localhost:8000/api/login/'
###
* Если вы используете WINDOWS, то только двойные кавычки 

  пример: curl --location --request POST "http://localhost:8000/api/login/")

### Получение токена пользователя: 
* Метод запроса: GET
* URL: http://localhost:8000/api/login/
* Body: 
    * username: имя пользователя
    * password: пароль
* Пример WINDOWS (используйте в username и password имя пользователя и пароль от суперюзера):
```
curl --location --request GET "http://localhost:8000/api/login/" \
--form "username=%username" \
--form "password=%password"
```
* Пример MAC OS или LINUX (используйте в username и password имя пользователя и пароль от суперюзера):
```
curl --location --request GET 'http://localhost:8000/api/login/' \
--form 'username=%username' \
--form 'password=%password'
```

### Создание опроса:
* Метод запроса: POST
* URL: http://localhost:8000/api/pollsApp/create/
* Header:
   *  Авторизация: Token userToken
* Body:
    * poll_name: название опроса
    * pub_date: дату публикации можно установить только при создании опроса, формат: YYYY-MM-DD HH:MM:SS
    * end_date: дата окончания опроса, формат: YYYY-MM-DD HH:MM:SS
    * poll_description: описание опроса
    
* Пример WINDOWS: 
```
curl --location --request POST "http://localhost:8000/api/pollsApp/create/" \
--header "Authorization: Token %userToken" \
--form "poll_name=%poll_name" \
--form "pub_date=%pub_date" \
--form "end_date=%end_date" \
--form "poll_description=%poll_description"
```
* Пример MAC OS или LINUX 
```
curl --location --request POST 'http://localhost:8000/api/pollsApp/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll_name=%poll_name' \
--form 'pub_date=%pub_date' \
--form 'end_date=%end_date' \
--form 'poll_description=%poll_description'
```

### Обновление опроса:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/pollsApp/update/[poll_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * poll_id: id опроса 
* Body:
    * poll_name: название опроса
    * end_date: дата окончания опроса, формат: YYYY-MM-DD HH:MM:SS
    * poll_description: описание опроса
* Пример WINDOWS:
```
curl --location --request PATCH "http://localhost:8000/api/pollsApp/update/[poll_id]/" \
--header "Authorization: Token %userToken" \
--form "poll_name=%poll_name" \
--form "end_date=%end_date" \
--form "poll_description=%poll_description"
```
* Пример MAC OS или LINUX
```
curl --location --request PATCH 'http://localhost:8000/api/pollsApp/update/[poll_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll_name=%poll_name' \
--form 'end_date=%end_date' \
--form 'poll_description=%poll_description'
```

### Удаление опроса:
* Request method: DELETE
* URL: http://localhost:8000/api/pollsApp/update/[poll_id]
* Header:
    * Авторизация: Token userToken
* Param:
    * poll_id
* Пример WINDOWS:
```
curl --location --request DELETE "http://localhost:8000/api/pollsApp/update/[poll_id]/" \
--header "Authorization: Token %userToken"
```
* Пример MAC OS или LINUX
```
curl --location --request DELETE 'http://localhost:8000/api/pollsApp/update/[poll_id]/' \
--header 'Authorization: Token %userToken'
```

### Просмотр всех опросов:
* Метод запроса: GET
* URL: http://localhost:8000/api/pollsApp/view/
* Header:
    * Авторизация: Token userToken
* Пример WINDOWS:
```
curl --location --request GET "http://localhost:8000/api/pollsApp/view/" \
--header "Authorization: Token %userToken"
```
* Пример MAC OS или LINUX
```
curl --location --request GET 'http://localhost:8000/api/pollsApp/view/' \
--header 'Authorization: Token %userToken'
```

### Просмотр текущих активных опросов:
* Метод запроса: GET
* URL: http://localhost:8000/api/pollsApp/view/active/
* Header:
    * Авторизация: Token userToken
* Пример WINDOWS:
```
curl --location --request GET "http://localhost:8000/api/pollsApp/view/active/" \
--header "Authorization: Token %userToken"
```
* Пример MAC OS или LINUX
```
curl --location --request GET 'http://localhost:8000/api/pollsApp/view/active/' \
--header 'Authorization: Token %userToken'
```

### Создание вопроса:
* Метод запроса: POST
* URL: http://localhost:8000/api/question/create/
* Header:
    * Авторизация: Token userToken
* Body:
    * poll: id опроса
    * question_text: текст вопроса
    * question_type: тип вопроса, который может быть только `one`, `multiple` или `text`
* Пример WINDOWS:
```
curl --location --request POST "http://localhost:8000/api/question/create/" \
--header "Authorization: Token %userToken" \
--form "poll=%poll" \
--form "question_text=%question_text" \
--form "question_type=%question_type" \
```
* Пример MAC OS или LINUX
```
curl --location --request POST 'http://localhost:8000/api/question/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type' \
```

### Обновление вопроса:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * question_id: id вопроса
* Body:
    * poll: id опроса
    * question_text: текст вопроса
    * question_type: тип вопроса, который может быть только `one`, `multiple` или `text`
* Пример WINDOWS:
```
curl --location --request PATCH "http://localhost:8000/api/question/update/[question_id]/" \
--header "Authorization: Token %userToken" \
--form "poll=%poll" \
--form "question_text=%question_text" \
--form "question_type=%question_type" \
```
* Пример MAC OS или LINUX
```
curl --location --request PATCH 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type' \
```


### Удаление вопроса:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/question/update/[question_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * question_id: id вопроса
* Пример WINDOWS:
```
curl --location --request DELETE "http://localhost:8000/api/question/update/[question_id]/" \
--header "Authorization: Token %userToken" \
--form "poll=%poll" \
--form "question_text=%question_text" \
--form "question_type=%question_type" \
```
* Пример MAC OS или LINUX
```
curl --location --request DELETE 'http://localhost:8000/api/question/update/[question_id]/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question_text=%question_text' \
--form 'question_type=%question_type' \
```

### Создание выбора ответа:
* Метод запроса: POST
* URL: http://localhost:8000/api/choice/create/
* Header:
    * Авторизация: Token userToken
* Body:
    * question: id вопроса
    * choice_text: выбор ответа
* Пример WINDOWS:
```
curl --location --request POST "http://localhost:8000/api/choice/create/" \
--header "Authorization: Token %userToken" \
--form "question=%question" \
--form "choice_text=%choice_text"
```
* Пример MAC OS или LINUX
```
curl --location --request POST 'http://localhost:8000/api/choice/create/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Обновление выбора отвтета:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * choice_id: id выбора ответа
* Body:
    * question: id вопроса
    * choice_text: выбор ответа
* Пример WINDOWS:
```
curl --location --request PATCH "http://localhost:8000/api/choice/update/[choice_id]/" \
--header "Authorization: Token %userToken" \
--form "question=%question" \
--form "choice_text=%choice_text"
```
* Пример MAC OS или LINUX
```
curl --location --request PATCH 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Удаление выбора ответа:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/choice/update/[choice_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * choice_id: id выбора ответа
* Пример WINDOWS:
```
curl --location --request DELETE "http://localhost:8000/api/choice/update/[choice_id]/" \
--header "Authorization: Token %userToken" \
--form "question=%question" \
--form "choice_text=%choice_text"
```
* Пример MAC OS или LINUX
```
curl --location --request DELETE 'http://localhost:8000/api/choice/update/[choice_id]/' \
--header 'Authorization: Token %userToken' \
--form 'question=%question' \
--form 'choice_text=%choice_text'
```

### Создание ответа:
* Метод запроса: POST
* URL: http://localhost:8000/api/answer/create/
* Header:
    * Авторизация: Token userToken
* Body:
    * poll: id опроса
    * question: id вопроса
    * choice: если тип вопроса `one` или `multiple`, тогда выбираем `choice_id`, иначе `null`
    * choice_text: если тип вопроса-`text`, создаем текстовый ответ, иначе `null`
* Пример WINDOWS:
```
curl --location --request POST "http://localhost:8000/api/answer/create/" \
--header "Authorization: Token %userToken" \
--form "poll=%poll" \
--form "question=%question" \
--form "choice=%choice" \
--form "choice_text=%choice_text"
```
* Пример MAC OS или LINUX
```
curl --location --request POST 'http://localhost:8000/api/answer/create/' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice' \
--form 'choice_text=%choice_text'
```

### Обновление ответа:
* Метод запроса: PATCH
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * answer_id: id ответа
* Body:
    * poll: id опроса
    * question: id вопроса
    * choice: если тип вопроса `one` или `multiple`, тогда выбираем `choice_id`, иначе `null`
    * choice_text: если тип вопроса-`text`, создаем текстовый ответ, иначе `null`
* Пример WINDOWS:
```
curl --location --request PATCH "http://localhost:8000/api/answer/update/[answer_id]" \
--header "Authorization: Token %userToken" \
--form "poll=%poll" \
--form "question=%question" \
--form "choice=%choice" \
--form "choice_text=%choice_text"
```
* Пример MAC OS или LINUX
```
curl --location --request PATCH 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken' \
--form 'poll=%poll' \
--form 'question=%question' \
--form 'choice=%choice' \
--form 'choice_text=%choice_text'
```

### Удаление ответа:
* Метод запроса: DELETE
* URL: http://localhost:8000/api/answer/update/[answer_id]/
* Header:
    * Авторизация: Token userToken
* Param:
    * answer_id: id ответа
* Пример WINDOWS:
```
curl --location --request DELETE "http://localhost:8000/api/answer/update/[answer_id]" \
--header "Authorization: Token %userToken"
```
* Пример MAC OS или LINUX
```
curl --location --request DELETE 'http://localhost:8000/api/answer/update/[answer_id]' \
--header 'Authorization: Token %userToken'
```

### Просмотр ответов пользователя:
* Метод запроса: GET
* URL: http://localhost:8000/api/answer/view/[user_id]/
* Param:
    * user_id: id пользователя 
* Header:
    * Авторизация: Token userToken
* Пример WINDOWS:
```
curl --location --request GET "http://localhost:8000/api/answer/view/[user_id]" \
--header "Authorization: Token %userToken"
```
* Пример MAC OS или LINUX
```
curl --location --request GET 'http://localhost:8000/api/answer/view/[user_id]' \
--header 'Authorization: Token %userToken'
```

