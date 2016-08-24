from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Wizard


class WizardSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = Wizard
        fields = ['pk','first_name','last_name','company_name']