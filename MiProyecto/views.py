from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.db.models import Q
from .forms import ReservaForm

from MiProyecto.models import Reserva
from MiProyecto.models import Producto
from .utils import generar_horas_disponibles


def inicio(request):
    return render(request, 'inicio.html')

def mi_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # El inicio de sesión ha tenido éxito, puedes redirigir al usuario a una página de inicio o a donde desees.
            return redirect('inicio')
        else:
            # Las credenciales no son válidas, puedes mostrar un mensaje de error en tu plantilla.
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
    else:
        # Si no se ha enviado un formulario, simplemente muestra el formulario de inicio de sesión.
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    # Redirige al usuario a la página de inicio u otra página deseada después del cierre de sesión.
    return redirect('inicio')


def reservar_hora(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            # Asigna el usuario actual a la reserva (puedes ajustarlo según tu autenticación)
            reserva.usuario = request.user
            reserva.save()
            # Redirige o realiza otras acciones después de la reserva
            return redirect('página_de_confirmación')
    else:
        form = ReservaForm()
    return render(request, 'reservar_hora.html', {'form': form})


def productos_disponibles(request):
    # Recupera los productos disponibles (por ejemplo, aquellos con stock > 0)
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, 'productos_disponibles.html', {'productos': productos})