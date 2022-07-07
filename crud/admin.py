from django.contrib import admin

from .models import Records
from .models import Cities
from .models import Equipment_spots
from .models import Equipment_models
from .models import Month_avg
from .models import Year_avg
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ExportActionMixin

class RecordsExcel(ExportActionMixin, admin.ModelAdmin):
    list_display = ('date', 'temperature', 'humidity', 'windspeed')

class HistoryExportAdmin(SimpleHistoryAdmin, RecordsExcel):
    pass

admin.site.register(Records, HistoryExportAdmin)
admin.site.register(Cities, SimpleHistoryAdmin)
admin.site.register(Equipment_spots, SimpleHistoryAdmin)
admin.site.register(Equipment_models, SimpleHistoryAdmin)
admin.site.register(Month_avg, SimpleHistoryAdmin)
admin.site.register(Year_avg, SimpleHistoryAdmin)
# Register your models here.
