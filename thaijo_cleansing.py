
import pandas as pd
import regex as re
import string as str
def replace_rank(string):
    list = '''ทหารบก 	 	 	 
พลเอก
พล.อ.
GEN
พลโท
พล.ท.
LT GEN
พลตรี
พล.ต.
MAJ GEN
พันเอก
พ.อ.
COL
พันโท
พ.ท.
LT COL
พันตรี
พ.ต.
MAJ
ร้อยเอก
ร.อ.
CAPT
ร้อยโท
ร.ท.
LT
ร้อยตรี
ร.ต.
SUB LT
จ่าสิบเอก
จ.ส.อ.
S M 1
จ่าสิบโท
จ.ส.ท.
S M 2
จ่าสิบตรี
จ.ส.ต.
S M 3
สิบเอก
ส.อ.
SGT
สิบโท
ส.ท.
CPL
สิบตรี
ส.ต.
PFC
พลทหาร
พลฯ
PVT
ทหารเรือ	 	 	 	 	 
พลเรือเอก
พล.ร.อ.
ADM
พลเรือโท
พล.ร.ท.
V ADM
พลเรือตรี
พล.ร.ต.
R ADM
นาวาเอก
น.อ. ...ร.น.
CAPT
นาวาโท
น.ท. ...ร.น.
CDR
นาวาตรี
น.ต. ...ร.น.
L CDR
เรือเอก
ร.อ. ...ร.น.
LT
เรือโท
ร.ท. ...ร.น.
LT JG
เรือตรี
ร.ต. ...ร.น.
SUB LT
พันจ่าเอก
พ.จ.อ.
CPO 1
พันจ่าโท
พ.จ.ท.
CPO 2
พันจ่าตรี
พ.จ.ต.
CPO 3
จ่าเอก
จ.อ.
PO 1
จ่าโท
จ.ท.
PO 2
จ่าตรี
จ.ต.
PO 3
พลทหาร
พลฯ
SEA-MAN
ทหารอากาศ	 	 	 	 	 
พลอากาศเอก
พล.อ.อ.
ACM
พลอากาศโท
พล.อ.ท.
AM
พลอากาศตรี
พล.อ.ต.
AVM
นาวาอากาศเอก
น.อ.
GP CAPT
นาวาอากาศโท
น.ท.
WG CDR
นาวาอากาศตรี
น.ต.
SQN LDR
เรืออากาศเอก
ร.อ.
FLT LT
เรืออากาศโท
ร.ท.
FLG OFF
เรืออากาศตรี
ร.ต.
PLT OFF
พันจ่าอากาศเอก
พ.อ.อ.
FS 1
พันจ่าอากาศโท
พ.อ.ท.
FS 2
พันจ่าอากาศตรี
พ.อ.ต.
FS 3
จ่าอากาศเอก
จ.อ.
SGT
จ่าอากาศโท
จ.ท.
CPL
จ่าอากาศตรี
จ.ต.
LAC
พลทหาร
พลฯ
AMN
ตำรวจ	 	 	 	 	 
พลตำรวจเอก
พล.ต.อ.
POL GEN
พลตำรวจโท
พล.ต.ท.
POL LT GEN
พลตำรวจตรี
พล.ต.ต.
POL MAJ GEN
พันตำรวจเอก
พ.ต.อ.
POL COL
พันตำรวจโท
พ.ต.ท.
POL LT COL
พันตำรวจตรี
พ.ต.ต.
POL MAJ
ร้อยตำรวจเอก
ร.ต.อ.
POL CAPT
ร้อยตำรวจโท
ร.ต.ท.
POL LT
ร้อยตำรวจตรี
ร.ต.ต.
POL SUB LT
นายดาบตำรวจ
ด.ต.
POL SEN SGT MAJ
จ่าสิบตำรวจ
จ.ส.ต.
POL SGT MAJ
สิบตำรวจเอก
ส.ต.อ.
POL SGT
สิบตำรวจโท
ส.ต.ท.
POL CPL
สิบตำรวจตรี
ส.ต.ต.
POL L/C
พลตำรวจ
พลฯ
POL CONST
อื่น ๆ
นาย
-
MR
นาง
-
MRS
นางสาว
-
MISS
บาทหลวง
-
REV
หม่อมหลวง
ม.ล.
M L
หม่อมราชวงศ์
ม.ร.ว.
M R
Dr
Authors :'''.split("\n")
    list2='''สามเณร
-
SAMANERA
-
พระอธิการ
-
PHRA ATHIKAN
เจ้าอธิการ
-
CHAO ATHIKAN
พระปลัด
-
PHRAPALAD
พระสมุห์
-
PHRASAMU
พระใบฎีกา
-
PHRABAIDIKA
พระครูปลัด
-
PHRAKHU PALAD
พระครูสมุห์
-
PHRAKHU SAMU
พระครูใบฎีกา
-
PHRAKHU BAIDIKA
พระมหา
-
PHRAMAHA
พระครูธรรมธร
-
PHRAKHU DHAMMADHORN
พระครูวินัยธร
-
PHRAKHU VINAIDHORN
PHRAKHRU
พระครู
พระ
-
PHRA
'''.split("\n")
    list3='''ดอกเตอร์	ดร.
เด็กชาย ด.ช.
เด็กหญิง	ด.ญ.
ทันตแพทย์	ทพ.
ทันตแพทย์หญิง	ทพญ.
เทคนิคการแพทย์	ทนพ.
เทคนิคการแพทย์หญิง	ทนพญ.
นางสาว	น.ส.
นายแพทย์	นพ.
นายสัตวแพทย์	นสพ. (ผู้จบปริญญา)
ผู้ช่วยศาสตราจารย์	ผศ.
แพทย์หญิง	พญ.
เภสัชกร	ภก.
เภสัชกรหญิง	ภกญ.
รองศาสตราจารย์	รศ.
ศาสตราจารย์	ศ.
ศาสตราจารย์เกียรติคุณ	ศ.
ศาสตราจารย์พิเศษ	ศ.
สัตวแพทย์	สพ. (ผู้จบการศึกษาระดับประกาศนียบัตร ทั้งชายและหญิง)
สัตวแพทย์หญิง	สพญ. (ผู้จบปริญญา)
สารวัตรใหญ่	สวญ.
เสนาธิการ	เสธ.
หม่อมเจ้า	ม.จ.
หม่อมราชวงศ์	ม.ร.ว.
หม่อมหลวง	ม.ล.'''.split("\n")
    check =0
    for i in list:
        if i!='-' and i!=' ':
            string =string.replace(i.title(),"")
    for i in list2:
        if i!='-' and i!=' ' and i.title() in string:
            string =string.replace(i.title(),"")
            check=1
    for i in list3:
        for y in i.split():
            string=string.replace(y,"")
    

    return [string,check]

