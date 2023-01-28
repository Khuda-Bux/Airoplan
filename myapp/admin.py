from django.contrib import admin
from .models import plan
# Register your models here.
@admin.register(plan)
class PlanAdmin(admin.ModelAdmin):
    list_display=['id','departing_from','final_destination','no','date',
                  'name_airline','flight_number','date2','delayed','hourse1',
                  'days','caused']