# signals_likes
Пример  сигнала для подсчета лайков в проекте Django. 
Такой подход может оптимизировать количество запросов к БД, но применять его стоит с осторожностью. 

Стек: python 3.10, Django 4.1

В репозитории три файла: 
1. models.py - содержит полноценную модель изображения
2. signal.py - содержит сигнал который обновляет кол-во лайков
3. apps.py - пример обновления файла приложения.

Ссылка на документацию по сигналам: https://docs.djangoproject.com/en/5.1/ref/applications/


An example of a signal for counting likes in the Django project. This approach can optimize the number of database queries, but it should be used with caution. 

Stack: python 3.10, Django 4.1

There are three files in the repository:

1. models.py - contains a full-fledged image
2. model signal.py - contains a signal that updates the number of likes
3. apps.py - an example of updating an application file.


Link to the signals documentation: https://docs.djangoproject.com/en/5.1/ref/applications/
