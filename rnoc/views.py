# -*- coding: utf-8 -*-

#CK editor day 24/04/2016
import sys  
import os
from django.utils.datastructures import MultiValueDictKeyError
from unidecode import unidecode
reload(sys)  
sys.setdefaultencoding('utf-8')
from django.db.models import F,Sum,IntegerField,FloatField
from django.db.models import Value as V

from models import FaultLibrary, EditHistory
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.template import RequestContext
from django.shortcuts import render_to_response, render, resolve_url
from models import Tram, Mll, Lenh,SearchHistory, H_Field, DoiTac
from forms import  TramForm, \
    TramTable, MllForm, MllTable, LenhTable, LenhForm, SearchHistoryTable,\
    ModelManagerForm, UserProfileForm_re
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Q

import collections
from django.contrib.auth.models import User
from rnoc.models import ThaoTacLienQuan, Tinh, BCNOSS, ThietBi,\
    BTSType
from django.db.models.fields import DateField, AutoField
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
#from django.contrib.sites.models import get_current_site
from LearnDriving.settings import TIME_ZONE
from django.db.models.expressions import When, Case, ExpressionWrapper
from django.db.models.aggregates import  Avg
from django.db.models.aggregates import Count
from decimal import Decimal
import operator
from itertools import chain
from toold4 import  recognize_fieldname_of_query, luu_doi_tac_toold4
from xu_ly_db_3g import tao_script, import_database_4_cai_new, init_rnoc,\
    export_excel_bcn, thongkebcn_generator
tao_script
import xlrd
import re
from exceptions import Exception
from sendmail import send_email
from django_tables2_reports.config import RequestConfigReport as RequestConfig


from django.db.models import CharField,DateTimeField
from django.utils import   timezone
try:
    from django.utils import simplejson
except:
    import json as simplejson
from rnoc.forms import UserForm, UserProfileForm,\
    VERBOSE_CLASSNAME, BCNOSSForm, BCNOSSTable, D4_DATETIME_FORMAT
import models
import forms#cai nay quan trong khong duoc xoa
ICONTAINS_OR_IREGEX =  'iregex'  
MYD4_LOOKED_FIELD = collections.OrderedDict((("Site_ID_2G",'2G'),
        ("Site_ID_3G",'3G'),
        ("eNodeB_Name","4G"),
        ("Site_Name_1", "SN1"),
        ("Site_Name_2", 'SN2')))
SHORT_DATETIME_FORMAT = "Y-m-d H:i"
################CHUNG######################
def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm_re(data=request.POST)

        # If the two forms are valid...
        user_form.is_valid() 
        #print '@@#$#',user_form.cleaned_data['email']
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
    
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
    
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
    
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.

            profile.save()
    
            registered = True

        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'drivingtest/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/omckv2/')
            else:
                notification = u'<h4 style="color:red">Username bị khóa</h4>'
                #return HttpResponse("Your Rango account is disabled.")
        else:
            #return HttpResponse("Invalid login details supplied.")
            notification = u'<h4 style="color:red">Username hoặc password không đúng, hoặc user không tồn tại</h4>'
            form = AuthenticationForm(request.GET)
    else:
        notification = u'<h4 style="color:green">Mời bạn login</h4>'
        form = AuthenticationForm(request)
    form.notification = notification
    return render_to_response('drivingtest/login_ok.html', {'form':form}, context)    
'''
@sensitive_post_parameters()
@csrf_protect
@never_cache
def login2(request, template_name='drivingtest/registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
        else:
            print 'form login not valid',form.errors 
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)
'''

    
    
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/omckv2/')

