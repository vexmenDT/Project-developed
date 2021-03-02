from django import forms
from .models import Estados, Paises, Alumnos

class PaisF(forms.ModelForm):
    class Meta:
        model = Paises
        fields = '__all__'



class EstadosF(forms.ModelForm):
    class Meta:
        model = Estados
        fields = '__all__'


class AlumnosF(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estado'].queryset = Estados.objects.none()

        if 'pais' in self.data:
            try:
                pais_id = int(self.data.get('pais'))
                self.fields['estado'].queryset = Estados.objects.filter(pais_id=pais_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['estado'].queryset = self.instance.pais.estado_set.order_by('nombre')





