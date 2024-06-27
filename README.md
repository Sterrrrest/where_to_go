# Куда пойти — Москва глазами Артёма
Данный проект нужен для тех, кто хочет посетить интересные места по мнению Артема.
    
Сайт можно найти по адресу https://sterrrrest.pythonanywhere.com/

## Как скачать

Для запуска проекта у вас уже должен быть установлен Python 3.11

- Скачайте код. Проект находится тут - https://github.com/Sterrrrest/where_to_go/tree/main. Выберите "Download" -> "Download ZIP".
- Далее установите переменные окружения.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следущие переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. Выключается значением `False`.
- `SECRET_KEY` — секретный ключ проекта. Например: `erofheronoirenfoernfx49389f43xf3984xf9384`.
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `STATIC_URL` — по умолчанию это `'/static/'`. [Что такое STATIC_URL](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-STATIC_URL).

## Запуск проекта

- Создайте окружение `python3 -m venv env`
- Запустите его `source env/bin/activate`
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте базу данных `python3 manage.py migrate`
- Для входа в панель админ создайте суперпользователя `python3 manage.py createsuperuser`
- Запустите сервер командой `python3 manage.py runserver`

В качестве веб-сервера можно использовать локально:

- Сайт - http://127.0.0.1:8000/
- Админ панель - http://127.0.0.1:8000/admin/

## Настройки

Внизу справа на странице можно включить отладочный режим логгирования.

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Добавление новых мест на карту

Для загрузки новых мест на карту, надо запустить команду:

`python3 manage.py load-places` И указать URL файла JSON

## Пример запуска

Для запуска проекта наберите `python3 manage.py`, затем команду `load-places` и URL по примеру ниже:

-   `python3 manage.py load-places https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%9B%D0%B0%D0%B3%D0%B5%D1%80%D1%8C%20%C2%AB%D0%9F%D0%BE%D0%B4%D0%BC%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D0%BD%D1%8B%D0%B9%C2%BB.json`

## Источники данных

Фронтенд получает данные из базы данных.


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).

