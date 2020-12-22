## پروژه مبانی جنگو 
: برای کلون و احرای کردن پروژه در کامپیوتر  خود، به ترتیب کار های زیر را انجان دهید

```sh
$ git clone origin https://github.com/Cypherspark/djnago-FC99.git
$ python -m venv env
$ env\\Scripts\\activate
$ cd Proj 
$ pip install requirements
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

در نهایت آدرس زیر را در مررگر خود چک کنید:

```sh
127.0.0.1:8000
```