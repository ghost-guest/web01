
import xadmin
from xadmin import views
from .models import EmailVerifyRecord

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
class GlobalSettings(object):
    site_title = "暮雪后台管理系统"
    site_footer = "暮雪在线"
    menu_style = 'accordion'
class EmailVerifyRecordAdmin(object):
    list_display = ["code", "email", "send_type", "send_time"]
    list_filter = ["code", "email", "send_type", "send_time"]
    search_fields = ["code", "email", "send_type"]
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)