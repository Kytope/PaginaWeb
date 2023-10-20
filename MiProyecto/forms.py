from django import forms
from .models import Reserva  # Importa el modelo relacionado si es necesario

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva  # Asocia el formulario con tu modelo
        fields = ['fecha_reserva', 'fecha_hora']  # Especifica los campos a mostrar en el formulario
