# Alegrosz


## Algorytm tworzenia funkcjinalności w django

1.Czy potrzebne nowe django apps?

    - 'django-admin startapp <name>'
    - rejestruje w settings.py -> INSTALLED_APPS

2. Czy potrzebne dane?
   -tworze modele w <appname/models.py>
   -'python manage.py makemigrations <app_label>'
   -'python ./manage.py migrate <app_label>'
3. Czy potrzebuje obsluge w django-admin(CMS)?
   - rejestruje modele w <app_name>/admin.py
2. Czy potrzebna jest logika? (View)
    - <app_name/views.py
3. Czy potrzebny jest routing?