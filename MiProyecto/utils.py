from datetime import datetime, timedelta
from MiProyecto.models import Reserva  # Asegúrate de importar el modelo Reserva

def generar_horas_disponibles():
    # Obtén el primer día del mes actual y el último día del mes actual
    fecha_inicio = datetime(datetime.today().year, datetime.today().month, 1)
    fecha_fin = fecha_inicio.replace(day=1, month=(fecha_inicio.month % 12) + 1)

    # Consulta las reservas existentes dentro del rango de fechas
    reservas_existentes = Reserva.objects.filter(
        fecha_hora__gte=fecha_inicio,
        fecha_hora__lt=fecha_fin
    )

    hora_inicio = datetime(datetime.today().year, datetime.today().month, 1, 8, 0)
    hora_fin = datetime(datetime.today().year, datetime.today().month, 1, 18, 0)
    intervalo = timedelta(hours=2)
    horas_disponibles = []

    while hora_inicio < hora_fin:
        # Verifica si la hora está en las reservas existentes
        if not reservas_existentes.filter(fecha_hora=hora_inicio).exists():
            horas_disponibles.append(hora_inicio)
        hora_inicio += intervalo

    return horas_disponibles


