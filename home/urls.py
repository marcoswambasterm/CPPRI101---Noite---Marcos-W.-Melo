from django.urls import path, reverse_lazy
from . import views
from .views import IndexView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vitimas/', views.lista_vitimas, name='lista_vitimas'),
    path('login/', LoginView.as_view(template_name='login.html', extra_context={'titulo': 'Autenticação'}), name= 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('alterar_senha/', PasswordChangeView.as_view(template_name='login.html',
                                                                      extra_context={'titulo': 'Alterar Senha'}, success_url=reverse_lazy('index')),name='alterar_senha'),
]