@sensitive_post_parameters()
@csrf_protect
@login_required
def password_change(request,
                    template_name='drivingtest/registration/password_change_form_ok.html',
                    post_change_redirect=None,
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    if post_change_redirect is None:
        post_change_redirect = reverse('rnoc.views.password_change_done')
        #print '@@22type of post_change_redirect',type(post_change_redirect),post_change_redirect
    else:
        post_change_redirect = resolve_url(post_change_redirect)
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            extra_context ={'success_change_form':u'Bạn đã đổi pass thành công'}
            return HttpResponseRedirect(post_change_redirect)
    else:
        form = password_change_form(user=request.user)
    context = {
        'form': form,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


@login_required
def password_change_done(request,
                         template_name='drivingtest/registration/password_change_done_ok.html',
                         current_app=None, extra_context=None):
    context = {}
    #print '##########password_change_done'
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)



#####OMC###############
SELECT_EXTRAS = {'day': "date( gio_mat  AT TIME ZONE '{0}')",}

def annotation_for_thongkengaythang (bcns_objects,is_groups,is_include_code_8 = False):
    print 'is_groupsis_groupsis_groups@@@@',is_groups
    tk_qs  = bcns_objects
    for annota in is_groups:
        if annota == 'day':
            tk_qs  = tk_qs.extra(select={'day': "date( gio_mat  AT TIME ZONE '{0}')".format(TIME_ZONE)})  
        elif annota == 'month':
            is_groups.append('year')
            tk_qs  = tk_qs.extra(select={'month': "extract( month from date( gio_mat  AT TIME ZONE '{0}') )".format(TIME_ZONE),\
                                         'year': "extract( year from date( gio_mat  AT TIME ZONE '{0}') )".format(TIME_ZONE)})
        elif annota == 'year':
            tk_qs  = tk_qs.extra(select={'year': "extract( year from date( gio_mat  AT TIME ZONE '{0}') )".format(TIME_ZONE)})

    def chon_code_loi_tong_thoi_gian_expression(code_loi):
        if code_loi ==8:
            return Case(When(Q(code_loi=8)|Q(code_loi=7)|Q(code_loi=4), then=F('tong_thoi_gian')))
        return Case(When(code_loi=code_loi, then=F('tong_thoi_gian')))
    def sum_thoi_gian_theo_code_loi_expression(code_loi):
        if code_loi == 8:
            return  Sum( Case(When(Q(code_loi=8)|Q(code_loi=7)|Q(code_loi=4), then=F('tong_thoi_gian')),output_field=IntegerField()))
            #code_loi = Q(code_loi=8)|Q(code_loi=7)|Q(code_loi=4)
        return  Sum( Case(When(code_loi=code_loi, then=F('tong_thoi_gian')),output_field=IntegerField()))
    def phan_tram_thoi_gian_theo_code_loi_expression(code_loi):
        return  ExpressionWrapper(sum_thoi_gian_theo_code_loi_expression(code_loi)* Decimal('100.0')/sum_tong_Mll_expression,output_field=FloatField())
    sum_mat_dien_expression =  Sum( Case(When(code_loi=1, then=F('tong_thoi_gian')),output_field=IntegerField()))
    sum_tong_Mll_expression = Sum('tong_thoi_gian')
    #phan_tram_mat_dien_expression = ExpressionWrapper(sum_mat_dien_expression* Decimal('1.0')/sum_tong_Mll_expression,output_field=FloatField())
    #phan_tram_mat_dien_expression = ExpressionWrapper( (F('sum_mat_dien') * Decimal('1.0') / F('tong_thoi_gian') ),output_field=FloatField())
    def sum_filter_code_loi_expression(code_loi = None,count_or_tong_thoi_gian=None):
        return Sum( Case(When(code_loi=code_loi, then=count_or_tong_thoi_gian),output_field=IntegerField()
                         )
                    )
    LISTS_TBINH = ['count_tong_mll','sum_tong_mll','tb_1_lan_mll','count_mat_dien','sum_mat_dien','tb_1_lan_mat_dien','phan_tram_mat_dien',\
             'count_truyen_dan','sum_truyen_dan',
             'phan_tram_truyen_dan','tb_1_lan_truyen_dan','count_thiet_bi','sum_thiet_bi',
             'phan_tram_thiet_bi','tb_1_lan_thiet_bi',
             ]     
    tk_qs  = tk_qs.values(*is_groups).\
    annotate(count_tong_mll = Count('id')).\
    annotate(sum_tong_mll =sum_tong_Mll_expression ).\
    annotate(tb_1_lan_mll = Avg('tong_thoi_gian')).\
    annotate(count_mat_dien = sum_filter_code_loi_expression(code_loi = 1,count_or_tong_thoi_gian = 1)
             ).\
    annotate(sum_mat_dien =sum_mat_dien_expression).\
    annotate(tb_1_lan_mat_dien = Avg( Case(When(code_loi=1, then=F('tong_thoi_gian')),output_field=IntegerField()))).\
    annotate(phan_tram_mat_dien = phan_tram_thoi_gian_theo_code_loi_expression(1)).\
    annotate(count_truyen_dan =sum_filter_code_loi_expression(code_loi = 5,count_or_tong_thoi_gian = 1) ).\
    annotate(sum_truyen_dan = Sum( Case(When(code_loi=5, then=F('tong_thoi_gian')),output_field=IntegerField()))).\
    annotate(tb_1_lan_truyen_dan = Avg( Case(When(code_loi=5, then=F('tong_thoi_gian')),output_field=IntegerField()))).\
    annotate(phan_tram_truyen_dan = phan_tram_thoi_gian_theo_code_loi_expression(5)).\
    annotate(count_thiet_bi = Sum( Case(When(code_loi=3, then=1),output_field=IntegerField()))).\
    annotate(sum_thiet_bi = Sum( Case(When(code_loi=3, then=F('tong_thoi_gian')),output_field=IntegerField()))).\
    annotate(phan_tram_thiet_bi = phan_tram_thoi_gian_theo_code_loi_expression(3)).\
    annotate(tb_1_lan_thiet_bi = Avg( Case(When(code_loi=3, then=F('tong_thoi_gian')),output_field=IntegerField())))
    if  is_include_code_8:
        tk_qs = tk_qs.annotate(count_dau_chuyen = Sum( Case(When(Q(code_loi=8)|Q(code_loi=7)|Q(code_loi=4), then=1),output_field=IntegerField()))).\
        annotate(sum_dau_chuyen = Sum( Case(When(Q(code_loi=8)|Q(code_loi=7)|Q(code_loi=4), then=F('tong_thoi_gian')),output_field=IntegerField()))).\
        annotate(phan_tram_dau_chuyen = phan_tram_thoi_gian_theo_code_loi_expression(8)).\
        annotate(tb_1_lan_dau_chuyen = Avg(Case(When(Q(code_loi=8)|Q(code_loi=7)|Q(code_loi=4), then=F('tong_thoi_gian')),output_field=IntegerField())))
        LISTS_TBINH.extend(['count_dau_chuyen','sum_dau_chuyen','phan_tram_dau_chuyen','tb_1_lan_dau_chuyen'])
    #aggr =  tk_qs.aggregate(tb_count_mat_dien = Avg( 'count_mat_dien'))
    
    if ('tinh' in is_groups and 'BSC_or_RNC' not in is_groups) or ('BSC_or_RNC' in is_groups and 'tinh' not in is_groups) :
        LISTS_TBINH.extend(['tong_mll_tren_tram','mat_dien_tren_tram','truyen_dan_tren_tram','thiet_bi_tren_tram'])
        instance_2g =  BTSType.objects.get(Name = '2G')
        instance_3g =  BTSType.objects.get(Name = '3G')
        if 'tinh' in is_groups:
            if 'BTS_Type' not in is_groups:
                so_luong_tram_expression = F('tinh__tong_so_tram')
                tk_qs = tk_qs.annotate(so_luong_tram_tinh_or_bsc_rnc = Avg('tinh__tong_so_tram'))
            else:
                so_luong_tram_expression = Case(
                           When(BTS_Type=instance_2g,then = F('tinh__so_luong_tram_2G')),\
                           When(BTS_Type=instance_3g,then = F('tinh__so_luong_tram_3G')),\
                           output_field=FloatField()\
                           )
                tk_qs = tk_qs.annotate(so_luong_tram_tinh_or_bsc_rnc =Avg(so_luong_tram_expression))
        elif 'BSC_or_RNC' in is_groups:
            tk_qs = tk_qs.annotate(so_luong_tram_tinh_or_bsc_rnc = Avg('BSC_or_RNC__so_luong_tram'))
            so_luong_tram_expression = F('BSC_or_RNC__so_luong_tram')
        
        mll_tren_1_tram_expression = ExpressionWrapper( (F('tong_thoi_gian') * Decimal('1.0') / so_luong_tram_expression ),output_field=FloatField())
        tk_qs = tk_qs.annotate(tong_mll_tren_tram = Sum(mll_tren_1_tram_expression,output_field=CharField()))
        mll_tren_1_tram_expression_theo_code_loi = ExpressionWrapper( (chon_code_loi_tong_thoi_gian_expression(1) * Decimal('1.0') / so_luong_tram_expression ),output_field=FloatField())
        tk_qs = tk_qs.annotate(mat_dien_tren_tram = Sum(mll_tren_1_tram_expression_theo_code_loi,output_field=CharField()))
        
        mll_tren_1_tram_expression_theo_code_loi = ExpressionWrapper( (chon_code_loi_tong_thoi_gian_expression(5) * Decimal('1.0') / so_luong_tram_expression ),output_field=FloatField())
        tk_qs = tk_qs.annotate(truyen_dan_tren_tram = Sum(mll_tren_1_tram_expression_theo_code_loi,output_field=CharField()))
        
        mll_tren_1_tram_expression_theo_code_loi = ExpressionWrapper( (chon_code_loi_tong_thoi_gian_expression(3) * Decimal('1.0') / so_luong_tram_expression ),output_field=FloatField())
        tk_qs = tk_qs.annotate(thiet_bi_tren_tram = Sum(mll_tren_1_tram_expression_theo_code_loi,output_field=CharField()))
       
        if  is_include_code_8:
            LISTS_TBINH.extend(['dau_chuyen_tren_tram'])
            mll_tren_1_tram_expression_theo_code_loi = ExpressionWrapper( (chon_code_loi_tong_thoi_gian_expression(8) * Decimal('1.0') / so_luong_tram_expression ),output_field=FloatField())
            tk_qs = tk_qs.annotate(dau_chuyen_tren_tram = Sum(mll_tren_1_tram_expression_theo_code_loi,output_field=CharField()))
           
       
        '''
        tk_qs = tk_qs.annotate(tong_mll_tren_tram =  Concat(V('{{'),Sum(mll_tren_1_tram_expression,output_field=CharField()
                                                                ), V(u'|floatformat:2 }} phút trên 1 trạm '),output_field=CharField()
                                                            )
                               )
        '''
        #cam xoa o tren
    #for aggregate
    DISTS_TB = {}
    for x in LISTS_TBINH:
        DISTS_TB[('tb_'+x)] = Avg(x)
    aggr =  tk_qs.aggregate(**DISTS_TB)
    return tk_qs,aggr
        
@login_required
def init(request):
    init_rnoc()
    return HttpResponse('ok')
so_luong_truy_suat = 0
@login_required
def omckv2(request):
    global so_luong_truy_suat
    so_luong_truy_suat +=1
    print 'so_luong_truy_suat',so_luong_truy_suat
    tramform = TramForm()
    mllform = MllForm()
    commandform = LenhForm()
    mlltable = MllTable(Mll.objects.all().order_by('-id'))
    RequestConfig(request, paginate={"per_page": 15}).configure(mlltable) 
    lenhtable = LenhTable(Lenh.objects.all().order_by('-id'))
    RequestConfig(request, paginate={"per_page": 15}).configure(lenhtable) 
    tramtable = TramTable(Tram.objects.all().order_by('-ngay_gio_tao'), )
    RequestConfig(request, paginate={"per_page": 10}).configure(tramtable)
    user = request.user
    profile_instance = user.userprofile
    userprofileform = UserProfileForm(instance = profile_instance,khong_show_2_nut_cancel_va_loc=True )
    BCNOSS_form = BCNOSSForm()
    BCNOSS_table = BCNOSSTable(BCNOSS.objects.all().order_by('-id'))
    RequestConfig(request, paginate={"per_page": 15}).configure(BCNOSS_table) 
    history_search_table = SearchHistoryTable(SearchHistory.objects.all().order_by('-search_datetime'), )
    RequestConfig(request, paginate={"per_page": 10}).configure(history_search_table)
    model_manager_form = ModelManagerForm()
    return render(request, 'drivingtest/omckv2.html',{'userprofileform':userprofileform,\
                                                      'BCNOSS_form':BCNOSS_form,'BCNOSS_table':BCNOSS_table,\
                                                      'tramtable':tramtable,'tramform':tramform,'mllform':mllform,\
                                                      'commandform':commandform,\
                                                      'mlltable':mlltable,'lenhtable':lenhtable,
                                                      'history_search_table':history_search_table,
                                                      'model_manager_form':model_manager_form})

#URL  =  $.get('/omckv2/search_history/'
# DELETE SOMETHING ON SURFACE AND C   
    
class FilterToGenerateQ():
    No_AUTO_FILTER_FIELDS=[]
    def __init__(self,request,FormClass,ModelClass,form_cleaned_data):
        self.form_cleaned_data = form_cleaned_data
        self.EXCLUDE_FIELDS = getattr(FormClass.Meta,'exclude', [])
        #self.No_AUTO_FILTER_FIELDS = No_AUTO_FILTER_FIELDS
        self.ModelClass = ModelClass
        self.request = request
    def generateQgroup(self):
        qgroup=Q()
        for f in self.ModelClass._meta.fields :
            try:
                if not self.request.GET[f.name] or self.form_cleaned_data[f.name]==None  or  (f.name  in self.EXCLUDE_FIELDS) or  (f.name  in self.No_AUTO_FILTER_FIELDS)  :
                    continue
            except :#MultiValueDictKeyError
                continue
            functionname = 'generate_qobject_for_exit_model_field_'+f.name
            no_auto_function = getattr(self, functionname,None)
            if no_auto_function:
                g_no_auto = no_auto_function(f.name)
                qgroup &=g_no_auto
            elif isinstance(f,CharField):
                if self.form_cleaned_data[f.name]==u'*':
                    qgroup &= ~Q(**{'%s__isnull'%f.name:True}) & ~Q(**{'%s__exact'%f.name:''})
                elif self.form_cleaned_data[f.name]==u'!':
                    qgroup &= Q(**{'%s__isnull'%f.name:True}) | Q(**{'%s__exact'%f.name:''})
                else:
                    qgroup &=Q(**{'%s__iregex'%(f.name):self.form_cleaned_data[f.name]})
                    print {'%s__iregex'%(f.name):self.form_cleaned_data[f.name]}
            elif isinstance(f,DateTimeField) or  isinstance(f,DateField) or  isinstance(f,AutoField):
                pass
            else:
                qgroup &=Q(**{'%s'%f.name: self.form_cleaned_data[f.name]})
        #MANYTOMANYFIELDS
        for f in self.ModelClass._meta.many_to_many :
            try:
                if not self.request.GET[f.name]:
                    continue
            except :#MultiValueDictKeyError
                continue
            if (f.name not in self.EXCLUDE_FIELDS) and (f.name not in self.No_AUTO_FILTER_FIELDS):
                qgroup &=Q(**{'%s__in'%f.name:self.form_cleaned_data[f.name]})
        
        q_out_field = getattr(self,'generate_qobject_for_NOT_exit_model_fields',None)
        if q_out_field:
            q_outer_field = self.generate_qobject_for_NOT_exit_model_fields()
            qgroup &= q_outer_field       
        return qgroup     
class FilterToGenerateQ_ForBCNOSSForm(FilterToGenerateQ):
    def generate_qobject_for_exit_model_field_gio_mat(self,fname):
            d = self.form_cleaned_data[fname] + timedelta(minutes=1)
            q_gio_mat = Q(gio_mat__lte=d)
            return q_gio_mat
    def generate_qobject_for_NOT_exit_model_fields(self):
        qgroup=Q()
        if self.form_cleaned_data['gio_mat_lon_hon']:
            d = self.form_cleaned_data['gio_mat_lon_hon']
            q = Q(gio_mat__gte=d)
            qgroup = qgroup & q
        
        return qgroup
class FilterToGenerateQ_ForTram(FilterToGenerateQ):
    
    def generate_qobject_for_exit_model_field_Ngay_Phat_Song_3G(self,fname):
            d = self.form_cleaned_data[fname]
            q = Q(Ngay_Phat_Song_3G__lte=d)
            return q
    def generate_qobject_for_exit_model_field_Ngay_Phat_Song_2G(self,fname):
            d = self.form_cleaned_data[fname]
            q = Q(Ngay_Phat_Song_2G__lte=d)
            return q  
    def generate_qobject_for_NOT_exit_model_fields(self):
        qgroup=Q()
        if self.form_cleaned_data['Ngay_Phat_Song_3G_lon_hon']:
            d = self.form_cleaned_data['Ngay_Phat_Song_3G_lon_hon']
            q = Q(Ngay_Phat_Song_3G__gte=d)
            qgroup = qgroup & q
        if self.form_cleaned_data['Ngay_Phat_Song_2G_lon_hon']:
            d = self.form_cleaned_data['Ngay_Phat_Song_2G_lon_hon']
            q = Q(Ngay_Phat_Song_2G__gte=d)
            qgroup = qgroup & q
        return qgroup
class FilterToGenerateQ_ForMLL(FilterToGenerateQ):
    
    def generate_qobject_for_exit_model_field_gio_mat(self,fname):
            d = self.form_cleaned_data[fname] + timedelta(minutes=1)
            q_gio_mat = Q(gio_mat__lte=d)
            return q_gio_mat
    
    def generate_qobject_for_NOT_exit_model_fields(self):
        qgroup=Q()
        if self.request.GET['comment']:
            q_across = Q(comments__comment__icontains=self.request.GET['comment'])
            qgroup = qgroup&q_across
        if self.request.GET['specific_problem_m2m']:
            value = re.sub('\*\*$','',self.request.GET['specific_problem_m2m'])
            q_across_fault = Q(specific_problems__fault__Name__icontains=value)
            q_across_object_name = Q(specific_problems__object_name__icontains=value)
            q_specific_problem_m2m = q_across_fault | q_across_object_name
            qgroup = qgroup & q_specific_problem_m2m
        #for m2m

        if  self.form_cleaned_data['thao_tac_lien_quan']: 
            #print '@@@@@@@@@@@@@@@@@zz',self.form_cleaned_data['thao_tac_lien_quan']
            q_across_thaotac = Q(comments__thao_tac_lien_quan__in=self.form_cleaned_data['thao_tac_lien_quan'])
            qgroup = qgroup & q_across_thaotac
           
        if self.form_cleaned_data['doi_tac']: # input text la 1 doi tac hoan chinh nhu la a-b-number
            q_across_doi_tac = Q(comments__doi_tac=self.form_cleaned_data['doi_tac'])
            qgroup = qgroup & q_across_doi_tac
        elif self.request.GET['doi_tac']: # input text la form
            value = self.request.GET['doi_tac']
            fieldnames = [f.name for f in DoiTac._meta.fields if isinstance(f, CharField)]
            q_across_doi_tac = reduce(operator.or_, (Q(**{"comments__doi_tac__%s__icontains" % fieldname:value }) for fieldname in fieldnames ))
            qgroup = qgroup & q_across_doi_tac
        if self.form_cleaned_data['gio_mat_lon_hon']:
            d = self.form_cleaned_data['gio_mat_lon_hon']
            q = Q(gio_mat__gte=d)
            qgroup = qgroup & q
        
        return qgroup
    

# delete surface branch
def show_string_avoid_none (value,string_pattern = '{0}',none_string_presentation = ''):
    if value:
        return string_pattern.format(str(value))
    else:
        return none_string_presentation
'''
def update_trang_thai_cho_mll(mll_instance):
    last_comment_instance = mll_instance.comments.latest('id')
    mll_instance.trang_thai = last_comment_instance.trang_thai
    mll_instance.save()
'''                                               
#MODAL_style_title_dict_for_form = {'CommentForm':('')}
def update_edit_history(ModelOfForm_Class_name,instance,request):
    if (EditHistory.objects.filter(modal_name=ModelOfForm_Class_name).count() > 10000 ):
            oldest_instance= EditHistory.objects.all().order_by('edit_datetime')[0]
            oldest_instance.ly_do_sua = request.GET['edit_reason']
            oldest_instance.search_datetime = datetime.now()
            oldest_instance.edited_object_id = instance.id
            oldest_instance.modal_name = ModelOfForm_Class_name
            oldest_instance.thanh_vien =request.user
            oldest_instance.save()
    else:
        instance_edit_history = EditHistory(modal_name = ModelOfForm_Class_name, thanh_vien =request.user,ly_do_sua = request.GET['edit_reason'],edit_datetime = datetime.now(),edited_object_id = instance.id )
        instance_edit_history.save()
def loc_query_for_table_notification(form_for_loc,request):
    count=0
    loc_query=''
    for k,f in form_for_loc.fields.items():
        try:
            v = request.GET[k]
        except:
            continue
        if v:
            try:
                label = f.label +''
            except TypeError:
                label = k
            count +=1
            if count==1:
                loc_query = label + '=' + v
            else:
                loc_query = loc_query + '&'+label + '=' + v
    return  loc_query
def modelmanager(request,modelmanager_name,entry_id):
    #tham so loc nam trong GET, ngoai tham so loc ra thi con tham so which_table_or _form tham so modal hay normal form, neu co nhung tham so nhu tramid
    #hay query_main_search_by_button thi chac chan khong co tham so loc
    # khi loc ma method = Request thi parameter GET  gui di chi toan la fiedl khong co add extra parameter cua table
    # chi co add them extra parameter cua table khi post Edit
    #khi co tramid thi khong co loc
    #khi co tram id thi khong co query_main_search_by_button
    #form_name = modelmanager
    status_code = 200
    url = '/omckv2/modelmanager/'+ modelmanager_name +'/'+entry_id+'/'
    form_table_template =request.GET.get('form-table-template')
    is_form = True if  (request.GET.get('is_form',None) =='true')else False
    is_table = True if  (request.GET.get('is_table',None) =='true')else False
    is_download_table = True if 'downloadtable' in request.GET else False
    if is_download_table:
        is_form = False
    
    dict_render ={}
    form = None
    table2 = None
    need_valid=False
    need_save_form  =False
    data=None
    initial=None
    instance=None
    form_notification = None
    #table_notification = u'<span class="table_notification"> Danh sách được hiển thị ở table bên dưới  </span>'
    loc = True if 'loc' in request.GET else False
    loc_pass_agrument=False
    force_allow_edit = False
    #khong_show_2_nut_cancel_va_loc = False
    table_name = request.GET.get('table_name') if request.method =='POST' else None
    khong_show_2_nut_cancel_va_loc = request.GET.get('khong_show_2_nut_cancel_va_loc',None)
    if khong_show_2_nut_cancel_va_loc ==None:
        khong_show_2_nut_cancel_va_loc = True if table_name else False
    else:
        khong_show_2_nut_cancel_va_loc = True
    next_continue_handle_form = True
    #FORM HANDLE
    #if which_form_or_table!="table only" or loc or (is_download_table and loc): #get Form Class
    if is_form : # or loc or (is_download_table and loc)
        form_name= modelmanager_name
        FormClass = eval('forms.' + form_name)#repeat same if loc
        ModelOfForm_Class_name = re.sub('Form$','',form_name,1)
        
        if form_name =='NhanTinUngCuuForm':# only form not model form
            mll_instance = Mll.objects.get(id = request.GET['selected_instance_mll'])
            tram_2g_or_3g = re.search('_([2,3,4]G)_',mll_instance.object)
            if tram_2g_or_3g :
                mll_instance_object = mll_instance.object[7:]  
                tram_2g_or_3g_text = tram_2g_or_3g.group(1)
            else:
                mll_instance_object = mll_instance.object
                tram_2g_or_3g_text=''
            
            if mll_instance.site_name not in mll_instance_object:
                mll_instance_object +=' (' + show_string_avoid_none(mll_instance.site_name,'{0}') + ')'
            if tram_2g_or_3g_text =='3G':
                tram_2g_or_3g_text = 'Node B'
            elif tram_2g_or_3g_text:
                tram_2g_or_3g_text = 'Tram ' + tram_2g_or_3g_text
            else:
                tram_2g_or_3g_text = ''
            try:
                thietbi = show_string_avoid_none(unidecode(mll_instance.thiet_bi.Name),'. Thiet bi: {0}.') 
            except AttributeError: #Nonetype
                thietbi = ''
            noi_dung_tin_nhan = 'Bao ung cuu: ' + tram_2g_or_3g_text + ' ' + mll_instance_object + \
            show_string_avoid_none(unidecode(mll_instance.su_co.Name), '. Nguyen nhan: {0}') + \
            thietbi
            
            matinh_in_sitename = mll_instance.site_name[-3:]
            try:
                dia_ban = Tinh.objects.get(ma_tinh = matinh_in_sitename).dia_ban.ky_hieu
            except Tinh.DoesNotExist:
                dia_ban =''
            group = (u'NET2_UC_' + dia_ban) if dia_ban else ''
            form = FormClass(initial = {'noi_dung_tin_nhan':noi_dung_tin_nhan,'group':group})
            form.modal_title_style = 'background-color:#337ab7'
            form.modal_prefix_title  = 'Nội Dung Nhắn Tin'
            form_notification = u'<span class="form-notification text-primary">Nhấn nút copy, sẽ copy nội dung tn vào clipboard</span>'
            dict_render = {'form':form,'form_notification':form_notification}
        else:
            
            #print 'request.POST',request.POST
            if request.method=='POST':
                need_valid =True
                need_save_form=True
                data = request.POST
            elif request.method=='GET':
                if loc:
                    #print 'request.GET',request.GET
                    need_valid =True
                    data = request.GET
                    loc_pass_agrument = True #tham so nay de loai bo loi required khi valid form
                else:
                    if entry_id=='new':
                        form_notification = u'<span class="form-notification text-primary">Form trống để tạo instance <span class="name-class-notification">%s</span> mới </span>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name])
                    else:
                        form_notification = u'<span class="form-notification text-warning"> Đang hiển thị form của Đối tượng <span class="name-class-notification">%s</span> có ID là %s</span>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name],entry_id)
                        if 'force_allow_edit' in request.GET:
                            force_allow_edit=True # chuc nang cua is_allow_edit la de display nut edit hay khong
            ModelOfForm_Class = FormClass.Meta.model # repeat same if loc
            
            if entry_id !="new":# check 1 so truong hop tra ngay ve ket qua status_code=403(forbid)
                try:
                    int(entry_id)
                    instance = ModelOfForm_Class.objects.get(id = entry_id)
                except ValueError:#not interger, tuc la 1 chuoi
                    #if ModelOfForm_Class_name =='Tram':
                    if ModelOfForm_Class_name =='Tram':
                        karg = {'Site_Name_1':entry_id}
                    else:
                        if ModelOfForm_Class_name == "ThaoTacLienQuan":
                            entry_ids = entry_id.split(',')
                            entry_ids.reverse()
                            for x in entry_ids:
                                x = x.rstrip().lstrip()
                                if x =='':
                                    continue
                                else:
                                    entry_id = x
                                    break
                            karg = {'Name' : entry_id}  
                        elif ModelOfForm_Class_name == "ThietBi":
                            if '*' not in entry_id:
                                thietbi_name = entry_id
                                bts_type = None
                            else:
                                gach_index = entry_id.find('*')
                                thietbi_name = entry_id[:gach_index].lstrip().rstrip()
                                bts_type_name = entry_id[gach_index+1:].lstrip().rstrip()
                                if bts_type_name:
                                    try:
                                        bts_type = BTSType.objects.get(Name =bts_type_name )
                                    except:
                                        bts_type = None
                                else:
                                    bts_type = None
                            karg = {'Name':thietbi_name}
                            if bts_type:
                                karg.update({'bts_type':bts_type})
                        else:
                            karg = {'Name':entry_id}          
                    try:
                        #entry_id = urllib.unquote(entry_id).decode('utf8') 
                        instance = ModelOfForm_Class.objects.filter(**karg)[0]
                    except IndexError:
                        form_notification = u'<span class="form-notification text-danger">Không tìm thấy yêu cầu get instance của bạn </span>'
                        dict_render = {'form':None,'form_notification':form_notification}
                        status_code = 200
                        next_continue_handle_form = False
                if request.method=="POST":# hoac la need_save_form
                    print instance.id
                    if 'is_delete' in request.POST and (instance.nguoi_tao != request.user or request.user.is_superuser) :
                        dict_render.update({'info_for_alert_box':u'Bạn không có quyền xóa instance MLL or Comment của người khác'})
                        status_code = 403
                    elif  'is_delete' in request.POST:#instance.nguoi_tao == request.user
                        instance = ModelOfForm_Class.objects.get(id = entry_id)
                        delta = (timezone.now() - instance.ngay_gio_tao).seconds/60
                        set_allowed_delta_time = 12
                        if delta <set_allowed_delta_time:
                            instance.delete()
                            form_notification = u'<span class="form-notification text-danger">Đã xóa comment này, delta %s</span>'%str(delta)
                            dict_render = {'form':None,'form_notification':form_notification}
                            status_code = 200
                            next_continue_handle_form = False
                        else:
                            dict_render.update({'info_for_alert_box':\
                                                u'Hết thời gian để xóa instance nay vi no đã tạo được {0} giây, trong khi bạn chỉ được xóa trong vòng {1}\
                                                '.format(str(delta),str(set_allowed_delta_time))})
                            status_code = 403
                    elif form_name=="CommentForm" and instance.nguoi_tao != request.user :
                        dict_render.update({'info_for_alert_box':u'Bạn không có quyền thay đổi comment của người khác'})
                        status_code = 403
            if next_continue_handle_form and status_code ==200:
                form = FormClass(data=data,instance = instance,initial=initial,loc =loc_pass_agrument,form_table_template=form_table_template,force_allow_edit=force_allow_edit,request = request,\
                                 khong_show_2_nut_cancel_va_loc = khong_show_2_nut_cancel_va_loc)
                if need_valid:
                    is_form_valid = form.is_valid()
                    if not is_form_valid :
                        form_notification = u'<span class="form-notification text-danger">Nhập Form sai, vui lòng check lại </span>'
                        status_code = 400
                if need_save_form and status_code ==200:
                    instance = form.save(commit=True)
                    if ( entry_id !="new" and (form_name=="TramForm" or form_name == 'MllForm')):
                        print 'dang luu lich su edit'
                        update_edit_history(ModelOfForm_Class_name, instance, request)

                    id_string =  str(instance.id)
                    if entry_id =="new":
                        form_notification = u'<span class="form-notification text-success">Bạn vừa tạo thành công 1 Đối tượng <span class="name-class-notification">%s</span> có ID là %s.</span>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name],id_string)
                    else:
                        form_notification = u'<span class="form-notification text-success">Bạn vừa Edit thành công 1 Đối tượng <span class="name-class-notification">%s</span>  có ID là %s.</span>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name],id_string)
                    #reload form with newinstance
                    form = FormClass(instance = instance,request=request,khong_show_2_nut_cancel_va_loc=khong_show_2_nut_cancel_va_loc)###############3
                #if not is_download_table:
                if  status_code !=403:
                    dict_render = {'form':form,'form_notification':form_notification}
    #TABLE handle
    if is_download_table or(is_table  and status_code == 200):
        per_page = 15
        if table_name:# and request.method=='POST'
            TableClass = eval('forms.' + table_name)
            ModelofTable_Class = TableClass.Meta.model
            ModelofTable_Class_name = re.sub('Table','',request.GET['table_name'],1)
        else:
            if modelmanager_name =='BCNOSSForm':
                is_groups = []
                
                groups_fields=['group_ngay','is_group_tinh','is_group_BSC_or_RNC','is_group_BTS_Type','is_group_BTS_thiet_bi','is_group_object']
                for x in groups_fields:
                    is_group_1_item = request.GET.get(x,None)
                    if is_group_1_item:
                        kqs = re.subn(r'^is_group_','',x)
                        if kqs[1]:
                            is_groups.append(kqs[0])
                        else:
                            is_groups.append(is_group_1_item)
                if is_groups:
                    table_name = 'ThongKeNgayThangTable'
                    TableClass = eval('forms.' + table_name)
                else:
                    table_name = re.sub('Form$','Table',modelmanager_name)
                    TableClass = eval('forms.' + table_name)
            else:
                table_name = re.sub('Form$','Table',modelmanager_name)
                TableClass = eval('forms.' + table_name)
            # find modelClass and name
            if not is_form:#table only
                ModelofTable_Class_name = re.sub('Form$','',modelmanager_name,1)
                ModelofTable_Class = TableClass.Meta.model
            else:
                ModelofTable_Class_name = ModelOfForm_Class_name
                ModelofTable_Class = ModelOfForm_Class
                
        #print 'table_nametable_nametable_nametable_name',table_name
        if modelmanager_name == 'ThongKeForm':
            querysets = ((x for x in thongkebcn_generator() ))
            table_notification = u'<span class="table_notification">Tất cả  đối tượng trong  <span class="name-class-notification">%s</span> được hiển thị ở table bên dưới</span>'%(ModelofTable_Class_name)
            #per_page = 3
        elif 'tramid' in request.GET:
            if table_name =='TramTable':
                querysets =[]
                tram_object = ModelofTable_Class.objects.get(id=request.GET['tramid'])
                save_history(tram_object.Site_Name_1,request)
                querysets.append(tram_object)
                table_notification =u'<span class="table_notification">Trạm được chọn được hiển thị ở table bên dưới</span>'
                # tim querysets2:
                Site_Name_1 = tram_object.Site_Name_1
                querysets2 = Mll.objects.filter(site_name=Site_Name_1)
                if is_form:
                    if request.GET['search_tu_dong_table_mll']=='yes':
                        table2 = MllTable(querysets2) # vi query set cua form_name=="TramForm" and entry_id !='new' khong order duoc nen phai tach khong di lien voi t
                        RequestConfig(request, paginate={"per_page": 15}).configure(table2)
                        table_notification2 = u'<span class="table_notification">Kết quả tìm Trạm <span style="color:red;">"%s"</span>t rong database <span class="name-class-notification">%s</span>  được hiển thị bên dưới</span>'%(Site_Name_1,VERBOSE_CLASSNAME[ModelofTable_Class_name])
                        dict_render.update({'table2':table2,'table_notification2':table_notification2})
            elif table_name =='MllTable' :#giong nhu tren o tren nhung trong truong hop sort (onlytable), phai di kem voi table only
                tram_object = Tram.objects.get(id=request.GET['tramid'])
                Site_Name_1 = tram_object.Site_Name_1
                querysets = Mll.objects.filter(site_name=Site_Name_1)
                table_notification = u'<span class="table_notification">Kết quả tìm Trạm <span style="color:red;">"%s"</span>t rong database <span class="name-class-notification">%s</span>  được hiển thị bên dưới</span>'%(Site_Name_1,VERBOSE_CLASSNAME[ModelofTable_Class_name])
            else:# trong truong hop manager model ( link chon Chon loai de quan ly)
                querysets =[]
                kq_searchs_one_contain = ModelofTable_Class.objects.get(id=request.GET['tramid'])
                querysets.append(kq_searchs_one_contain)
                table_notification = u'<span class="table_notification"> Đối tượng <span class="name-class-notification">%s</span>  được chọn hiển thị ở table bên dưới</span>'%VERBOSE_CLASSNAME[ModelofTable_Class_name]
        elif 'query_main_search_by_button' in request.GET:
            query = request.GET['query_main_search_by_button']
            if '&' in query:
                contains = request.GET['query_main_search_by_button'].split('&')
                query_sign = 'and'
            else:
                contains = request.GET['query_main_search_by_button'].split(',')
                query_sign = 'or'
            kq_searchs = ModelofTable_Class.objects.none()
            for count,contain in enumerate(contains):
                fname_contain_reconize_tuple = recognize_fieldname_of_query(contain,MYD4_LOOKED_FIELD)#return (longfieldname, searchstring)
                contain = fname_contain_reconize_tuple[1]
                #print 'contain**manager',contain
                fieldnameKey = fname_contain_reconize_tuple[0]
                #print 'fieldnameKey',fieldnameKey
                if fieldnameKey=="all field":
                        FNAME = [f.name for f in ModelofTable_Class._meta.fields if isinstance(f, CharField)]
                        #print 'FNAME',FNAME
                        qgroup = reduce(operator.or_, (Q(**{"%s__%s" %(fieldname,ICONTAINS_OR_IREGEX): contain}) for fieldname in FNAME ))
                        
                        FRNAME = [f.name for f in ModelofTable_Class._meta.fields if (isinstance(f, ForeignKey) or isinstance(f, ManyToManyField) )and f.rel.to !=User]
                        #print 'FRNAME',FRNAME
                        Many2manyfields =[f.name for f in ModelofTable_Class._meta.many_to_many]
                        #print 'Many2manyfields',Many2manyfields
                        FRNAME  = FRNAME + Many2manyfields
                        if FRNAME:
                            qgroup_FRNAME = reduce(operator.or_, (Q(**{"%s__Name__%s" %(fieldname,ICONTAINS_OR_IREGEX): contain}) for fieldname in FRNAME ))
                            qgroup = qgroup | qgroup_FRNAME
                       
                else:
                    qgroup = Q(**{"%s__%s" %(fieldnameKey,ICONTAINS_OR_IREGEX): contain})
                if not fname_contain_reconize_tuple[2]:#neu khong query phu dinh
                    kq_searchs_one_contain = ModelofTable_Class.objects.filter(qgroup)
                else:
                    kq_searchs_one_contain = ModelofTable_Class.objects.exclude(qgroup)
                if query_sign=="or": #tra nhieu tram.
                    kq_searchs = list(chain(kq_searchs, kq_searchs_one_contain))
                elif query_sign=="and": # dieu kien AND but loop all field with or condition
                    if count==0:
                        kq_searchs = kq_searchs_one_contain
                    else:
                        kq_searchs = kq_searchs & kq_searchs_one_contain
            querysets = kq_searchs
            table_notification = u'<span class="table_notification">Kết quả tìm kiếm <span class="query-tim">"%s"</span> trong database <span class="name-class-notification">%s</span>  được hiển thị ở table bên dưới</span>'%(query,VERBOSE_CLASSNAME[ModelofTable_Class_name])
            
        #elif form_name =='Tram_NTPForm':
        elif 'tram_id_for_same_ntp' in request.GET : #da la cai nay thi khong the co loc trong , khi click vao download script 
            instance_site = Tram.objects.get(id = request.GET['tram_id_for_same_ntp'])
            rnc = instance_site.RNC
            IUB_VLAN_ID = instance_site.IUB_VLAN_ID
            querysets = Tram.objects.filter(RNC=rnc,IUB_VLAN_ID=IUB_VLAN_ID)
            table_notification = u'<span class="table_notification"> Danh sách các trạm 3G có cùng VLAN ID và RNC với trạm <span class="query-tim">"%s"</span></span>'%instance_site.Site_ID_3G
            #print 'len(querysets)',len(querysets)
        elif modelmanager_name =='EditHistoryForm':
            edited_object_id = request.GET['edited_object_id']
            modal_name = request.GET['model_name']
            querysets = EditHistory.objects.filter(modal_name = modal_name,edited_object_id=edited_object_id)
            table_notification = u'<span class="table_notification">Lịch sử  chình sửa của instance <span class="query-tim">"%s"</span> này được show ở table dưới: </span>'%(modal_name)
        elif loc:
            
            if loc_pass_agrument:#truong hop nhan nut loc
                FormClass_for_loc =  FormClass
            else:
                print 'table_nametable_nametable_name@@@@@2',table_name
                if table_name=='ThongKeNgayThangTable':
                    FormClass_for_loc = BCNOSSForm
                else:
                    FormClass_for_loc_name =  re.sub('Table$','Form',table_name)
                    FormClass_for_loc= eval('forms.' + FormClass_for_loc_name)
            
            form_for_loc = FormClass_for_loc(data=request.GET,loc=True)
            if form_for_loc.is_valid():#alway valid but you must valid to get form.cleaned_data:
                print '######form cua get loc valid'
            else:
                print 'form.errors',form_for_loc.errors.as_text()
            if modelmanager_name=='MllForm':
                FiterClass=FilterToGenerateQ_ForMLL # adding more out field fiter
            elif modelmanager_name == 'TramForm':
                FiterClass=FilterToGenerateQ_ForTram
            elif modelmanager_name == 'BCNOSSForm':
                FiterClass=FilterToGenerateQ_ForBCNOSSForm
            else:
                FiterClass= FilterToGenerateQ
            qgroup_instance= FiterClass(request,FormClass_for_loc,ModelofTable_Class,form_for_loc.cleaned_data)
            qgroup = qgroup_instance.generateQgroup()
            
            if modelmanager_name == 'BCNOSSForm':
                is_include_code_8 = form_for_loc.cleaned_data['is_include_code_4_7_8']
                if is_include_code_8:
                    qgroup = qgroup
                else:#mac dinh la exclude 478
                    qgroup = qgroup & (~Q(code_loi=8)&~Q(code_loi=7)&~Q(code_loi=4))
                querysets = ModelofTable_Class.objects.filter(qgroup).distinct()
            else:
                querysets = ModelofTable_Class.objects.filter(qgroup).distinct().order_by('-id')
            if loc_pass_agrument:#loc bang nut loc co tra ve form va table
                form_notification = u'<span class="form-notification text-info">  Số kết quả lọc là <span class="soluong-notif">%s</span> trong database <span class="name-class-notification">%s</span> <span>'%(len(querysets),VERBOSE_CLASSNAME[ModelofTable_Class_name])
                dict_render.update({'form_notification':form_notification})
            loc_query = loc_query_for_table_notification(form_for_loc,request)
            table_notification = u'<span class="table_notification"> Số kết quả lọc là <span class="soluong-notif">%s</span> query tìm <span class="query-tim">"%s"</span> trong database <span class="name-class-notification">%s</span>  được hiển thị ở table bên dưới</span>'%(len(querysets),loc_query,VERBOSE_CLASSNAME[ModelofTable_Class_name])
        
        
        else: # if !loc and ...
            
            querysets = ModelofTable_Class.objects.all().order_by('-id')
            table_notification = u'<span class="table_notification">Tất cả <span class="soluong-notif">(%s)</span>  đối tượng trong database <span class="name-class-notification">%s</span> được hiển thị ở table bên dưới</span>'%(len(querysets),VERBOSE_CLASSNAME[ModelofTable_Class_name])
        if table_name=='MllTable':
            try:
                loc_cas = request.GET['loc_ca']
                if loc_cas and loc_cas !="None":
                    q = reduce(operator.or_, (Q(ca_truc__id = ca_name) for ca_name in loc_cas.split('d4') ))
                    querysets = querysets.filter(q)
            except MultiValueDictKeyError:
                pass
                
        elif table_name=='ThongKeNgayThangTable':
            rt = annotation_for_thongkengaythang (querysets,is_groups,is_include_code_8 = is_include_code_8)
            querysets = rt[0]
            aggr = rt[1]
        if status_code != 400:
            if table_name=='ThongKeNgayThangTable':
                table = TableClass(querysets,is_groups = is_groups,is_include_code_8 = is_include_code_8)
                table.aggr = aggr
                
            else:
                table = TableClass(querysets)
            RequestConfig(request, paginate={"per_page": per_page}).configure(table)
            dict_render.update({'table':table,'table_notification':table_notification})
    if is_download_table:
        is_dl_bcn = request.GET.get('download-bcn',None)
        if is_dl_bcn:
            #print 'len(querysets)',len(querysets)
            yesterday_or_other =  request.GET['yesterday_or_other']
            if yesterday_or_other !='theotable':
                return export_excel_bcn(querysets=querysets,yesterday_or_other = yesterday_or_other)
            else:#theotable
                if len(querysets)>1000:
                    dict_render.update({'info_for_alert_box':u'Bạn không có quyền xóa instance MLL or Comment của người khác'})
                    status_code = 403
                    dict_render ={'info_for_alert_box':u'Số dòng báo cáo lơn hơn 1000'}
                    pattern ='drivingtest/form_table_manager.html'
                    return render(request, pattern,dict_render,status=status_code)
                else:
                    return export_excel_bcn(querysets=querysets)
        if request.GET['downloadtable'] == 'csv':
            return table.as_xls_d4_in_form_py_csv(request)
        elif request.GET['downloadtable'] == 'xls':
            return table.as_xls_d4_in_form_py_xls(request)
    else:
        if form_table_template =='form_on_modal' and is_form :# and not click order-sort
            if form:
                form.verbose_form_name =VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name)
            pattern = 'drivingtest/form_table_manager_for_modal.html'
        else:
            pattern ='drivingtest/form_table_manager.html'
        #dict_render['form_notification'] =    u'<h3>%s</h3>'%(u'<span class="notification-datetime">%s</span> '%(datetime.now().strftime(D4_DATETIME_FORMAT)) + dict_render['form_notification'])
        try:
            dict_render['form_notification'] =    u'<div class="form-notifcation-wrapper-div">%s</div>'%(u'<div class="now-notification-div">%s   </div>'%(datetime.now().strftime(D4_DATETIME_FORMAT)) + u'<div class="form-notifcation-div">%s</div>'%dict_render['form_notification'])
        except KeyError:
            pass
        try:    
            dict_render['table_notification'] =    u'<div class="table-notifcation-wrapper-div">%s</div>'%(u'<div class="now-notification-div">%s   </div>'%(datetime.now().strftime(D4_DATETIME_FORMAT)) + u'<div class="form-notifcation-div">%s</div>'%dict_render['table_notification'])
        except KeyError:
            pass
            
        return render(request, pattern,dict_render,status=status_code)
            



