 ##   Установка приложения
1. Приложение на языке python(необходимо иметь на компьютере установленный python).  
Выполнить клонирование репозитория с github 
```shell
    git clone https://github.com/vink77/HW19_2.git
```
2. Подключить виртуальное окружение
```shell
  python -m venv venv
  ```
```shell
   venv/Scripts/activate
```
3. Установить необходимые зависимости в виртуальное окружение.  
```shell
   pip install -r requirements.txt
```
4.Установить базу данных postgres и менеджер pgAdmin4.   
      Создать базу **'DB_magazin'**  
      Создать и импортировать миграции
```shell
    python manage.py makemigrations
  ```
```shell
    python manage.py migrate 
```

5. Заполнить базу данных командой в терминале:
```shell
   python manage.py fill
```
6. Запустить сервер командой в терминале:

```shell
   python manage.py runserver
```
7. Перейти по ссылке 127.0.0.1