def check_space(string):
    check=0
    for i in string:
        if((i>="A" and i<="Z") or(i>="a" and i<="z")):
            check=1
            break
        elif(i>="ก" and i<="ฮ"):
            check=2
            break
    if(check):
        return 1 #thai and eng
    else:
        return 0 #others

def spliteng(string):
    eng=[]
    thai=[]
    check=0 #1=eng 2=thai
    for x in string.split(' '):

        for letter in x:
            if(letter>='A' and letter<='Z' or letter>='a' and letter<='z'):
                check=1
                break
            elif(letter>='ก' and letter <='ฮ'):
                check=2
                break
        
        if check==1:
            
            eng.append(x)
        elif check==2:
            thai.append(x)
    
    eng=' '.join(eng)
    thai= ' '.join(thai)
    string =thai+';'+eng
    return string

def spaces_remover(string):
    lst= str.punctuation 
    for i in lst:
        string = string.lstrip(i)
        string = string.rstrip(i)
    return string

def remove_spaces(string):

    if string == '':
        return ''
    elif string == ' ':
        return ''
    if string[0] == ' ':
        string = string[1:]
    if string[-1] == ' ':
        string = string[:-1]
    check=0
    check =check_space(string)
    
    if(check):
        check =0 
        string,check= replace_rank(string)

        
        string  = spliteng(string)
        
        string = spaces_remover(string)

        return string
    else:
        return string

def clear_samename(names):
    namesx=[]
    for i in names:
        namesx.extend(i.split(';'))
    namesx = [spaces_remover(x) for x in namesx]
    names=[]
    for i in namesx:
        if(i not in names):
            names.append(i)
    names = [x for x in names if x!='']
    names=[x.replace("(",'') for x in names]
    names=[x.replace(")",'') for x in names]
    print(names)

    return names

if __name__ == '__main__':
    char = {'id': [], 'name': []}
    df = pd.read_csv('test.csv')
    df = df.fillna('')
    for idx, row in df.iterrows():
        names = []
        char['id'].extend([f"{row['_id']}_{i+1}" for i in range(10)])
        author = row['_source.author']
        if author != '':
            names.append(author)
        co_author = row['_source.co-author']
        if co_author != '':
            ca = co_author.split(',')
            for c in ca:
                if c not in names:
                    names.append(c)
        if len(names) == 0:
            char['name'].extend([None]*10)
            continue
        names = [remove_spaces(name) for name in names]
        
        names = clear_samename(names)
        #print(names)
        if len(names) > 10:
            names = names[:10]
        elif len(names) < 10:
            names.extend(['']*(10-len(names)))
        char['name'].extend(names)
    char = pd.DataFrame(char)
    char.to_csv('sample_submission.csv', index=False)