def download_script_ntp(request):
    sendmail=0
    site_id = request.GET['site_id']
    #print 'site_id',site_id
    instance_site = Tram.objects.get(id=site_id)
    sitename = instance_site.Site_ID_3G
    if not sitename:
        return HttpResponseBadRequest('khong ton tai site 3G cua tram nay')
    achive_path,loai_tu,path_or_temporaryfile = tao_script( instance_site,ntpServerIpAddressPrimary = request.GET['ntpServerIpAddressPrimary'],\
                              ntpServerIpAddressSecondary= request.GET['ntpServerIpAddressSecondary'],\
                               ntpServerIpAddress1= request.GET['ntpServerIpAddress1'],\
                                ntpServerIpAddress2 = request.GET['ntpServerIpAddress2'])
    
    basename = sitename + "_" + loai_tu + '.zip'
    if sendmail:
        send_email(files= achive_path,filetype='tempt',fname = basename)
    if path_or_temporaryfile:
        #https://djangosnippets.org/snippets/365/
        #wrapper = (file(achive_path, "rb").read())
        wrapper = FileWrapper(file(achive_path, "rb"))
        #Neu khong muon chia nho file:
        #wrapper = (file(achive_path, "rb").read())
        response = HttpResponse(wrapper, content_type='application/zip')
        response['Content-Length'] = os.path.getsize(achive_path)
    else: #achive_path is temporary file
        wrapper = FileWrapper(achive_path)
        achive_path.seek(0)
        response = HttpResponse(wrapper, content_type='application/zip')
        response['Content-Length'] = achive_path.tell()
    
    response['Content-Disposition'] = 'attachment; filename=%s'%(basename)
    #response['Content-Length'] = achive_path.tell()
    #achive_path.seek(0)
    return response 
