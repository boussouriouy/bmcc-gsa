from django.urls import path

from . import views

urlpatterns = [
    path('', views.member, name='member'),
    path('form/', views.form, name='form'),
    path('<int:detail_id>/', views.detail, name='detail')
]
