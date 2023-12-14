# echobot
Бот который отправляет копию полученного сообщения обратно в тот же чат

## Установка и настройка

Создайте и активируйте окружение
```sh
python3 -m venv .venv
source .venv/bin/activate
```

Установите зависимости
```sh
python -m pip install -R requirements.txt
```


## Запуск

Укажите нужную переменную окружения
```sh
export ECHOBOT_API_TOKEN=***
```

```sh
python echobot.py
```

