import  regex as re
string= '123ca-t!`\'@()-"'
lst2 = re.findall(r'([!-\']|[*-/]|[:-@]|[[-`]|[{-~]|[0-9])', string)

print(lst2)
for i in lst2:
    print(i)
    string = string.strip(i)
stringx= "-cat-"
print(stringx.strip('-'))


print(string)



