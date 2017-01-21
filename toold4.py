# -*- coding: utf-8 -*- 
import re
import datetime
import os


SETTINGS_DIR = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(SETTINGS_DIR, 'media')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnDriving.settings')


from rnoc.models import DoiTac, SLASH_DISTINCTION
#from LearnDriving.settings import MYD4_LOOKED_FIELD

def luu_doi_tac_toold4(doi_tac_inputext,user_tao=None,is_save_doitac_if_not_exit=False):
            if SLASH_DISTINCTION not in doi_tac_inputext:
                dictx = {'Name':doi_tac_inputext}
            else: # if has - 
                fieldnames= ['Name','Don_vi','So_dien_thoai']
                doi_tac_inputexts = doi_tac_inputext.split(SLASH_DISTINCTION)
                doi_tac_inputexts = [x.lstrip().rstrip() for x in doi_tac_inputexts ]
                sdt_fieldname = fieldnames.pop(2)# sdt_fieldname =sdt_fieldname
                p = re.compile(r'\d[\d\s]{3,}') #digit hoac space lon hon 3 kytu lien tiep
                kq= p.search(doi_tac_inputext)
                try:
                    phone_number_index_of_ = kq.start()
                    index_of_sdt_in_list = len(re.findall(SLASH_DISTINCTION,doi_tac_inputext[:phone_number_index_of_]))# jush count bao nhieu dau * truoc so dien thoai
                    fieldnames.insert(index_of_sdt_in_list, 'So_dien_thoai')
                except AttributeError:#'NoneType' object has no attribute 'start'
                    pass
                dictx = dict(zip(fieldnames,doi_tac_inputexts))
            doitacs = DoiTac.objects.filter(**dictx)
            if len(doitacs)==0:
                if is_save_doitac_if_not_exit:
                    dictx.update({'nguoi_tao':user_tao})
                    doitac = DoiTac(**dictx)
                    doitac.save()
                    return doitac
                else:
                    return None
            else:
                return doitacs[0]


def create_dict_d41(contains,fieldnames):
    dict ={}
    for contain in contains:
        contain = contain.lstrip().rstrip()
        for key in fieldnames:
            p = re.compile('^'+ key +'_',re.VERBOSE)
            kq = p.subn('',contain)
            #print kq[1]
            if kq[1]:
                #print key,contain.replace(key+'_','')
                #print key,p.subn('',contain)
                dict[fieldnames[key]] = kq[0]
                continue
        if kq[1]==0:
            dict["all field"] = contain
                
    print dict
    return dict
def recognize_fieldname_of_query(contain,fieldnames):
    #Chuc nang: nhận dạng search theo kiểu: 2g=hc1001 hoac site_Site_ID_2G = hc1001
    is_negative_query = False
    contain = contain.lstrip().rstrip()
    p = re.compile('^'+ '(.*?)' +'=(.*?)$',re.IGNORECASE)
    kq = p.findall(contain)
    if kq:
        fieldname = kq[0][0].lstrip().rstrip().replace(" ","_")
        for longfield,sortfield in fieldnames.items():
            if fieldname.lower()==sortfield.lower():
                fieldname = longfield
                break
        contain = kq[0][1].lstrip().rstrip()
    else:
        fieldname = "all field"
    if contain and contain[0]=='!':
        contain = contain[1:]
        is_negative_query = True
    else:
        is_negative_query = False
    return (fieldname,contain,is_negative_query)
def create_a_list_from_row_string(stringss):
    outs = stringss.split('\n')
    out_put = u','.join(['"' + x +'"' for x in outs if len(x)>1])
    return out_put
    
def prepare_value_for_specificProblem(specific_problem_instance):
    return ((specific_problem_instance.fault.Name + '**') if specific_problem_instance.fault else '') + ((specific_problem_instance.object_name) if specific_problem_instance.object_name else '')
    
if __name__=="__main__":
    inputa = '''oanh-duong
letam
thaole
hainguyen
le-duc-hung
nguyenminhtrang
lambui
chinhle
Tham
huyen
le-son-ha
jenny
hien
nhandohoang
nicolasnguyenvan
sanbui
 
'''
    print create_a_list_from_row_string(inputa) 
    