def edit_history_search(request):
    
    try:
        id_h = request.GET['history_search_id']
        try:
            #print 'id_h',id_h
            instance = SearchHistory.objects.get(id=int(id_h))
        except:
            print 'loi tai instance nay'
        if request.GET['action']=="edit":
            #instance = SearchHistory.objects.get(id=id_h)
            #print request.GET
            for f in H_Field:
                if f in request.GET:
                    value = request.GET[f] 
                    if value!= u'—':
                        setattr(instance,f,value)
                        instance.save()
                        history_search_table = SearchHistoryTable(SearchHistory.objects.all().order_by('-search_datetime'), )
        else:
            
            instance.delete()
            #request.session.flush()
        history_search_table = SearchHistoryTable(SearchHistory.objects.all().order_by('-search_datetime'), )
        RequestConfig(request, paginate={"per_page": 10}).configure(history_search_table)
        return render(request, 'drivingtest/custom_table_template_mll.html',{'table':history_search_table})           
    except Exception as e:
        #print type(e),e
        return HttpResponse(str(e))
from django.template import Template 




ICON_AUTOCOMPLETE_DICT = {'nguyen_nhan':{'class_name':'NguyenNhan','is_admin_allow_dau_hieu_co_add':True},\
                     'du_an':{'class_name':'DuAn','is_admin_allow_dau_hieu_co_add':True},\
                     'su_co':{'class_name':'SuCo','is_admin_allow_dau_hieu_co_add':True},\
                     'trang_thai':{'class_name':'TrangThai','is_admin_allow_dau_hieu_co_add':True},\
                     'tinh':{'class_name':'Tinh','is_admin_allow_dau_hieu_co_add':False},\
                     'quan_huyen':{'class_name':'QuanHuyen','is_admin_allow_dau_hieu_co_add':False},\
                     }
