from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('new/', views.new, name='new'),
    path('edit/<int:pk>', views.RecordUpdateView.as_view(), name='edit'),
    path('delete/<int:id>', views.destroy, name='delete'),
]
