from django.shortcuts import render
from django.http import HttpResponse
from . import gdrive_api_modif
# Create your views here.

def home(request):

    return render(request, "modify_values.html")

def modify_values_ftn(request):

    color = request.POST['color_html']
    reader = request.POST['reader_html']
    tag = request.POST['tag_html']
    area = request.POST['area_html']

    msg = gdrive_api_modif.update_values(color, reader, tag, area)

    return render(request, "modify_values.html", {'message': msg})