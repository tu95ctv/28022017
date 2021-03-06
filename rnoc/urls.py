from django.conf.urls import patterns, url, include
from . import views
from django.conf import settings
from django.contrib import admin

# UNDERNEATH your urlpatterns definition, add the following two lines:
admin.autodiscover()
urlpatterns = patterns('',
        
        #################OMCKV2####################
        url(r'^omckv$', views.omckv2, name='index'),
        url(r'^omckv2/upload_excel_file/$', views.upload_excel_file, name='upload_file'),
        #url(r'^omckv2/tracnghiem/$', views.trac_nghiem, name='upload_file'),
        url(r'^omckv2/upload_bcn_excel/$', views.upload_bcn_excel, name='upload_file'),
        url(r'^omckv2/edit_history_search/$', views.edit_history_search, name='suggestion'),
        url(r'^omckv2/modelmanager/(?P<modelmanager_name>\w+)/(?P<entry_id>.*?)/$', views.modelmanager, name='suggestion'),
        url(r'^omckv2/$',  views.omckv2, name='omckv2'),
        #url(r'^omckv2/delete_mll/$',  views.delete_mll, name='tram_table'),
        url(r'^omckv2/autocomplete/$',  views.autocomplete, name='tram_table'),
        url(r'^omckv2/download_script_ntp/$',  views.download_script_ntp, name='tram_table'),
        url(r'^omckv2/init/$',  views.init, name='tram_table'),
        url(r'^omckv2/changepassword/$', views.password_change, name='password_change'),
        url(r'^omckv2/changepassword/done/$', views.password_change_done, name='password_change_done'),
        url(r'^accounts/', include('django.contrib.auth.urls')),
        ##########CHUNG
        url(r'^login/$',views.user_login,name="user_login"),
        url(r'^logout/$',views.user_logout,name="user_logout"),
        url(r'^omckv2/registers/$', views.register, name='register'), # ADD NEW PATTERN! 
        )
if settings.DEBUG:
    urlpatterns += patterns( 
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
 
    
    
    