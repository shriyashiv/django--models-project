from django.forms import ModelForm
from .models import Passenger_details
class Passenger_detailsForm(ModelForm):
    class Meta:
        model=Passenger_details
        fields='__all__'




