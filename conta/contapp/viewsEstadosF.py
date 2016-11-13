import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date, time, timedelta
from contapp.models import  empresa, tipCuenta, rubCuenta, cuenta, partida, movimiento,impArchivo
from contapp.service import  ImpCatalago, errores, CatalogoCuentas,FormImportacion,FormEmpresa
from django.views.generic import ListView,CreateView
# Create your views here.
UPLOAD_FOLDER = '/var/www'