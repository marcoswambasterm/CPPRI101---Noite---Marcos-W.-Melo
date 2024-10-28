from django.urls import path
from . import views

urlpatterns = [
    path('vitimas/', views.lista_vitimas, name='lista_vitimas'),
    path('vitimas/nova-pessoa/', views.criar_pessoa, name='criar_pessoa'),
    path('editar-pessoa/<int:pk>/', views.editar_pessoa, name='editar_pessoa'),
    path('vitimas/deletar-pessoa/<int:pk>/', views.deletar_pessoa, name='deletar_pessoa'),

    path('vitimas/novo-pet/', views.criar_pet, name='criar_pet'),
    path('vitimas/editar-pet/<int:pk>/', views.editar_pet, name='editar_pet'),
    path('vitimas/deletar-pet/<int:pk>/', views.deletar_pet, name='deletar_pet'),
]