def autocomplete (request):
    query   = request.GET['query'].lstrip().rstrip()
    name_attr = request.GET['name_attr']
    results = [] # results la 1 list gom nhieu dict, moi dict la moi li , moi dict la moi ket qua tim kiem

    if name_attr in ICON_AUTOCOMPLETE_DICT:
        class_name = ICON_AUTOCOMPLETE_DICT[name_attr]['class_name']
        Classeq = eval('models.' + class_name.replace(' ',''))#repeat same if loc
        if query == 'tatca':
            autocomplete_qs = Classeq.objects.all()
            is_admin_allow_dau_hieu_co_add = False
            href_id = None
        else:
            fieldnames = [f.name for f in Classeq._meta.fields if isinstance(f, CharField)  ]
            qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: query}) for fieldname in fieldnames ))
            autocomplete_qs = Classeq.objects.filter(qgroup)
        for doitac in autocomplete_qs[:]:
            doitac_dict = {}
            doitac_dict['label'] = doitac.Name 
            doitac_dict['desc'] = ''
            doitac_dict['id'] = doitac.id
            results.append(doitac_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        }
        is_admin_allow_dau_hieu_co_add = ICON_AUTOCOMPLETE_DICT[name_attr].get('is_admin_allow_dau_hieu_co_add',False)
        if is_admin_allow_dau_hieu_co_add:
            try:
                instance = Classeq.objects.get(Name=query)
                dau_hieu_co_add = False
                href_id = instance.id
            except Classeq.DoesNotExist:
                dau_hieu_co_add = True
                href_id = "new"
            to_json.update({'dau_hieu_co_add':dau_hieu_co_add,'href_id':href_id})
    elif name_attr =='thiet_bi':
        if query == 'tatca':
            autocomplete_qs = ThietBi.objects.all()
            dau_hieu_co_add = False
            href_id = None
        else:
            fieldnames = [f.name for f in ThietBi._meta.fields if isinstance(f, CharField) ]
            if '*' not in query:
                thietbi_name = query
                bts_type_name =None
            else:
                
                gach_index = query.find('*')
                thietbi_name = query[:gach_index].lstrip().rstrip()
                bts_type_name = query[gach_index +1:].lstrip().rstrip()
            karg = {'Name__icontains':thietbi_name}
            if bts_type_name:
                karg.update({'bts_type__Name__icontains':bts_type_name})  
            autocomplete_qs = ThietBi.objects.filter(**karg)
            karg_for_dau_hieu_co_add = {'Name':thietbi_name}
            if bts_type_name:
                karg_for_dau_hieu_co_add.update({'bts_type__Name':bts_type_name})
            try:  
                i = ThietBi.objects.filter(**karg_for_dau_hieu_co_add)[0]
                dau_hieu_co_add = False
                href_id = i.id
            except IndexError:
                dau_hieu_co_add = True
                href_id = "new"
        for doitac in autocomplete_qs[:]:
            doitac_dict = {}
            doitac_dict['label'] = str(doitac) 
            doitac_dict['desc'] = ''
            results.append(doitac_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        }
        to_json.update({'dau_hieu_co_add':dau_hieu_co_add,'href_id':href_id})
    elif name_attr =='thiet_bi1':
        if query == 'tatca':
            autocomplete_qs = ThietBi.objects.all()
            dau_hieu_co_add = False
        else:
            fieldnames = [f.name for f in ThietBi._meta.fields if isinstance(f, CharField) ]
            if '*' not in query:
                qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: query}) for fieldname in fieldnames ))
                autocomplete_qs = ThietBi.objects.filter(qgroup)
                try:
                    ThietBi.objects.get(Name=query)
                    dau_hieu_co_add = False
                except ThietBi.DoesNotExist:
                    dau_hieu_co_add = True
            else:
                gach_index = query.find('*')
                thietbi_name = query[:gach_index].lstrip().rstrip()
                bts_type_name = query[gach_index+1:].lstrip().rstrip()
                qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: thietbi_name}) for fieldname in fieldnames))
                kq_searchs_one_contain = ThietBi.objects.filter(qgroup)
                qgroup = Q(bts_type__Name__icontains = bts_type_name)
                kq_searchs_2nd = ThietBi.objects.filter(qgroup)
                autocomplete_qs = kq_searchs_one_contain & kq_searchs_2nd
                
                try:
                    bts_type = BTSType.objects.get(Name =bts_type_name )
                    dau_hieu_co_add = False
                except:
                    dau_hieu_co_add = True
                if dau_hieu_co_add ==False:
                    try:                    
                        ThietBi.objects.get(Name=thietbi_name,bts_type = bts_type)
                        dau_hieu_co_add = False
                    except ThietBi.DoesNotExist:
                        dau_hieu_co_add = True
        for doitac in autocomplete_qs[:]:
            doitac_dict = {}
            doitac_dict['label'] = str(doitac) 
            doitac_dict['desc'] = ''
            results.append(doitac_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        }
        to_json.update({'dau_hieu_co_add':dau_hieu_co_add})
    elif name_attr =='doi_tac' :
        if query=='tatca':
            autocomplete_qs = DoiTac.objects.all()
            dau_hieu_co_add = False 
            href_id = 'new'
            
        elif '*' not in query:
            fieldnames = [f.name for f in DoiTac._meta.fields if isinstance(f, CharField)  ]
            qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: query}) for fieldname in fieldnames ))
            autocomplete_qs = DoiTac.objects.filter(qgroup).distinct()
            doi_tac_check = luu_doi_tac_toold4(query)
            dau_hieu_co_add = True if not doi_tac_check else False 
        else:# there '-' in query
            fieldnames = [f.name for f in DoiTac._meta.fields if isinstance(f, CharField)  ]
            contains = query.split('*')
            for count,contain in enumerate(contains):
                qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: contain}) for fieldname in fieldnames))
                kq_searchs_one_contain = DoiTac.objects.filter(qgroup)
                if count==0:
                    autocomplete_qs = kq_searchs_one_contain
                else:
                    autocomplete_qs = autocomplete_qs & kq_searchs_one_contain
            doi_tac_check = luu_doi_tac_toold4(query)
            dau_hieu_co_add = True if not doi_tac_check else False
        if dau_hieu_co_add:
            href_id = "new"
        elif  query!='tatca':
            href_id =  doi_tac_check.id
               
        for doitac in autocomplete_qs[:]:
            doitac_dict = {}
            doitac_dict['label'] = str(doitac)
            doitac_dict['desc'] = doitac.So_dien_thoai if doitac.So_dien_thoai else 'chưa có sdt'
            doitac_dict['id'] = doitac.id
            results.append(doitac_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        }
        to_json.update({'dau_hieu_co_add':dau_hieu_co_add,'href_id':href_id})
    elif name_attr =='thao_tac_lien_quan':
        if query == 'tatca':
            autocomplete_qs = ThaoTacLienQuan.objects.all()
        else:
            querys = query.split(',')
            query = querys[-1].rstrip().lstrip()
            fieldnames = [f.name for f in ThaoTacLienQuan._meta.fields if isinstance(f, CharField)  ]
            qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: query}) for fieldname in fieldnames ))
            autocomplete_qs = ThaoTacLienQuan.objects.filter(qgroup)
        for doitac in autocomplete_qs[:]:
            doitac_dict = {}
            doitac_dict['label'] = doitac.Name 
            doitac_dict['desc'] =  ''
            doitac_dict['id'] =  doitac.id
            results.append(doitac_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        }
        if query=='tatca':
            dau_hieu_co_add_so_luong = 0#khong add, info
            to_json.update({'curent_add':0})
            href_id = "new"#hinh thuc, thuc ra jquery no xac dinh cho.
            last_add_item = ''
        else:
            dau_hieu_co_add_so_luong = 0
            last_add_item = ''
            for count,query in enumerate(querys):
                query = query.rstrip().lstrip()
                if query=="":#tatca
                    to_json.update({'curent_add':0})
                    continue
                else:
                    try:
                        instance = ThaoTacLienQuan.objects.get(Name=query)
                    except ThaoTacLienQuan.DoesNotExist:
                        last_add_item = query
                        dau_hieu_co_add_so_luong += 1
                        if count ==len(querys) -  1:
                            to_json.update({'curent_add':1})
                if dau_hieu_co_add_so_luong ==0:#info
                    href_id = instance.id
                else:
                    href_id = "new"
        to_json.update({'dau_hieu_co_add':dau_hieu_co_add_so_luong,'href_id':href_id,'last_add_item':last_add_item})
    elif name_attr =='manager_suggestion':
        modelClass = eval('models.'+request.GET['model_attr_global'])
        if query=='tatca':
            querys = modelClass.objects.all()
        else:
            fieldnames = [f.name for f in modelClass._meta.fields if isinstance(f, CharField)  ]
            qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: query}) for fieldname in fieldnames ))
            querys = modelClass.objects.filter(qgroup)
        for object in querys[:10]:
            object_dict = {}
            object_dict['label'] = object.__unicode__()
            object_dict['id'] = object.id
            object_dict['desc'] = ''
            results.append(object_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        }
    
    elif 'specific_problem_m2m' in name_attr:
        qgroup = Q(Name__icontains=query)
        autocomplete_qs = FaultLibrary.objects.filter(qgroup)
        for doitac in autocomplete_qs[:]:
            doitac_dict = {}
            doitac_dict['label'] = doitac.Name 
            doitac_dict['desc'] =  ''
            results.append(doitac_dict)
        to_json = {
            "key_for_list_of_item_dict": results,
        } 
    
    elif name_attr =='object' or name_attr =="main_suggestion":
        contain = query
        if contain =='tatca':
            fieldnames = MYD4_LOOKED_FIELD
            contain = 'a'
        elif contain =='':
            fieldnames = {'Site_ID_3G':'3G'}
        else:
            fieldnames = MYD4_LOOKED_FIELD
        
        for fieldname,sort_fieldname  in fieldnames.iteritems(): #Loop through all field
            #if '.*?' in contain:
            if 1:
                icontains_or_iregex = 'iregex'
            else:
                icontains_or_iregex = 'icontains'
            contain = contain.replace(' ','[-_]')
            q_query = Q(**{"%s__%s" % (fieldname,icontains_or_iregex): contain})
            one_field_searchs = Tram.objects.filter(q_query)[0:20]
            if len(one_field_searchs)>0:
                for tram in one_field_searchs:
                    tram_dict = {}
                    try:
                        if fieldname =="Site_ID_3G":
                            thiet_bi = str(tram.Cabinet)
                        elif fieldname =="Site_ID_2G":
                            thiet_bi =str(tram.nha_san_xuat_2G)
                        else:
                            thiet_bi = "2G&3G"
                    except Exception as e:
                            thiet_bi = 'error' + tram.Site_Name_1
                            #print e, tram
                    tram_dict['id'] = tram.id
                    tram_dict['sort_field'] = sort_fieldname
                    tram_dict['label'] =  getattr(tram,fieldname)
                    tram_dict['thiet_bi'] =  thiet_bi
                    tram_dict['site_name_1'] = tram.Site_Name_1
 
                    tram_dict['sn1'] = show_string_avoid_none(tram.Site_Name_1)
                    tram_dict['sn2'] = show_string_avoid_none(tram.Site_Name_2,none_string_presentation='__')
                    tram_dict['s3g'] = show_string_avoid_none (tram.Site_ID_3G,none_string_presentation='__')
                    tram_dict['s2g'] = show_string_avoid_none (tram.Site_ID_2G,none_string_presentation='__')
                    
                    
                    tram_dict['s4g'] = show_string_avoid_none (tram.eNodeB_Name,none_string_presentation='__')
                    tram_dict['s4g_thietbi'] = str(tram.eNodeB_Type)
                    tram_dict['s3g_thietbi'] = str(tram.Cabinet)
                    
                    tram_dict['s2g_thietbi'] = str(tram.nha_san_xuat_2G)
                    results.append(tram_dict)
        to_json = {
                "key_for_list_of_item_dict": results,
            }
    return HttpResponse(simplejson.dumps(to_json), content_type='application/json')


