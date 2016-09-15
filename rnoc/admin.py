from django.contrib import admin

from models import Tram,DoiTac, Mll, TrangThai, DuAn,\
    UserProfile
from django.contrib.auth.models import Permission
from django.db.models.fields import CharField

class Tadmin(admin.ModelAdmin):
    search_fields = ['Site_Name_1','Site_ID_3G']
    
class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    #fields = ['name','codename']
class TramAdmin(admin.ModelAdmin):
    list_display=('Site_Name_1','Site_ID_3G','Ngay_Phat_Song_3G')
    search_fields = ('Site_Name_1','Site_ID_3G')
    list_filter = ('Cabinet','RNC')
    date_hierarchy = 'Ngay_Phat_Song_3G'
    ordering = ('Ngay_Phat_Song_3G','-Site_Name_1')
    filter_horizontal = ('du_an',)
    raw_id_fields = ('Cabinet',)
class UserProfileAdmin(admin.ModelAdmin):
    fields = [f.name for f in UserProfile._meta.fields]
    list_display = fields
    search_fields = fields
class MllAdmin(admin.ModelAdmin):
    fields = [f.name for f in Mll._meta.fields ]
    char_fields = [f.name for f in Mll._meta.fields if isinstance(f, CharField)]
    list_display = fields
    search_fields = char_fields

admin.site.register(Permission, PermissionAdmin)
admin.site.register(Tram,TramAdmin)
admin.site.register(DoiTac)
admin.site.register(Mll,MllAdmin)
admin.site.register(TrangThai)
admin.site.register(DuAn)
admin.site.register(UserProfile,UserProfileAdmin)
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered
app_models = apps.get_app_config('rnoc').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass