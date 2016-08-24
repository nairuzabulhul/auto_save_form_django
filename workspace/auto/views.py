from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from django.core import serializers
from django.http import HttpResponse
from django.http.request import QueryDict
import ast
from auto.models import Wizard
from auto.serializers import WizardSerializer


def wizard_view(request):

    return render(request, "auto/index.html", {})


# Create your views here.
@api_view(['GET', 'POST'])
def wizard_api_view(request):

    try:
        wizard_id = int(request.data.get('id'))
    except ValueError:
        wizard_id = None

    try:
        wizard = Wizard.objects.get(id=wizard_id)
    except Wizard.DoesNotExist:
        wizard = None

    if wizard is None:
        wizard = Wizard.objects.create(
            data=request.data
            # first_name= request.data['first_name'],
            # last_name = request.data['last_name'],
            # company_name = request.data['company_name']
        )
    else:
        wizard.data = request.data
        # wizard.first_name = request.data['first_name']
        # wizard.last_name = request.data['last_name']
        # wizard.company_name = request.data['company_name']
        wizard.save()

    wizardJSON = serializers.serialize('json', [wizard], ensure_ascii=False)
            
    print wizardJSON, type(wizardJSON)
            
    return Response(wizardJSON)