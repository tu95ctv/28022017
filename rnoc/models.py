# -*- coding: utf-8 -*-
##for test github1
from datetime import datetime
from django.utils import timezone
from filebrowser.fields import FileBrowseField
#from ckeditor.fields import RichTextField
print 'in model 2'
from django.db import models
from django.contrib.auth.models import User
from tinymce_4.fields import TinyMCEModelField

        ##OMCKV2
SLASH_DISTINCTION = u'/'
class IPAddress_FieldNullable(models.GenericIPAddressField):
    def get_db_prep_save(self,value,connection,prepared=False):
        return value or None   
class EditHistory(models.Model):
    modal_name = models.CharField(max_length=50)
    edited_object_id = models.IntegerField()
    thanh_vien = models.ForeignKey(User,null=True,blank=True,verbose_name=u"Thành viên sửa")
    ly_do_sua = models.CharField(max_length=250,null=True,blank=True)
    edit_datetime= models.DateTimeField(null=True,blank=True)#3
    
class BTSType(models.Model):
    Name = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.Name 
class Brand(models.Model):
    Name = models.CharField(max_length = 130,unique = True)
    def __unicode__(self):
        return self.Name
  
class ThietBi(models.Model):
    Name = models.CharField(max_length=120,unique = True)
    brand = models.ForeignKey(Brand,null=True,blank=True)
    bts_type = models.ForeignKey(BTSType,null=True,blank=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi chú')#3
    color_code = models.CharField(max_length=15,null=True,blank=True)
    is_duoc_tao_truoc = models.BooleanField(verbose_name=u"Không cho phép sửa field Name")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_thietbi_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_thietbi_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        #brand_text = '' if self.brand ==None else SLASH_DISTINCTION + 'Brand:' + self.brand.Name
        brand_text = SLASH_DISTINCTION + 'None' if self.brand ==None else SLASH_DISTINCTION + self.brand.Name
        #bts_type_text = '' if self.bts_type ==None else SLASH_DISTINCTION + 'Type:' + self.bts_type.Name
        bts_type_text = SLASH_DISTINCTION + 'None' if self.bts_type ==None else SLASH_DISTINCTION  + self.bts_type.Name
        return self.Name + brand_text + bts_type_text
        
    
class Component(models.Model):
    Name = models.CharField(max_length=20,unique = True)
    Name_khong_dau = models.CharField(max_length=150,null=True)
    thiet_bi_of_component = models.ForeignKey(ThietBi,null=True,blank=True,verbose_name = u'Thiết bị')
    ghi_chu = models.CharField(max_length=500,null=True,blank=True)#3
    color_code = models.CharField(max_length=15,null=True,blank=True)
    is_duoc_tao_truoc = models.BooleanField(default = False,verbose_name=u"Không cho phép sửa field Name")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_component_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_component_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    picture =  models.CharField(max_length=200,null=True,blank=True)
    def __unicode__(self):
        thiet_bi = getattr(self, 'thiet_bi_of_component')
        return self.Name + ((SLASH_DISTINCTION + thiet_bi.Name) if thiet_bi else '')
class DoiTac(models.Model):#khong co color code
    #First_name = models.CharField(max_length=20,null=True,blank=True)
    Name = models.CharField(max_length=80)
    Name_khong_dau = models.CharField(max_length=80,null=True,blank=True)
    Don_vi  = models.CharField(max_length=80,null=True,blank=True,verbose_name = u'Đơn Vị')
    So_dien_thoai  = models.CharField(max_length=80,null=True,blank=True,verbose_name = u'Số điện thoại')
    Nam_sinh  = models.CharField(max_length=80,null=True,blank=True,verbose_name = u'Năm Sinh')
    email = models.CharField(max_length=80,null=True,blank=True)
    ghi_chu  = models.CharField(max_length=80,null=True,blank=True,verbose_name = u'Ghi chú')
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_doitac_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_doitac_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    
    def __unicode__(self):
        return self.Name  + (SLASH_DISTINCTION + self.Don_vi if self.Don_vi else "") + (SLASH_DISTINCTION+ self.So_dien_thoai if self.So_dien_thoai else "")
class DuAn(models.Model):
    Name=models.CharField(max_length=150)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú'   ) 
    #ghi_chu = RichTextField(max_length=1330,null=True,blank=True)
    type_2G_or_3G = models.CharField(max_length=2,blank=True,null=True)
    thoi_diem_bat_dau= models.DateTimeField(null=True,blank=True,verbose_name=u"thời điểm bắt đầu")#3
    thoi_diem_ket_thuc= models.DateTimeField(null=True,blank=True,verbose_name=u"thời điểm kết thúc")#3
    doi_tac_du_an = models.ManyToManyField(DoiTac,blank=True,verbose_name = u'Đối tác dự án')
    is_duoc_tao_truoc = models.BooleanField(default = False,verbose_name=u"Không cho phép sửa field Name")
    #default = User.objects.get(username = "tund").id
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_duan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_duan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
    
class SiteType(models.Model):
    Name = models.CharField(max_length=150,unique=True)
    def __unicode__(self):
        return self.Name
class SuCo (models.Model):
    Name = models.CharField(max_length=150,unique=True)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú'   ) 
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_nguyennhan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_nguyennhan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=timezone.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    
    def __unicode__(self):
        return self.Name
class NguyenNhan (models.Model):
    Name = models.CharField(max_length=150,unique=True)
    Name_khong_dau = models.CharField(max_length=150,null=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú') 
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_NguyenNhan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_NguyenNhan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=timezone.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    
    def __unicode__(self):
        return self.Name
class CaTruc(models.Model):
    Name = models.CharField(max_length=30,unique=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    is_duoc_tao_truoc = models.BooleanField(default=False,verbose_name = u"Không cho phép sửa field Name")
    #nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_trangthai_set',blank=True)
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_catruc_set',blank=True,verbose_name=u"người sửa cuối cùng")
    #ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    
    
    def __unicode__(self):
        return self.Name
class TrangThai(models.Model):
    Name = models.CharField(max_length=100,unique=True)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    #ghi_chu = models.CharField(max_length=500,null=True,blank=True)
    ghi_chu = TinyMCEModelField(null=True,blank=True,verbose_name = u'Ghi Chú')
    #image = FileBrowseField(u"Featured Image", null=True,max_length=400, directory='posts/', extensions=['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff'])
    #stylecss_name = models.CharField(max_length=100,null=True,blank=True)
    color_code = models.CharField(max_length=15,null=True,blank=True)
    is_cap_nhap_gio_tot =models.BooleanField(verbose_name = u'Trạng thái này có tự cập nhập giờ tốt không ?',default = False)
    is_duoc_tao_truoc = models.BooleanField(default = False,verbose_name=u"Không cho phép sửa field Name")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_trangthai_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_trangthai_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
class ThaoTacLienQuan(models.Model):
    Name = models.CharField(unique=True,max_length=100)
    Name_khong_dau = models.CharField(max_length=80,null=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    Name_khong_dau = models.CharField(max_length=100,null=True)
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_ThaoTacLienQuan_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_ThaoTacLienQuan_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
class FaultLibrary(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    diversity = models.CharField(max_length=10,blank=True,null=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_FaultLibrary_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_FaultLibrary_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
class Lenh(models.Model):
    command= models.CharField(max_length=500)#3
    Name= models.CharField(max_length=200,unique=True)#3
    Name_khong_dau = models.CharField(max_length=80,null=True,blank=True)
    thiet_bi= models.ForeignKey(ThietBi,null=True,blank = True,verbose_name=u"Thiết bị")#12
    ghi_chu_lenh= models.CharField(max_length=200,null=True,blank=True,verbose_name=u"Ghi chú")#3
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_Lenh_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_Lenh_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    
    def __unicode__(self):
        return self.command
    
class DiaBan(models.Model):
    Name= models.CharField(max_length=50,unique=True)#3
    Name_khong_dau = models.CharField(max_length=50,blank=True,unique=True)
    ky_hieu = models.CharField(max_length=50)#3
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    so_luong_tram_2G = models.IntegerField(null=True,blank=True)
    so_luong_tram_3G = models.IntegerField(null = True,blank=True)
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_diaban_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
    
    
class Tinh(models.Model):
    Name= models.CharField(max_length=50,unique=True)#3
    Name_khong_dau = models.CharField(max_length=50,blank=True,unique=True,verbose_name = u'Name không dấu')
    #dia_ban = models.CharField(max_length=50)
    dia_ban = models.ForeignKey(DiaBan,null=True,verbose_name = u'Địa Bàn')
    ma_tinh = models.CharField(max_length=4,unique=True,verbose_name = u'Mã Tỉnh')
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    so_luong_tram_2G = models.IntegerField(null=True,blank=True,verbose_name = u'Số lượng trạm 2G')
    so_luong_tram_3G = models.IntegerField(null = True,blank=True,verbose_name = u'Số lượng trạm 3G')
    tong_so_tram = models.IntegerField(null = True,blank=True,verbose_name = u'Tổng số lượng trạm')
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_Tinh_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
    
   
class MSC(models.Model):
    Name = models.CharField(max_length=50)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name=u'Ghi chú')    
    msc_or_sgsn = models.CharField(max_length=20,null=True,blank=True,verbose_name=u'MSC hay SGSN')
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_MSC_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_MSC_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name
class BSCRNC(models.Model):
    Name = models.CharField(max_length=50,unique=True)
    HANG_SX = models.CharField(max_length=20,null=True,blank=True)
    DIA_CHI = models.CharField(max_length=200,null=True,blank=True)
    DIEN_THOAI = models.CharField(max_length=20,null=True,blank=True)
    VI_TRI_RNC = models.ForeignKey(Tinh,null=True,blank=True)
    TINH_RNC_QUAN_LY=models.CharField(max_length=50,null=True,blank=True)
    brand = models.ForeignKey(Brand,null=True,blank=True)
    bsc_or_rnc = models.CharField(max_length=50,)
    
    SGSN = models.ForeignKey(MSC,null=True,related_name = 'msc_dot_sgsn_set',blank=True)
    MSC = models.ForeignKey(MSC,related_name = 'msc_dot_msc_set',null=True,blank=True,verbose_name=u'MSC')
    so_luong_tram = models.IntegerField(null = True,blank=True)
    ghi_chu = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_BSCRNC_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_BSCRNC_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        return self.Name 
class QuanHuyen(models.Model):
    Name = models.CharField(max_length=80)
    tinh = models.ForeignKey(Tinh,related_name='Tinh_dot_quan_huyen_sets')
    def __unicode__(self):
        return self.Name +'-'+self.tinh.Name
class PhuongXa(models.Model):
    Name = models.CharField(max_length=80)
    tinh = models.ForeignKey(Tinh,related_name='Tinh_dot_phuong_xa_sets')
    quan_huyen = models.ForeignKey(QuanHuyen,related_name='Quan_huyen_dot_phuong_xa_sets')
    def __unicode__(self):
        return self.Name +'-'+self.tinh.Name + '-'+self.tinh.Name
class UPE(models.Model):
    Name = models.CharField(max_length=80)
    tinh = models.ForeignKey(Tinh,related_name='Tinh_dot_UPE_sets')
    def __unicode__(self):
        return self.Name +'-'+self.tinh.Name
class TanSo2G(models.Model):
    Name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Name
class TanSo3G(models.Model):
    Name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.Name

class CauHinh(models.Model):
    Name = models.CharField(max_length = 50,unique=True,)
    ghi_chu = models.CharField(max_length=300,null=True,blank=True,verbose_name = u'Ghi Chú' )
    def __unicode__(self):
        return self.Name
class Tram(models.Model):
    #Chung
    nha_tram = models.ForeignKey("NhaTram",null=True,blank=True)
    Site_Name_1= models.CharField(max_length=80,unique=True)
    Site_Name_2= models.CharField(max_length=80,null=True,blank = True)
    Site_type = models.ForeignKey(SiteType,blank=True)
    ghi_chu_tram = models.CharField(max_length=500,null=True,blank=True,verbose_name = u'Ghi Chú')
    import_ghi_chu = models.CharField(max_length=400,null=True,blank = True,verbose_name = u'Ghi Chú import')#24
    dia_chi_3G = models.CharField(max_length=200,null=True,blank = True,verbose_name =u"Địa chỉ 3G")#35
    tinh = models.ForeignKey(Tinh,null=True,blank=True,verbose_name = u'Tỉnh',related_name = 'tinh_dot_tram_set')
    quan_huyen = models.ForeignKey(QuanHuyen,null=True,blank = True,verbose_name = u'Quận huyện')
    phuong_xa = models.ForeignKey(PhuongXa,null=True,blank = True,verbose_name = u'Phường Xã')
    Nha_Tram = models.CharField(max_length=20,null=True,blank = True,verbose_name = u"Nhà Trạm")#35
    Ma_Tram_DHTT = models.CharField(max_length=20,null=True,blank = True,verbose_name = u'Mã trạm ĐHTT')#35
    dia_chi_3G_khong_dau = models.CharField(max_length=200,null=True,blank = True,verbose_name =u"Địa chỉ 3G khong dau")#35
    dia_chi_2G = models.CharField(max_length=200,null=True,blank = True,verbose_name =u"Địa chỉ 2G")#35
    dia_chi_2G_khong_dau = models.CharField(max_length=200,null=True,blank = True,verbose_name =u"Địa chỉ 2G khong dau")#35
    macro_or_ibs = models.CharField(max_length=10,null=True,blank = True)#35
    #booster
    booster = models.CharField(max_length=80,null=True,blank = True)
    #2G
    Ngay_Phat_Song_2G = models.DateField(null=True,blank = True,verbose_name=u"Ngày phát sóng 2G")#5
    BSC_2G = models.ForeignKey(BSCRNC,null=True,blank = True,related_name='bscrnc_dot_Tram_BSC_2G_set')#35
    cau_hinh_2G = models.ForeignKey(CauHinh,related_name ='Tram_cau_hinh_2G',null=True,blank = True,verbose_name = u"Cấu hình 2G")#35
    cau_hinh_3G = models.ForeignKey(CauHinh,related_name ='Tram_cau_hinh_3G',null=True,blank = True,verbose_name = u"Cấu hình 3G")#35
    nha_san_xuat_2G = models.ForeignKey(ThietBi,null=True,blank = True,verbose_name = u'Thiết bị 2G')#35
    Site_ID_2G = models.CharField(max_length=80,null=True,blank = True)#35
    Site_ID_2G_Number = models.CharField(max_length=100,null=True,blank = True,)#35
    LAC_2G = models.CharField(max_length=20,null=True,blank = True,)#35
    Cell_ID_2G = models.CharField(max_length=220,null=True,blank = True,)#35
    Long_2G = models.CharField(max_length=30,null=True,blank = True,)#35
    Lat_2G = models.CharField(max_length=30,null=True,blank = True,)#35
    tan_so_2G = models.ForeignKey(TanSo2G,null=True,blank = True)
    brand_2G = models.ForeignKey(Brand,null=True,blank = True)
    active_2G = models.BooleanField(default = False,verbose_name =  u"Đang Active 2G")
    TRX_DEF = models.CharField(max_length=50,null=True,blank = True,)#35
    TG_Text = models.CharField(max_length=150,null=True,blank = True,)#35
    TG = models.CharField(max_length=3,null=True,blank = True)#35
    TG_1800 = models.CharField(max_length=3,null=True,blank = True,)#35
    #4G
    IUB_VLAN_ID_4G = models.CharField(max_length=4,null=True,blank = True)#15
    IUB_SUBNET_PREFIX_4G = models.CharField(max_length=40,null=True,blank = True,)#16
    IUB_DEFAULT_ROUTER_4G = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#17
    IUB_HOST_IP_4G = IPAddress_FieldNullable(null=True,blank = True)#18
    MUB_VLAN_ID_4G = models.CharField(max_length=4,null=True,blank = True)#19
    MUB_SUBNET_PREFIX_4G = models.CharField(max_length=40,null=True,blank = True,)#20
    MUB_DEFAULT_ROUTER_4G = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#21
    MUB_HOST_IP_4G = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#22
    active_4G = models.BooleanField(default = False,verbose_name =  u"Đang Active 4G")
    brand_4G = models.ForeignKey(Brand,null=True,blank = True,related_name = 'brand_4g_set_dot_tram')
    eNodeB_Name = models.CharField(max_length=40,null=True,blank = True,)#35
    eNodeB_ID_DEC = models.CharField(max_length=6,null=True,blank = True)
    eNodeB_Type = models.ForeignKey(ThietBi,null=True,blank = True,related_name='ThietBi_of_eNodeB')#12
    #3G
    tan_so_3G = models.ForeignKey(TanSo3G,null=True,blank = True)
    License_60W_Power = models.NullBooleanField(blank = True) #1
    U900 = models.NullBooleanField(blank = True,null=True)#2
    Site_ID_3G = models.CharField(max_length=80,null=True,blank = True)#3
    Ngay_Phat_Song_3G = models.DateField(null=True,blank = True,verbose_name=u"Ngày phát sóng 3G")#8
    Status = models.CharField(max_length=50,null=True,blank = True,)#10
    Project_Text = models.CharField(max_length=100,null=True,blank = True,)#10
    Trans= models.CharField(max_length=40,null=True,blank = True,)#11
    Cabinet = models.ForeignKey(ThietBi,null=True,blank = True,related_name="Tramcuathietbis",verbose_name = u'Thiết bị 3G')#12
    Port = models.CharField(max_length=40,null=True,blank = True,)#13
    RNC = models.ForeignKey(BSCRNC,null=True,blank = True)#14
    IUB_VLAN_ID = models.CharField(max_length=4,null=True,blank = True)#15
    IUB_SUBNET_PREFIX = IPAddress_FieldNullable(max_length=40,null=True,blank = True,)#16
    IUB_DEFAULT_ROUTER = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#17
    IUB_HOST_IP = IPAddress_FieldNullable(null=True,blank = True)#18
    MUB_VLAN_ID = models.CharField(max_length=4,null=True,blank = True)#19
    MUB_SUBNET_PREFIX = IPAddress_FieldNullable(max_length=40,null=True,blank = True,)#20
    MUB_DEFAULT_ROUTER = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#21
    MUB_HOST_IP = IPAddress_FieldNullable(max_length=40,null=True,blank = True)#22
    UPE = models.ForeignKey(UPE,null=True,blank = True,)#23
    Cell_1_Site_remote = models.CharField(max_length=40,null=True,blank = True,verbose_name ="Cell_1")#27
    Cell_2_Site_remote = models.CharField(max_length=40,null=True,blank = True,verbose_name ="Cell_2")#28
    Cell_3_Site_remote = models.CharField(max_length=40,null=True,blank = True,verbose_name ="Cell_3")#29
    Cell_4_Site_remote = models.CharField(max_length=40,null=True,blank = True,verbose_name ="Cell_4")#30
    Cell_5_Site_remote = models.CharField(max_length=40,null=True,blank = True,verbose_name ="Cell_5")#31
    Cell_6_Site_remote = models.CharField(max_length=40,null=True,blank = True,verbose_name ="Cell_6")#32
    Cell_7_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#33
    Cell_8_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#34
    Cell_9_Site_remote = models.CharField(max_length=40,null=True,blank = True,)#35
    Cell_K_U900_PSI =  models.CharField(max_length=40,null=True,blank = True,)#35
    Cell_ID_3G = models.CharField(max_length=220,null=True,blank = True,)#35
    LAC_3G = models.CharField(max_length=10,null=True,blank = True,)#35
    Long_3G = models.CharField(max_length=30,null=True,blank = True,)#35
    Lat_3G = models.CharField(max_length=30,null=True,blank = True,)#35
    brand_3G = models.ForeignKey(Brand,null=True,blank = True,related_name = 'brand_3g_set_dot_tram')
    ntpServerIpAddressPrimary = models.CharField(max_length=20,null=True,blank = True,)
    ntpServerIpAddressSecondary = models.CharField(max_length=20,null=True,blank = True,)
    ntpServerIpAddress1 = models.CharField(max_length=20,null=True,blank = True,)
    ntpServerIpAddress2 = models.CharField(max_length=20,null=True,blank = True,)
    du_an = models.ManyToManyField(DuAn,blank=True,verbose_name =u"Dự án")
    is_co_U900_rieng = models.NullBooleanField(blank = True,default=False,verbose_name = u'Site 3G U2100 có Site U900 riêng')
    is_co_U2100_rieng = models.NullBooleanField(blank = True,default=False,verbose_name = u'Site 3G U900 có Site U2100 riêng')
    active_3G = models.BooleanField(default = False,verbose_name =  u"Đang Active 3G")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_tram_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_tram_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=timezone.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,blank=True,verbose_name=u"Lý do sửa",null=True)
    def __unicode__(self):
        if self.Site_Name_1:
            return self.Site_Name_1
        else:
            return str(self.id)
        
class NhaTram(models.Model):
    Name = models.CharField(max_length=80,unique = True)
    tram_3g1 = models.ForeignKey(Tram,null=True,blank=True,related_name='Nhatramdottram_3g1')
    tram_3g2 = models.ForeignKey(Tram,null=True,blank=True,related_name='Nhatramdottram_3g2')
    tram_2g1 = models.ForeignKey(Tram,null=True,blank=True,related_name='Nhatramdottram_2g1')
    tram_2g2 = models.ForeignKey(Tram,null=True,blank=True,related_name='Nhatramdottram_2g2')
    
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_nhatram_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_nhatram_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    def __unicode__(self):
        return self.Name
    
class Mll(models.Model):
    object= models.CharField(max_length=50,verbose_name = u'Đối tượng')
    site_name= models.CharField(max_length=50,null=True,blank=True,verbose_name=u"Site name")#3
    thiet_bi= models.ForeignKey(ThietBi,null=True,blank = True,verbose_name=u"Thiết bị")#12
    su_co = models.ForeignKey(SuCo,related_name="Mlls",null=True,blank=True,verbose_name=u"Sự cố/Event/Công Việc")
    nguyen_nhan = models.ForeignKey(NguyenNhan,related_name="mll_set_of_NguyenNhan",null=True,blank=True,verbose_name=u"Nguyên nhân chung")
    nguyen_nhan_cu_the= models.CharField(max_length=500,verbose_name = u'Nguyên nhân cụ thể',null=True,blank = True)
    du_an = models.ForeignKey(DuAn,related_name="DuAns",null=True,blank=True,verbose_name=u"Dự án")
    ung_cuu = models.BooleanField(verbose_name=u"ư/c",default = False)
    ca_truc = models.ForeignKey(CaTruc,blank=True,null=True,verbose_name=u"Ca trực")
    gio_mat= models.DateTimeField(blank=True,verbose_name=u"Giờ mất")#3
    gio_tot= models.DateTimeField(null=True,blank=True,verbose_name=u"Giờ tốt")#3
    trang_thai = models.ForeignKey(TrangThai,null=True,blank=True,verbose_name=u"Trạng thái")
    chap_chon = models.BooleanField(verbose_name=u"Chập chờn",default = False,blank=True)
    giao_ca = models.BooleanField(verbose_name=u"g/ca",default = False)
    #nghiem_trong = models.BooleanField(verbose_name=u"N/trọng",default = False)
    brand = models.ForeignKey(Brand,null=True,blank=True,verbose_name=u"Brand") 
    type_2g_or_3g = models.ForeignKey(BTSType,null=True,blank=True,verbose_name=u"2G or 3G") 
    nghiem_trong = models.IntegerField(verbose_name=u"N/trọng",null=True,blank=True)
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_mlll_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_mll_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(null=True,verbose_name=u"Ngày giờ sửa cuối cùng",blank=True)#3
    ngay_gio_comment_cuoi_cung= models.DateTimeField(null=True,verbose_name=u"Ngày giờ comment cuối cùng",blank=True)#3
    ly_do_sua= models.CharField(max_length=100,null=True,blank=True,verbose_name=u"Lý do sửa")
    def __unicode__(self):
        return self.object

class BCNOSS(models.Model):
    object= models.CharField(max_length=50,verbose_name = u'Đối tượng')
    gio_mat= models.DateTimeField(verbose_name=u"Giờ mất")#3
    gio_tot= models.DateTimeField(null=True,blank=True,verbose_name=u"giờ tốt")#3
    code_loi = models.IntegerField()
    vnp_comment = models.CharField(max_length = 500)
    gio_canh_bao_ac= models.DateTimeField(blank=True,null=True,verbose_name=u"giờ canh bao AC")#3
    BSC_or_RNC = models.ForeignKey(BSCRNC,null=True,blank=True)
    BTS_Type = models.ForeignKey(BTSType,null=True,blank = True,verbose_name = u"2G,3G or 4G")
    BTS_thiet_bi = models.ForeignKey(ThietBi,null=True,blank = True,verbose_name = u"Nhà sản xuất")
    tong_thoi_gian = models.IntegerField(null=True,blank = True,verbose_name = u"tổng thời gian")
    tinh = models.ForeignKey(Tinh,verbose_name = u"Tỉnh")
    kien_nghi_de_xuat = models.CharField(max_length = 500,null=True,blank=True,verbose_name = u"Kiến nghị đề xuất")
    is_khong_tinh_mll_keo_dai = models.BooleanField(default=False,verbose_name = u"Không Tính mll kéo dài")

class SpecificProblem(models.Model):
    fault = models.ForeignKey(FaultLibrary,null=True,blank=True)
    object_name = models.CharField(max_length=200,null=True,blank=True)
    mll = models.ForeignKey(Mll,related_name ='specific_problems')
    def __unicode__(self):
        return ((self.fault.Name  + SLASH_DISTINCTION ) if self.fault else '')  + self.object_name
    

        
class Comment(models.Model):
    
    datetime= models.DateTimeField(blank=True,verbose_name=u"nhập giờ")
    doi_tac = models.ForeignKey(DoiTac,related_name="Comments",null=True,blank=True,verbose_name=u"đối tác")
    comment= models.CharField(max_length=500,null=True,blank=True)# if bo blank=False mac dinh se la true chelp_text="add comment here",
    #comment= RichTextField(max_length=2000,null=True,blank=True)# if bo blank=False mac dinh se la true chelp_text="add comment here",
    trang_thai = models.ForeignKey(TrangThai,blank=True,verbose_name=u"Trạng thái")
    thao_tac_lien_quan = models.ManyToManyField(ThaoTacLienQuan,blank=True,verbose_name=u"Thao tác")
    lenh_lien_quan = models.ManyToManyField(Lenh,blank=True,verbose_name=u"Lệnh liên quan")
    #component = models.ForeignKey(Component,blank=True,null=True,verbose_name=u"Component liên quan")
    component_lien_quan = models.ManyToManyField(Component,blank=True,null=True,verbose_name=u"Component liên quan")
    nguoi_tao = models.ForeignKey(User,related_name='user_nguoi_tao_dot_comment_set',blank=True,verbose_name=u"Người tạo")
    nguoi_sua_cuoi_cung = models.ForeignKey(User,null=True,related_name='user_nguoi_sua_dot_comment_set',blank=True,verbose_name=u"người sửa cuối cùng")
    ngay_gio_tao= models.DateTimeField(verbose_name=u"Ngày giờ tạo",blank=True)#3
    ngay_gio_sua= models.DateTimeField(verbose_name=u"Ngày giờ sửa cuối cùng",blank=True,null=True)#3
    mll = models.ForeignKey(Mll,related_name="comments",blank=True)
    def __unicode__(self):
        return self.comment
class SearchHistory(models.Model):
    query_string= models.CharField(max_length=200,null=True,blank=True)#3
    thanh_vien = models.ForeignKey(User,null=True,blank=True)#3
    search_datetime= models.DateTimeField(null=True,blank=True)#3
    ghi_chu= models.CharField(max_length=200,null=True,blank=True)#3

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    Name = models.CharField(max_length=200)
    user = models.OneToOneField(User)
    ca_truc= models.ForeignKey(CaTruc,null=True,blank=True,verbose_name=u'Bạn đang trực ca nào?')
    so_dien_thoai = models.CharField(max_length=20,null=True,blank=True,verbose_name = u"Số điện thoại")
    color_code = models.CharField(max_length=15,null=True,blank=True,verbose_name = u"Màu hiển thị")
    khong_search_tu_dong= models.BooleanField(default = True,verbose_name = u"Không search tự động đối với table MLL")
    khong_search_tu_dong_tram= models.BooleanField(default = True,verbose_name = u"Không search tự động Trạm")
    loc_ca = models.ManyToManyField(CaTruc,related_name = "catruc_dot_userprofile_dot_set",blank = True,verbose_name=u'Bạn muốn hiên thị ca nào?')
    def __unicode__(self):
        return self.user.username

class DapAn(models.Model):
    Name = models.CharField(max_length = 500)
    is_true_or_false = models.BooleanField(default = False) 
    
class TracNghiem(models.Model):
    cau_hoi = models.CharField(unique = True,max_length = 255)
    is_multiple_choice = models.BooleanField(default = False)
    dap_an = models.ManyToManyField(DapAn)
    #dap_an = 
'''
class UserOption(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    khong_search_tu_dong= models.BooleanField()
    loc_ca = models.ManyToManyField(CaTruc)
    def __unicode__(self):
        return self.user.username

'''
   
   
from django.db.models import CharField
H_Field = [f.name for f in SearchHistory._meta.fields if isinstance(f, CharField) ]
