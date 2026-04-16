---

1. Create app
   Run: python manage.py startapp vazifa2

---

2. Update settings.py
   Open settings.py → find INSTALLED_APPS → add:
   rest_framework
   vazifa2

---

3. Create model (vazifa2/models.py)
   Create class Vazifa2 with fields:

* title → CharField (max_length=200)
* is_active → BooleanField (default=True)
* status → CharField with choices: yangi, jarayonda, tugadi (default='yangi')

Also add **str** method returning title

---

4. Run migrations
   Run:
   python manage.py makemigrations
   python manage.py migrate

---

5. Create serializer (vazifa2/serializers.py)
   Create ModelSerializer:

* model = Vazifa2
* fields = '**all**'

---

6. Create view (vazifa2/views.py)
   Create ModelViewSet:

* queryset = Vazifa2.objects.all()
* serializer_class = Vazifa2Serializer

---

7. Create urls inside app (vazifa2/urls.py)

* Import DefaultRouter
* Register Vazifa2ViewSet with route 'vazifa2'
* Include router.urls in urlpatterns

---

8. Connect main urls (project urls.py)
   Open main urls.py and add:
   path('vazifa2/', include('vazifa2.urls'))

---

9. Run server
   Run: python manage.py runserver

---

10. Open in browser
    Go to:
    [http://127.0.0.1:8000/vazifa2/vazifa2/](http://127.0.0.1:8000/vazifa2/vazifa2/)

---

Result:

* GET list
* POST form (title, is_active, status)
* Full CRUD working

