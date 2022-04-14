from django.urls import path
from basic_app import views

# FOR TEMPLATE TAGGING:
app_name = 'basic_app'

urlpatterns=[
    path('information/',views.info,name='info'),
    path('other/',views.other,name='other'),
]
