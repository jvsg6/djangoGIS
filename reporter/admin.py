from django.contrib import admin
from .models import Accident
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class AccidentAdmin(LeafletGeoAdmin):
	list_display = ('name', 'location')

admin.site.register(Accident, AccidentAdmin)