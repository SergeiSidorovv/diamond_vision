1) Склонировать репозиторий
git clone https://github.com/SergeiSidorovv/diamond_vision.git

2) Создать новый локальный репозиторий 
git init

3) Установить зависимости
pip install -r requirements.txt


Задание с email

1) Перейти в директорию email_domen
2) Запустить команду python main.py


Задание с ботом
1) Создать файл .env на уровне requirements.txt
2) Добавить токен телеграм бота
3) Создать в телеграме закрытый чат с ботом, написать туда сообщение
4) Перейти в директорию telegram 
5) Запустить команду python main.py
6) Ввести в консоли id чата, его можно получить по адресу https://api.telegram.org/bot{BOT_TOKEN}/getUpdates
Скобки {} при добавлении токена убираем
7)Копируем отрицательный id, примерно из такого json {"id":-5069554201,"title":"chat2","type":"group"}. 
Id должен быть отрицательным 
