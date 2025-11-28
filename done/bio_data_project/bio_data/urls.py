from django.urls import path
from . import views

urlpatterns=[
    path('',views.bio_data_form,name='bio_data_form'),
    path('display_bio_data/',views.display_bio_data,name='display_bio_data'),
]