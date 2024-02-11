import pandas as pd
import regex as re


def remove_spaces(string):
    if 'พระ' not in string:
        if '(' in string and ')' in string:
            string = string.replace(string[string.index('(')-1:string.index(')')+1], '')
        if '(' in string and ')' in string:
            string = string[:string.index('(')]
        #if '(' in string:
            #string = string.replace(string[string.index('('):], '').strip()
            #print(string)
        if '(' in string or ')' in string:
            string = string.replace('(', '')
            string = string.replace(')', '')
#A.A.|K.O.|E.O.|S.A.|
    if string == '':
        return ''
    elif string == ' ':
        return ''
    if string[0] == ' ':
        string = string[1:]
    if string[-1] == ' ':
        string = string[:-1]
    if string[-1] == '-':
        string = string[:-1]
    if string == '. .':
        string = ''
    if string == '- -' or string == '-- --' or string == '-- -':
        string = ''
    if len(string.split(' ')) < 2:
        string = ''
    if string == 'Cover Vol.':
        string = ''
    string = string.replace('และคณะ', '')
    
    string = string.title()
    string = re.sub(r'[-*](?=\s*$)', '', string)
    string = re.sub(r'\b(?:Dr.|M.R. |Prof.|Mr.|Ms.|Mrs.|นาย|นางสาว|นาง|ม.ร.ว.| ร.ต. |ทันตแพทย์หญิง|พระ|พระครู|ผู้ช่วยศาสตราจารย์|ผศ.|ดร.| ดร. |นพ.|Authors :|ว่าที่|ร.ต.|รองศาสตราจารย์ ดร.|ดร. |ผู้ช่วยศาสตราจารย์|ผู้ช่วยศาสตราจารย์ ดร.|รองศาสตราจารย์ ดร.| ดร.|อ.|อ.ดร.| พ.ต. ดร.|อาจารย์ ดร.|รศ.ดร.|รศ.ดร.| พ.ต. ดร.|พระ|พระมหา|พระครู|พระสรวิชญ์|พระครูใบฎีกา|พระครูสมุห์|พระปลัด)\b', '' ,string)
    string = re.sub(r'ู^(?:Dr.|M.R. |Prof.|Mr.|Ms.|Mrs.|นาย|นางสาว|นาง|ม.ร.ว.| ร.ต. |ทันตแพทย์หญิง|พระ|พระครู|ผู้ช่วยศาสตราจารย์|ผศ.|ดร.| ดร. |นพ.|Authors :|ว่าที่|ร.ต.|รองศาสตราจารย์ ดร.|ดร. |ผู้ช่วยศาสตราจารย์|ผู้ช่วยศาสตราจารย์ ดร.|รองศาสตราจารย์ ดร.| ดร.|อ.|อ.ดร.| พ.ต. ดร.|อาจารย์ ดร.|รศ.ดร.|รศ.ดร.| พ.ต. ดร.|พระ|พระมหา|พระครู|พระสรวิชญ์|พระครูใบฎีกา|พระครูสมุห์|พระปลัด)\b', '' ,string)
    
    #string = re.sub(r'(.+)-(.+)-(.+)', r'\1\2\3', string)
    #string = re.sub(r'(.+)-(.+)', r'\1\2', string)
    #string = re.sub(r'(.+)ณ(.+)', r'\1', string)
    
    string = re.sub('\d', '', string)
    
    return string

def contains_thai_and_english(sentence):
    # Regular expressions for Thai and English words
    thai_pattern = re.compile(r'[\u0E00-\u0E7F]')
    english_pattern = re.compile(r'[A-Za-z]')

    # Check if both Thai and English characters are present
    contains_thai = bool(thai_pattern.search(sentence))
    contains_english = bool(english_pattern.search(sentence))

    return contains_thai and contains_english

def remove_duplicates_preserve_order(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

num = 1

if __name__ == '__main__':
    char = {'id': [], 'name': []}
    df = pd.read_csv('/kaggle/input/thaijo-researcher-for-code-submission/test.csv')
    df = df.fillna('')
    for idx, row in df.iterrows():
        names = []
        char['id'].extend([f"{row['_id']}_{i+1}" for i in range(10)])
        
        author = row['_source.author']
        author = re.split(r'; |, ', author)[0]
        if author != '':
            print("A", author)
            author = remove_spaces(author).strip()
            #print("A\'", author)
            if contains_thai_and_english(author):

                thai_unicode_range = "\u0E00-\u0E7F"

                pattern = f'([{thai_unicode_range}\s]+)([a-zA-Z\s]+)'

                matches = re.match(pattern, author)

                if matches:
                    thai_segment = matches.group(1).strip()
                    english_segment = matches.group(2).strip()
                    names.append(thai_segment)
                    names.append(english_segment)
                else:
                    names.append(author)
            else:
                names.append(author)
        
        
        co_author = row['_source.co-author']
        if co_author != '':
            print("Co:", co_author)
            ca = re.split(r'; |, ', co_author)
            for c in ca:
                c = remove_spaces(c).strip()
                #print("C\''", c)
                if c not in names:
                    if contains_thai_and_english(c):       

                        thai_unicode_range = "\u0E00-\u0E7F"

                        pattern = f'([{thai_unicode_range}\s]+)([a-zA-Z\s]+)'

                        matches = re.match(pattern, c)

                        if matches:
                            thai_segment = matches.group(1).strip()
                            english_segment = matches.group(2).strip()
                            #print("1st:", thai_segment)
                            #print("2nd:", english_segment)
                            names.append(thai_segment)
                            names.append(english_segment)
                            #print(names)
                        else:
                            names.append(c)
                    else:
                        names.append(c)
    
        names = remove_duplicates_preserve_order(names)
        if len(names) == 0:
            char['name'].extend([None]*10)
            continue
        #names = [remove_spaces(name).strip() for name in names]
        names = list(filter(lambda x: x.strip() and any(c.isalnum() for c in x), names))
        print(f"{num} Result:", names, end="\n\n")
        num += 1
        if len(names) > 10:
            names = names[:10]
        elif len(names) < 10:
            names.extend(['']*(10-len(names)))
        char['name'].extend(names)
    
    char = pd.DataFrame(char)
    print(char)
    char.to_csv('predict.csv', index=False)