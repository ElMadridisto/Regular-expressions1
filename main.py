from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

#first_name_name_surname= r"(^[А-Я][а-я]+)(\s|,)([А-Я][а-я]+)(\s|,)(([А-Я][а-я]+)((\s|,)+)(([А-Я][а-я]+|[А-Я]+),)((\w+\s\w+[\s,–]+(\w+\s)+\w+))?)?"
patern= r"(^[А-Я][а-я]+)(\s|,)([А-Я][а-я]+)(\s|,)(([А-Я][а-я]+)((\s|,)+)(([А-Я][а-я]+|[А-Я]+),)((\w+\s\w+[\s,–]+(\w+\s)+\w+))?)?,((8|\+7)\s?\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})((\s)\(?(\w*.)\s(\d*)\)?)?)?"
#number_phones = r"(8|\+7)\s?\(?(\d{3})\)?[\s|-]?(\d{3})[\s|-]?(\d{2})[\s|-]?(\d{2})(\s\(?(\w*.)\s(\d*)\)?)?"
dict_d = {}
b=[]
#c=[]
d=[]
list_off2 = []
with open('phonebook_raw.csv',encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    for list_1 in rows:
        a=re.sub(patern, r"\1,\3,\6,\10,\12,+7(\16)\17-\18-\19\21\22\23", ','.join(list_1))
        b.append(a)
        #pprint(b)
    for c in b:
        c = c.split(",")
        #print(c)
        #print(c[0]+','+c[1])
        if (c[0]+','+c[1]) not in dict_d:
            dict_d.update({c.pop(0)+','+c.pop(0): c})
        else:
            #print(dict_d[c[0]+','+c[1]])
            #print(c)
            for item in dict_d[c[0]+','+c[1]]:
                if item == '':
                    i = dict_d[c[0]+','+c[1]].index(item)
                    dict_d[c[0]+','+c[1]][i] = c[i + 2]


            #print(dict_d[c[0]+','+c[1]])
    #print(dict_d)
    #list_off2 = []
    for k, v in dict_d.items():
        list_2 = (k,v)
        for items in list_2:
            if type(items) is str:
                list_off = items.split(',')
            else:
                list_off.extend(items)
        #print(list_off)
        list_off2.append(list_off)
#pprint(list_off2)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(list_off2)