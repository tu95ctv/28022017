# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
print 'in model 2'
from django.db import models
from django.contrib.auth.models import User
from django import forms

#from drivingtest.forms import D4_DATETIME_FORMAT
D4_DATETIME_FORMAT = '%H:%M %d/%m/%Y'
        ##OMCKV2
class IPAddress_FieldNullable(models.IPAddressField):
    def get_db_prep_save(self,value,connection,prepared=False):
        return value or None   




    
class EditHistory(models.Model):
    modal_name = models.CharField(max_length=50)
    edited_object_id = models.IntegerField()
    thanh_vien = models.ForeignKey(User,null=True,blank=True,verbose_name=u"Thành viên sửa")
    ly_do_sua = models.CharField(max_length=250)
    edit_datetime= models.DateTimeField(null=True,blank=True)#3
    
    
class ThietBi(models.Model):
    Name = models.CharField(max_length=20,unique=True,null=True)
    #ghi_chu = RichTextField(max_length=10000,blank=True)
    ghi_chu = models.CharField(max_length=10000,null=True,blank=True)#3
    color_code = models.CharField(max_length=15,null=True,blank=True)
    #tai_lieu_huong_dan = models.CharField(max_length=10000,blank=True)
    is_duoc_tao_truoc = models.BooleanField(verbose_name=u"Không cho phép sửa field Name")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_thietbi_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_thietbi_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    
    def __unicode__(self):
        return self.Name  
class DoiTac(models.Model):#khong co color code
    #First_name = models.CharField(max_length=20,null=True,blank=True)
    Name = models.CharField(max_length=80)
    Name_khong_dau = models.CharField(max_length=80,null=True,blank=True)
    Don_vi  = models.CharField(max_length=80,null=True,blank=True)
    So_dien_thoai  = models.CharField(max_length=80,null=True,blank=True)
    Nam_sinh  = models.CharField(max_length=80,null=True,blank=True)
    dia_chi_email = models.EmailField(max_length=80,null=True,blank=True)
    Thong_tin_khac  = models.CharField(max_length=80,null=True,blank=True)
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_doitac_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_doitac_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    email = models.CharField(max_length=80,null=True,blank=True)
    def __unicode__(self):
        return self.Name  + ("-" + self.Don_vi if self.Don_vi else "")
class DuAn(models.Model):
    Name=models.CharField(max_length=150)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    ghi_chu = models.CharField(max_length=1330,null=True,blank=True)
    #ghi_chu = RichTextField(max_length=1330,null=True,blank=True)
    type_2G_or_3G = models.CharField(max_length=2,blank=True)
    thoi_diem_bat_dau= models.DateTimeField(null=True,blank=True,verbose_name=u"thời điểm bắt đầu")#3
    thoi_diem_ket_thuc= models.DateTimeField(null=True,blank=True,verbose_name=u"thời điểm kết thúc")#3
    doi_tac_du_an = models.ManyToManyField(DoiTac,null=True,blank=True)
    is_duoc_tao_truoc = models.BooleanField(default = False,verbose_name=u"Không cho phép sửa field Name")
    #default = User.objects.get(username = "tund").id
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_duan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_duan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.Name
    
    
class SuCo (models.Model):
    Name = models.CharField(max_length=150,unique=True)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    Ghi_chu = models.CharField(max_length=10000,null=True,blank=True)

    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_nguyennhan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_nguyennhan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=timezone.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    
    def __unicode__(self):
        return self.Name
