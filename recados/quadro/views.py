from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Recado
def index(request):
    quantidade_recados = Recado.objects.count()
    template = loader.get_template('quadro/index.html')
    context = {
    'quantidade_recados': quantidade_recados,
    }
    return HttpResponse(template.render(context, request))