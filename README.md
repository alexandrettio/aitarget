# aitarget
## Подготовка к запуску
создайте файл `web-variables.env` или проинициализируйте соответствующие переменные окружения 
```
SECRET_KEY= Ключ для приложения джанго
EMAIL_HOST=smtp хост, с которого будет производиться рассылка которой будет производиться рассылка
EMAIL_PORT=порт smtp
EMAIL_HOST_USER=владелец почты, с которой будет производиться рассылка
EMAIL_HOST_PASSWORD= пароль от почты владельца ящика
```

## Запуск проекта
```
git clone https://github.com/alexandrettio/aitarget/tree/master/library
cd library
docker-compose up -d
```
## Оговорки
Проект представляет собой способ решить тестовое задание за минимальное время. Не ставит своей целью поддержание кода в дальнейшем, по этой причине не покрыт тестами. А id сущностей выбраны привычными мен uuid4 которые удобно мерджить если приложения работают на нескольких инстансах без промежуточной синхронизации, что в общем случае не является хорошим решением.
