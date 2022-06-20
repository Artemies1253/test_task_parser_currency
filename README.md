# test_task_parser_currency
## Технологии: 
Для запуска бекенд проекта используется докер, используем команды docker-compose build docker-compose up

Для запуска парсинга используется консольная команда python manage.py fill_in_database (не забываем что все команды нужно прокидывать в докер, если вы запустились через него)

Название всех валют находиться в классе src.parsers.emums.ValueInvestingComEnum , необходимо использовать эти названия что бы обращаться к API(из консоли по второму уровню и к полноценному бекенду с 3 уровня)

Что бы добавить новую валюту для парсинга нужно в файл src.parsers.emums.ValueInvestingComEnum забить имя и найти значение symbol на сайте (https://ru.investing.com/charts/cryptocurrency-charts) для этого нужно нажать F12, найти запрос history? из этого запроса параметр symbol переносим в src.parsers.emums.ValueInvestingComEnum.

good_luck_have_fan))