class NguyenNhan (models.Model):
    Name = models.CharField(max_length=150,unique=True)
    Name_khong_dau = models.CharField(max_length=150,null=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    Ghi_chu = models.CharField(max_length=10000,null=True,blank=True)
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_NguyenNhan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_NguyenNhan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=timezone.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    
    def __unicode__(self):
        return self.Name
class CaTruc(models.Model):
    Name = models.CharField(max_length=30,unique=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    ghi_chu = models.CharField(max_length=10000,null=True,blank=True)
    is_duoc_tao_truoc = models.BooleanField(default=False,verbose_name = u"Không cho phép sửa field Name")
    #nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_trangthai_set',blank=True)
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_catruc_set',blank=True,verbose_name=u"người sửa cuối cùng")
    #ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    
    
    def __unicode__(self):
        return self.Name
class TrangThai(models.Model):
    Name = models.CharField(max_length=100,unique=True)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    #ghi_chu = models.CharField(max_length=10000,null=True,blank=True)
    ghi_chu = RichTextField(max_length=10000,null=True,blank=True)
    #stylecss_name = models.CharField(max_length=100,null=True,blank=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    is_cap_nhap_gio_tot =models.BooleanField()
    is_duoc_tao_truoc = models.BooleanField(default = False,verbose_name=u"Không cho phép sửa field Name")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_trangthai_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_trangthai_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.Name
class ThaoTacLienQuan(models.Model):
    Name = models.CharField(unique=True,max_length=100)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    ghi_chu = models.CharField(max_length=200,null=True,blank=True)#3
    Name_khong_dau = models.CharField(max_length=100,null=True)
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_ThaoTacLienQuan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_ThaoTacLienQuan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.Name
class FaultLibrary(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    diversity = models.CharField(max_length=10,blank=True,null=True)
    ghi_chu =models.CharField(max_length=10000,blank=True)
    
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_FaultLibrary_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_FaultLibrary_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.Name
class Lenh(models.Model):
    command= models.CharField(max_length=5000,unique=True)#3
    Name= models.CharField(max_length=200,null=True,blank=True)#3
    Name_khong_dau = models.CharField(max_length=80,null=True,blank=True)
    #phan_loai_thiet_bi= models.CharField(max_length=50,null=True,blank=True)#3
    thiet_bi= models.ForeignKey(ThietBi,null=True,blank = True,verbose_name=u"Thiết bị")#12
    ghi_chu_lenh= models.CharField(max_length=200,null=True,blank=True,verbose_name=u"Ghi chú")#3
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_Lenh_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_Lenh_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    
    def __unicode__(self):
        return self.command
class Tinh(models.Model):
    Name= models.CharField(max_length=50,unique=True)#3
    Name_khong_dau = models.CharField(max_length=50,blank=True,unique=True)
    dia_ban = models.CharField(max_length=80,verbose_name=u"Địa bàn")
    ma_tinh = models.CharField(max_length=4,unique=True)
    ghi_chu =models.CharField(max_length=10000,blank=True,null=True)
    
    
    
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_Tinh_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
class BSCRNC(models.Model):
    Name = models.CharField(max_length=50,unique=True)
    HANG_SX = models.CharField(max_length=20,null=True,blank=True)
    DIA_CHI = models.CharField(max_length=200,null=True,blank=True)
    DIEN_THOAI = models.CharField(max_length=20,null=True,blank=True)
    VI_TRI_RNC = models.ForeignKey(Tinh,null=True)
    TINH_RNC_QUAN_LY=models.CharField(max_length=50,null=True,blank=True)
    MSS = models.CharField(max_length=20,null=True,blank=True)
    SGSN = models.CharField(max_length=20,null=True,blank=True)
    
    ghi_chu =models.CharField(max_length=10000,blank=True,null=True)
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_BSCRNC_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_BSCRNC_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.Name 
class Tram(models.Model):
    License_60W_Power = models.NullBooleanField(blank = True) #1
    U900 = models.NullBooleanField(blank = True,null=True)#2
    Site_ID_3G= models.CharField(max_length=80,null=True,blank = True)#3
    Ngay_Phat_Song_2G = models.DateField(null=True,blank = True,verbose_name=u"Ngày phát sóng 2G")#5
    Ngay_Phat_Song_3G = models.DateField(null=True,blank = True,)#8
    Site_Name_1= models.CharField(max_length=80,null=True)
    Site_Name_2= models.CharField(max_length=80,null=True,blank = True)
    #BSC  = models.CharField(max_length=15,null=True,blank = True,)#9
    Status = models.CharField(max_length=50,null=True,blank = True,)#10
    Project_Text = models.CharField(max_length=100,null=True,blank = True,)#10
    Trans= models.CharField(max_length=40,null=True,blank = True,)#11
    Cabinet = models.ForeignKey(ThietBi,null=True,blank = True,related_name="Tramcuathietbis",verbose_name = u'Thiết bị 3G')#12
    Port = models.CharField(max_length=40,null=True,blank = True,)#13
    #RNC = models.CharField(max_length=40,null=True,blank = True,)#14
    RNC = models.ForeignKey(BSCRNC,null=True,blank = True)#14
    BSC_2G = models.ForeignKey(BSCRNC,null=True,blank = True,related_name='bscrnc_dot_Tram_BSC_2G_set')#35
    IUB_VLAN_ID = models.CharField(max_length=4,null=True,blank = True)#15
    IUB_SUBNET_PREFIX = IPAddress_FieldNullable(max_length=40,null=True,blank = True,)#16
    IUB_DEFAULT_ROUTER = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#17
    IUB_HOST_IP = IPAddress_FieldNullable(null=True,blank = True)#18
    MUB_VLAN_ID = models.CharField(max_length=4,null=True,blank = True)#19
    MUB_SUBNET_PREFIX = IPAddress_FieldNullable(max_length=40,null=True,blank = True,)#20
    MUB_DEFAULT_ROUTER = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#21
    MUB_HOST_IP = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#22
    UPE = models.CharField(max_length=140,null=True,blank = True,)#23
    GHI_CHU = models.CharField(max_length=1000,null=True,blank = True,)#24
    dia_chi_3G = models.CharField(max_length=200,null=True,blank = True,)#35
    Count_Province = models.CharField(max_length=40,null=True,blank = True,)#25
    Count_RNC = models.CharField(max_length=40,null=True,blank = True,)#26
    Cell_1_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#27
    Cell_2_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#28
    Cell_3_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#29
    Cell_4_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#30
    Cell_5_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#31
    Cell_6_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#32
    Cell_7_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#33
    Cell_8_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#34
    Cell_9_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#35
    Cell_K_U900_PSI =  models.CharField(max_length=40,null=True,blank = True,)#35
    dia_chi_2G = models.CharField(max_length=200,null=True,blank = True,)#35
    
    Site_ID_2G = models.CharField(max_length=80,null=True,blank = True,)#35
    Site_ID_2G_Number = models.CharField(max_length=10,null=True,blank = True,)#35
    LAC_2G = models.CharField(max_length=20,null=True,blank = True,)#35
    Nha_Tram = models.CharField(max_length=20,null=True,blank = True,)#35
    Ma_Tram_DHTT = models.CharField(max_length=20,null=True,blank = True,)#35
    Cell_ID_2G = models.CharField(max_length=20,null=True,blank = True,)#35
    cau_hinh_2G = models.CharField(max_length=20,null=True,blank = True,)#35
    nha_san_xuat_2G = models.ForeignKey(ThietBi,null=True,blank = True,verbose_name = u'Thiết bị 2G')#35
    TG_Text = models.CharField(max_length=150,null=True,blank = True,)#35
    TG = models.CharField(max_length=3,null=True,blank = True)#35
    TG_1800 = models.CharField(max_length=3,null=True,blank = True,)#35
    Long_3G = models.CharField(max_length=30,null=True,blank = True,)#35
    Lat_3G = models.CharField(max_length=30,null=True,blank = True,)#35
    Long_2G = models.CharField(max_length=30,null=True,blank = True,)#35
    Lat_2G = models.CharField(max_length=30,null=True,blank = True,)#35
    TRX_DEF = models.CharField(max_length=50,null=True,blank = True,)#35
    ntpServerIpAddressPrimary = models.CharField(max_length=20,null=True,blank = True,)
    ntpServerIpAddressSecondary = models.CharField(max_length=20,null=True,blank = True,)
    ntpServerIpAddress1 = models.CharField(max_length=20,null=True,blank = True,)
    ntpServerIpAddress2 = models.CharField(max_length=20,null=True,blank = True,)
    du_an = models.ManyToManyField(DuAn,null=True,blank=True)
    eNodeB_Name = models.CharField(max_length=40,null=True,blank = True,)#35
    eNodeB_ID_DEC = models.CharField(max_length=6,null=True,blank = True)
    eNodeB_Type = models.ForeignKey(ThietBi,null=True,blank = True,related_name='ThietBi_of_eNodeB')#12
    is_co_U900_rieng = models.NullBooleanField(blank = True,default=False)
    is_co_U2100_rieng = models.NullBooleanField(blank = True,default=False)
    active_3G = models.BooleanField(default = False)
    active_2G = models.BooleanField(default = False)
    active_4G = models.BooleanField(default = False)
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_tram_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_tram_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=timezone.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    
    
    def __unicode__(self):
        if self.Site_Name_1:
            return self.Site_Name_1
        else:
            return str(self.id)
class Mll(models.Model):
    object= models.CharField(max_length=50,verbose_name = u'Đối tượng')
    site_name= models.CharField(max_length=50,null=True,blank=True,verbose_name=u"Site name")#3
    thiet_bi= models.ForeignKey(ThietBi,null=True,blank = True,verbose_name=u"Thiết bị")#12
    su_co = models.ForeignKey(SuCo,related_name="Mlls",null=True,blank=True,verbose_name=u"Sự cố")
    nguyen_nhan = models.ForeignKey(NguyenNhan,related_name="mll_set_of_NguyenNhan",null=True,blank=True,verbose_name=u"Nguyên nhân")
    du_an = models.ForeignKey(DuAn,related_name="DuAns",null=True,blank=True,verbose_name=u"dự án/công việc")
    ung_cuu = models.BooleanField(verbose_name=u"ư/c",default = False)
    #thanh_vien = models.ForeignKey(User,null=True,blank=True,verbose_name=u"Thành viên tạo")
    ca_truc = models.ForeignKey(CaTruc,blank=True,null=True,verbose_name=u"Ca trực")
    #last_edit_member = models.ForeignKey(User,null=True,blank=True,related_name = 'mll_set_of_last_edit_member')
    #last_update_time= models.DateTimeField(null=True,blank=True,verbose_name=u"update_time")#3
    gio_mat= models.DateTimeField(blank=True,verbose_name=u"giờ mất")#3
    gio_tot= models.DateTimeField(null=True,blank=True,verbose_name=u"giờ tốt")#3
    trang_thai = models.ForeignKey(TrangThai,null=True,blank=True,verbose_name=u"Trạng thái")
    #specific_problem= models.CharField(max_length=1000,null=True,blank=True)#3
    giao_ca = models.BooleanField(verbose_name=u"g/ca",default = False)
    nghiem_trong = models.BooleanField(verbose_name=u"N/trọng",default = False)
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_mlll_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_mll_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now(),verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.object
class SpecificProblem(models.Model):
    fault = models.ForeignKey(FaultLibrary,null=True,blank=True)
    object_name = models.CharField(max_length=200,null=True,blank=True)
    mll = models.ForeignKey(Mll,related_name ='specific_problems')
    def __unicode__(self):
        return ((self.fault.Name  + '**' ) if self.fault else '')  + self.object_name
    

        
class Comment(models.Model):
    datetime= models.DateTimeField(blank=True,verbose_name=u"nhập giờ")
    doi_tac = models.ForeignKey(DoiTac,related_name="Comments",null=True,blank=True,verbose_name=u"đối tác")
    comment= models.CharField(max_length=2000,null=True,blank=True)# if bo blank=False mac dinh se la true chelp_text="add comment here",
    comment= RichTextField(max_length=2000,null=True,blank=True)# if bo blank=False mac dinh se la true chelp_text="add comment here",
    trang_thai = models.ForeignKey(TrangThai,blank=True,verbose_name=u"Trạng thái")
    thao_tac_lien_quan = models.ManyToManyField(ThaoTacLienQuan,blank=True,null=True)
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_comment_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_comment_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(verbose_name=u"Ngày giờ sửa cuối cùng",blank=True,null=True)#3
    mll = models.ForeignKey(Mll,related_name="comments",blank=True)
    def __unicode__(self):
        return self.comment
class SearchHistory(models.Model):
    query_string= models.CharField(max_length=200,null=True,blank=True)#3
    #thanh_vien = models.CharField(max_length=40,null=True,blank=True)#3
    thanh_vien = models.ForeignKey(User,null=True,blank=True)#3
    search_datetime= models.DateTimeField(null=True,blank=True)#3
    ghi_chu= models.CharField(max_length=400,null=True,blank=True)#3

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    ca_truc= models.ForeignKey(CaTruc,null=True,)
    so_dien_thoai = models.CharField(max_length=20)
    #config_ca_filter_in_mll_table = models.ManyToManyField(CaTruc,related_name='userprofile_ca_filter',blank=True,null=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    def __unicode__(self):
        return self.user.username


from django.db.models import CharField
H_Field = [f.name for f in SearchHistory._meta.fields if isinstance(f, CharField) ]
