# Weather App — wttr2.py

Простой скрипт для получения прогноза погоды с сервиса [wttr.in](https://wttr.in).

## Описание

Файл `wttr2.py` содержит функцию `get_wttr(location)`, которая:
- Отправляет запрос на `wttr.in` с указанным местоположением.
- Использует параметры форматирования (`nTq`) для краткого и чистого вывода.
- Поддерживает мультиязычность (по умолчанию — английский).
- Выводит прогноз в консоль.

## Используемые параметры

- `n` — narrow version (only day and night).
- `T` — switch terminal sequences off (no colors).
- `q` — quiet version (no "Weather report" text)
- `lang=en` — язык ответа (можно изменить).

Подробнее об опциях [wttr.in/:help](https://wttr.in/:help)

Пример URL: `http://wttr.in/Moscow?nTq&lang=en`

## Зависимости

- `requests` — для HTTP-запросов.
