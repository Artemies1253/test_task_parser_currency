# test_task_parser_currency
## Технологии: 
Для запуска бекенд проекта используется докер, используем команды docker-compose build docker-compose up

Можно запускать и без докера 
python manage.py migrate

python manage.py runserver

Для запуска парсинга используется консольная команда python manage.py fill_in_database (не забываем что все команды нужно прокидывать в докер, если вы запустились через него)


Что бы добавить новую валюту для парсинга нужно в файл src.parsers.emums.ValueInvestingComEnum забить имя и найти значение symbol на сайте (https://ru.investing.com/charts/cryptocurrency-charts) для этого нужно нажать F12, найти запрос history? из этого запроса параметр symbol переносим в src.parsers.emums.ValueInvestingComEnum.
