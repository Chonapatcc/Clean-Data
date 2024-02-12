
import pandas as pd
import regex as re
import os 

def checklang(string):
    thai_pattern = re.compile(r'[\u0E00-\u0E7F]')
    english_pattern = re.compile(r'[A-Za-z]')

    #check 
    contains_thai = bool(thai_pattern.search(string))
    contains_english = bool(english_pattern.search(string))
    return contains_thai,contains_english

def remove_parenthesis(string):
    string = string.strip("(")
    string = string.strip(")")
    return string
def replace_parenthesis(string):
    string = string.replace('(','')
    string =string.replace(')','')
    return string

def remove_spaces(string):
    string = string.strip()
    return string

def spliteng_thai(string):
    if(string.startswith('พระ') or string.startswith("Phra")):
        lst = string.split()
        emp = []
        for val in lst:
            val=remove_spaces(val)
            emp.append(val)
        string = ' '.join(emp)
        return string
    else:
        lst = string .split()

        thaif,engf = checklang(lst[0]) #first word

        thailst = []
        englst = []

        for val in lst:
            val = remove_spaces(val)
            val = remove_parenthesis(val)
            val = replace_parenthesis(val)
            langthai ,langeng = checklang(val)
            if(langthai):
                thailst.append(val)
            else:
                englst.append(val)
        string1 = ' '.join(thailst)
        string2 = ' '.join(englst)
        if(thaif):
            string = string1+";"+string2
            return string
        else:
            string = string2+";"+string1
            return string

def onlythai(string):
    emp=[]
    lst = string.split()
    ch1 =string.startswith('พระ')
    for val in lst:
        if(ch1):
            val = remove_spaces(val)
        else:
            val = remove_spaces(val)
            val = remove_parenthesis(val)
            val = replace_parenthesis(val)
        emp.append(val)
    string = ' '.join(emp)
    return string

def onlyeng(string):
    emp=[]
    lst = string.split()
    ch1 = string.startswith('Phra')
    for val in lst:
        if(ch1):
            val = remove_spaces(val)
        else:
            val = remove_spaces(val)
            val = remove_parenthesis(val)
            val = replace_parenthesis(val)
        emp.append(val)
    string = ' '.join(emp)
    return string

def replacelang(string):
    string = string.title()
    lst = "Dr.|M.R. |Prof.|Mr.|Ms.|Mrs.|นาย|นางสาว|นาง|ม.ร.ว.| ร.ต. |ทันตแพทย์หญิง|พระ|พระครู|ผู้ช่วยศาสตราจารย์|ผศ.|ดร.| ดร. |นพ.|Authors :|ว่าที่|ร.ต.|รองศาสตราจารย์ ดร.|ดร. |ผู้ช่วยศาสตราจารย์|ผู้ช่วยศาสตราจารย์ ดร.|รองศาสตราจารย์ ดร.| ดร.|อ.|อ.ดร.| พ.ต. ดร.|อาจารย์ ดร.|รศ.ดร.|รศ.ดร.| พ.ต. ดร.|พระ|พระมหา|พระครู|พระสรวิชญ์|พระครูใบฎีกา|พระครูสมุห์|พระปลัด".split("|")

    for i in lst:
        if(string.startswith(i)):
            string = string.replace(i,'')
    return string

def remove_conjunc(string):
    lst2 = re.findall(r'([!-\']|[*-/]|[:-@]|[[-`]|[{-~]|[0-9])', string)
    for i in lst2:
        string = string.strip(i)

    return string

def lang(string):
    thai,eng = checklang(string)

    if(not (thai or eng)): # other lang
        string =string
    elif (thai and eng): #both
        string=spliteng_thai(string)
        
    elif (thai):
        string=onlythai(string)
    else:
        string=onlyeng(string)
    
    string=replacelang(string)
    return string 

def deleteword(string):
    want_to_removes = [
        ';', '"', 'และคณะ', 'ผศ.', 'ดร.', 'ร.ต.อ.', 'นพ.', 'รศ.', 'dr.', 'm.r.', 'mr.', 'ม.ร.ว.',
        'ms.', 'assist.', 'prof.', 'lect.', 'asst.', 'assoc.', '(ผู้แต่ง)', 'กองบรรณาธิการ ผู้เชี่ยวชาญ',
        'กองบรรณาธิการ กองบรรณาธิการ', 'รายละเอียดบทความ วารสารวิทยาการจัดการ', 'กองบรรณาธิการ วารสาร',
        'วารสารวิชาการและวิจัยสังคมศาสตร์', 'สารบัญ วารสารวิทยาการจัดการ', 'บรรณาธิการ วารสารวิทยาการจัดการ',
        'คณะมนุษยศาสตร์ มหาวิทยาลัยรามคำแหง', 'บัณฑิตวิทยาลัย วไลยอลงกรณ์', '(', ')', '[', ']', 'authors :',
        'cover vol', 'tsme thailand', 'สารบัญ', 'ผู้ช่วยศาสตราจารย์', 'ผู้ช่วยศาสตราจารย์ ดร.', 'รองศาสตราจารย์ ดร.',
        'รองศาสตราจารย์', 'พระครู', 'พระมหา', 'พระปลัด', 'อาจารย์', 'พันเอกหญิง', 'พันเอก', 'author', 'บทบรรณาธิการ',
        'บรรณาธิการ', 'editorial', 'วารสารวิชาการและวิจัยสังคม', 'เกี่ยวกับวารสาร', 'about the journal', 'ผู้ทรงคุณวุฒิ -',
        'แนะนำผู้เขียน -', ',', '*', 'กสทช.', 'ว่าที่ พ.ต.', 'อ.', 'ศ.', 'ว่าที่ ร.ต', 'ว่าที่ร้อยตรี', 'ร้อยเอก', 'et.al', 
        'et al', 'and other', 'ศูนย์บริการโลหิตแห่งชาติ สภากาชาดไทย', 'วารสารมหาวิทยาลัยราชภัฏสกลนคร', '-- --'
    ] 
    if string in want_to_removes:
        return ""
    else:
        return string
if __name__ == '__main__':
    char = {'id': [], 'name': []}
    df = pd.read_csv('test.csv')
    df = df.fillna('')
    for idx, row in df.iterrows():
        names = []
        char['id'].extend([f"{row['_id']}_{i+1}" for i in range(10)])
        author = row['_source.author']
        author = lang(author).split(';')
        names.extend(author)

        co_author = row['_source.co-author']
        if co_author != '':
            ca = co_author.split(',')
            for c in ca:
                c=lang(c)
                if c not in names:
                    c=c.split(';')
                    names.extend(c)
        if len(names) == 0:
            char['name'].extend([None]*10)
            continue
        names0 =[]
        for name in names:
            name = remove_spaces(name)
            name = replacelang(name)
            for _ in range(10):
                name = remove_conjunc(name)
            if(name not in names0):
                names0.append(name)
        names=names0
        names = [deleteword(name) for name in names]
        if len(names) > 10:
            names = names[:10]
        elif len(names) < 10:
            names.extend(['']*(10-len(names)))
        char['name'].extend(names)
    char = pd.DataFrame(char)
    char.to_csv('sub.csv', index=False)
