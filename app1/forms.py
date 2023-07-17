from django import forms
from app1.models import *

class Agent_model_form(forms.ModelForm):
    class Meta:
        model = Agents
        fields= '__all__'

class Cust_model_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'