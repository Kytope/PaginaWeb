"""
URL configuration for MiProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from MiProyecto.views import inicio
from MiProyecto.views import mi_login
from MiProyecto.views import logout_view
from MiProyecto.views import reservar_hora
from MiProyecto.views import productos_disponibles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  # Nombre de la URL para la vista de inicio
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reservar/', reservar_hora, name='reservar_hora'),
    path('productos-disponibles/', productos_disponibles, name='productos_disponibles'),
    path('login/', mi_login, name='login'),  # Nombre de la URL para la vista de inicio de sesión
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

