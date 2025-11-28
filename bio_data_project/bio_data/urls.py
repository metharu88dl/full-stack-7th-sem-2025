from django.urls import path
from . import views

urlpatterns=[
    path('',views.bio_data_form, name="bio_data_form"),
    path('/display',views.display_biodata,name="display_biodata"),
]