def delete_mll (request):
    id = request.GET['query']
    mll_instance  = Mll.objects.get(id=int(id))
    mll_instance.comments.all().delete()
    mll_instance.delete()
    table = MllTable(Mll.objects.all().order_by('-id'))
    RequestConfig(request, paginate={"per_page": 15}).configure(table)        
    return render(request, 'drivingtest/custom_table_template.html',{'table':table})
#from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper



def save_history(query,request):
    if (SearchHistory.objects.filter(thanh_vien=request.user).count() > 3 ):
                oldest_instance= SearchHistory.objects.all().order_by('search_datetime')[0]
                oldest_instance.query_string = query
                oldest_instance.search_datetime = datetime.now()
                oldest_instance.thanh_vien = request.user
                oldest_instance.save()
    else:
        instance = SearchHistory(query_string=query,search_datetime = datetime.now(),thanh_vien = request.user)
        instance.save()

@login_required
def upload_bcn_excel(request):
    if request.method == 'POST' :
        if 'file' in request.FILES:
                #print request.FILES['file'].name
                #return HttpResponse(request.FILES['file'].name)
                fcontain = request.FILES['file'].read()
                workbook = xlrd.open_workbook(file_contents=fcontain)
                
                #import_database_4_cai_new(choices,workbook = workbook,import_ghi_chu = request.FILES['file'].name )
                thongbao_so_luong = import_database_4_cai_new(['ImportBCN2G'],workbook = workbook)
                result_handle_file ='''<div class="alert alert-block alert-success" style=""><strong>%s</br>%s</strong></div>'''\
                %(u"Đã import xong từ file %s!!!"%request.FILES['file'].name,thongbao_so_luong)
        else: 
            result_handle_file ='''<div class="alert alert-block alert-danger" style=""><strong>%s</strong></div>'''%u'Thiếu File!!!'
    else:
        result_handle_file ='''<div class="alert alert-block alert-warning" style=""><strong>%s</strong></div>'''%u"Chọn File"
    return render(request, 'drivingtest/import_db_from_excel_bcn.html',{'result_handle_file':result_handle_file})
    
    
    
