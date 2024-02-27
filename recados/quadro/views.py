from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Recado

from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    try:
        ultima_data = datetime.fromtimestamp(request.session['ultima_data'])
    except KeyError:
        ultima_data = datetime.now()
        request.session['ultima_data'] = datetime.timestamp(ultima_data)
    quantidade_recados = Recado.objects.count()
    template = loader.get_template('quadro/index.html')
    context = {
        'ultima_data' : ultima_data,
        'quantidade_recados': quantidade_recados,
    }
    nova_data = datetime.now()
    request.session['ultima_data'] = datetime.timestamp(nova_data)
    return HttpResponse(template.render(context, request))