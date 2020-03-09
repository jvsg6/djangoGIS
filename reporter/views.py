from django.shortcuts import render, get_object_or_404
from .models import Accident
# Create your views here.

def accidentDetails(request, pk):
	accident = get_object_or_404(Accident, pk=pk)
	return render(request, 'reporter/accident.html', {'accident': accident})