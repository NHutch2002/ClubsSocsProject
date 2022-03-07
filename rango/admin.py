from django.contrib import admin
from rango.models import Society, Event, UserProfile
# Register your models here.

class SocietyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('societyName',)}
    
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('eventName',)}

admin.site.register(Society, SocietyAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(UserProfile)