@login_required
def upload_excel_file(request):
    context = RequestContext(request)
    if not request.user.is_superuser:
        result_handle_file ='''<div class="alert alert-block alert-danger" style=""><strong>%s</strong></div>'''%u"Bạn không có quyến import data"
    elif request.method == 'POST' :
        choices =  request.POST.getlist('sheetchoice')
        if choices:
            is_available_file_tick =  request.POST.get('is_available_file',False)
            if not is_available_file_tick: # Neu khong tick vao cai o chon file co san
                if 'file' in request.FILES:
                    fcontain = request.FILES['file'].read()
                    workbook = xlrd.open_workbook(file_contents=fcontain)
                    thongbao_so_luong = import_database_4_cai_new(choices,workbook = workbook,import_ghi_chu = request.FILES['file'].name )
                    result_handle_file ='''<div class="alert alert-block alert-success" style=""><strong>%s</br>%s</strong></div>'''%(u"Đã import xong từ file %s!!!"%request.FILES['file'].name,thongbao_so_luong)
                else: # but not file upload so render invalid
                    result_handle_file ='''<div class="alert alert-block alert-danger" style=""><strong>%s</strong></div>'''%u'Thiếu File, hoặc bạn phải tick vào is_available_file_tick'
            else:#
                workbook = None
                result_handle_file ='''<div class="alert alert-block alert-success" style=""><strong>%s</strong></div>'''%u"Đã import xong từ file bạn chọn!!!"u"Đã import xong từ file có sắn ở server!!!"
                print 'okkkkkkkkkkkkkkkkkkkkkkkk'
                import_database_4_cai_new(choices,workbook = workbook)
        else:
            result_handle_file ='''<div class="alert alert-block alert-danger" style=""><strong>%s</strong></div>'''%u"Bạn phải chọn database gì"
    else:#GET
        result_handle_file ='''<div class="alert alert-block alert-warning" style=""><strong>%s</strong></div>'''%u"Mời bạn chọn "
    return render_to_response('drivingtest/import_db_from_excel.html', {'result_handle_file':result_handle_file},context)



#https://docs.djangoproject.com/en/1.8/howto/outputting-csv/




#############################################################################




'''   
                    if form_name=="MllForm":
                        #now = datetime.now()
                        instance = form.save()
                        mll_instance= instance
                        #update_trang_thai_cho_mll(mll_instance)
                     
                        
                        if entry_id =="new":
                            instance = form.save(commit=False)
                            mll_instance= instance
                            #mll_instance.ca_truc = request.user.get_profile().ca_truc
                        else:#Edit mll
                            instance = form.save(commit=False)
                            mll_instance=instance
                            #mll_instance.edit_reason = request.GET['edit_reason']
                            update_trang_thai_cho_mll(mll_instance)
                        #mll_instance.last_update_time = now
                        mll_instance.save()# save de tao nhung cai database relate nhu foreinkey.
                        #form.save_specific_problem_m2m()
                        # luu specific_problem_m2m
                        
                        
                        if form.cleaned_data['specific_problem_m2m']:
                            specific_problem_m2ms = form.cleaned_data['specific_problem_m2m'].split('\n')
                            for count,specific_problem_m2m in enumerate(specific_problem_m2ms):
                                if '**' in specific_problem_m2m:
                                    faulcode_hyphen_objects = specific_problem_m2m.split('**')
                                    try:
                                        faultLibrary_instance = FaultLibrary.objects.get(Name = faulcode_hyphen_objects[0])
                                    except :
                                        faultLibrary_instance = FaultLibrary(Name = faulcode_hyphen_objects[0])
                                        faultLibrary_instance.ngay_gio_tao = datetime.now()
                                        faultLibrary_instance.nguoi_tao = request.user
                                        faultLibrary_instance.save()
                                    if len(faulcode_hyphen_objects) > 1:
                                        object_name = faulcode_hyphen_objects[1]
                                    else:
                                        object_name=None
                                else:
                                    faultLibrary_instance = None
                                    object_name = specific_problem_m2m
                                if entry_id =="new":
                                    SpecificProblem.objects.create(fault = faultLibrary_instance, object_name = object_name,mll=mll_instance)
                                else:#ghi chong len nhung entry problem specific dang co
                                    specific_problem_queryset_from_db_s = mll_instance.specific_problems.all()
                                    try:
                                        specific_problem = specific_problem_queryset_from_db_s[count]
                                        specific_problem.fault = faultLibrary_instance
                                        specific_problem.object_name = object_name
                                        specific_problem.save()
                                    except IndexError: # neu thieu instance hien tai so voi nhung instance sap duoc ghi thi tao moi 
                                        SpecificProblem.objects.create(fault = faultLibrary_instance, object_name = object_name,mll=mll_instance)
                                    # delete nhung cai specific_problems khong duoc ghi chong
                                    if (len(specific_problem_queryset_from_db_s) > count): 
                                        for x in specific_problem_queryset_from_db_s[count+1:]:
                                            x.delete()
                                        
                        # luu CommentForm trong luu MllForm
                        
                        if entry_id =="new":
                            CommentForm_i = CommentForm(request.POST,request = request)
                            #if CommentForm_i.is_valid():
                            first_comment = CommentForm_i.save(commit=False)
                            #first_comment.nguoi_tao = user
                            first_comment.mll = mll_instance
                            first_comment.save()
                            CommentForm_i.save_m2m()
                        
                            
                        
                        #RELOad new form
                        
                        #form = MllForm(instance=mll_instance,request=request)
                          
                    elif form_name=="CommentForm":
                        instance = form.save(commit=False)
                        if entry_id =="new":
                                comment_instance = instance
                                mll_instance  = Mll.objects.get(id=request.POST['mll'])
                                comment_instance.mll = mll_instance
                        else:
                            comment_instance = instance
                            mll_instance = instance.mll
                            olddatetime = comment_instance.datetime
                            if not request.POST['datetime']:
                                comment_instance.datetime = olddatetime
                        comment_instance.save()
                        form.save_m2m() 
                        if form.cleaned_data['trang_thai'].is_cap_nhap_gio_tot:
                            mll_instance.gio_tot = comment_instance.datetime
                            mll_instance.save()
                        if form.cleaned_data['trang_thai'].Name==u'Báo ứng cứu':
                            mll_instance.ung_cuu = True
                            mll_instance.save()
                        update_trang_thai_cho_mll(mll_instance)
                        
                    #elif form_name=="CommentForm":
                        #update_trang_thai_cho_mll(mll_instance)  
                    if form_name=="Tram_NTPForm":
                        form.save(commit=True)
                        if (request.GET.get('update_all_same_vlan_sites',None)=='yes'):
                            rnc = instance.RNC
                            IUB_VLAN_ID = instance.IUB_VLAN_ID
                            same_sites = Tram.objects.filter(RNC=rnc,IUB_VLAN_ID=IUB_VLAN_ID)
                            same_sites.update(**dict([(fn,request.POST[fn])for fn in NTP_Field]))
                    else:
                        '''
'''
def tram_table(request,no_return_httpresponse = False): # include search tram 
    #print 'tram_table'
    if 'id' in request.GET:
        id = request.GET['id']
        querysets =[]
        kq_searchs_one_contain = Tram.objects.get(id=id)
        querysets.append(kq_searchs_one_contain)
        query = request.GET['query']
        save_history(query)
    elif 'query' not in request.GET and 'id' not in request.GET or (request.GET['query']=='')  : # khong search, khong chose , nghia la querysets khi load page index
        querysets = Tram.objects.all()
    elif 'query' in request.GET : # tuc la if request.GET['query'], nghia la dang search:
        query = request.GET['query']
        #print 'this mine',query
        if '&' in query:
            contains = request.GET['query'].split('&')
            query_sign = 'and'
        else:
            contains = request.GET['query'].split(',')
            query_sign = 'or'
        kq_searchs = Tram.objects.none()
        for count,contain in enumerate(contains):
            fname_contain_reconize_tuple = recognize_fieldname_of_query(contain,MYD4_LOOKED_FIELD)#return (longfieldname, searchstring)
            contain = fname_contain_reconize_tuple[1]
            #print 'contain',contain
            fieldnameKey = fname_contain_reconize_tuple[0]
            #print 'fieldnameKey',fieldnameKey
            if fieldnameKey=="all field":
                    FNAME = [f.name for f in Tram._meta.fields if isinstance(f, CharField)]
                    qgroup = reduce(operator.or_, (Q(**{"%s__icontains" % fieldname: contain}) for fieldname in FNAME ))
                    FRNAME = [f.name for f in Tram._meta.fields if (isinstance(f, ForeignKey) or isinstance(f, ManyToManyField))]
                    #print 'FRNAME',FRNAME
                    Many2manyfields =[f.name for f in Tram._meta.many_to_many]
                    #print 'Many2manyfields',Many2manyfields
                    FRNAME  = FRNAME + Many2manyfields
                    qgroup_FRNAME = reduce(operator.or_, (Q(**{"%s__Name__icontains" % fieldname: contain}) for fieldname in FRNAME ))
                    qgroup = qgroup | qgroup_FRNAME
            else:
                #print 'fieldnameKey %s,contain%s'%(fieldnameKey,contain)
                qgroup = Q(**{"%s__icontains" % fieldnameKey: contain})
            if not fname_contain_reconize_tuple[2]:#neu khong query phu dinh
                kq_searchs_one_contain = Tram.objects.filter(qgroup)
            else:
                kq_searchs_one_contain = Tram.objects.exclude(qgroup)
            if query_sign=="or": #tra nhieu tram.
                kq_searchs = list(chain(kq_searchs, kq_searchs_one_contain))
            elif query_sign=="and": # dieu kien AND but loop all field with or condition
                if count==0:
                    kq_searchs = kq_searchs_one_contain
                else:
                    kq_searchs = kq_searchs & kq_searchs_one_contain
        querysets = kq_searchs
        #print 'len(querysets)',len(querysets)    
        #save_history(query)    
    
    if no_return_httpresponse:
        return querysets
    else:
        table = TramTable(querysets,) 
        dict_context = {'table': table}
        RequestConfig(request, paginate={"per_page": 10}).configure(table)
        return render(request, 'drivingtest/custom_table_template_mll.html', dict_context)
'''
