
# coding: utf-8

# In[5]:


#lab1q1_Wei_Tang
price = float(input("Enter item price: "))
provin_tax = price*0.05
fed_tax = price*0.07
total = price + provin_tax + fed_tax
print("Item price: "+ str(price))
print("Provincial tax: "+str(provin_tax))
print("Federal tax: "+str(fed_tax))
print("Total: "+str(total))

import decimal
print("Total: "+format(round(total,2), '.2f'))


# In[ ]:


#Lab1q2_Wei_Tang
from datetime import date
date = ""
while date != "STOP":
    date = input("Enter a date in format yy.mm.dd: ")
    if date == "STOP":
        break
    list1 = date.split(".")
    year = list1[0]
    mth = list1[1]
    date = list1[2]
    
    if year > "60":
        year = "19"+year
    else:
        year = "20"+year
    
    year = int(year)
    mth = int(mth)
    date = int(date)
    
    import calendar
    check = calendar.monthrange(year, mth)[1]
   
    if date > check:
        print("Error: Invalid date.")
    else:
        #Bonus_1
        print("{}-{}-{}".format(year,mth,date))
        #Bonus_2
        mth = calendar.month_name[mth]
        year = str(year)
        mth = str(mth)
        date = str(date)
        print("Date: "+year+", "+mth+" "+date)
        print(mth)
        


# In[141]:


#Lab1q3_Wei_Tang
data = """5:Joe:35000:1970-08-09
4:Steve:49999:1955-01-02
1:Leah:154000:1999-06-12
3:Sheyanne:255555:1987-05-14
2:Matt:24000:1972-11-03
7:Kyla:1000000:1950-02-01
8:Dave:15000:2000-09-05
"""
from datetime import datetime

field = "Id: , Name: , Salary: , Birthday: "
lines = data.split()

total = 0
maxs = 0
young = -1
name = ""
wordlist = [-1] * len(lines)
i = 0
for line in lines:
    words = line.split(":")
    wordlist[i] = words
    i = i+1
    labels = field.split(",")
    for word, label in zip(words, labels):
        print(label+word+'\t', end='')
    birthday = datetime.strptime(words[-1], '%Y-%m-%d')
    age = int((datetime.today()-birthday).days/365)
    age = str(age)
    print('\n'+"Age: "+age)
    total = total + int(words[2])
    maxs = max(maxs, int(words[2]))
    if young == -1 or int(age) < int(young):
        young = age
        name = words[1]
print()

count = len(lines)
avg = total/count

print("Number of perople: %d" % count)
print("Total salary: %d  Average salary: %d  Max salary: %d" % (total, avg, maxs))
print("Youngest employee: " + name)
print()
for line in lines:
    words = line.split(":")
    if int(words[2]) < 40000 or len(words[1]) < 5:
        newsal = int(words[2]) * 1.2
        print(words[1] +" "+"Old salary: " +words[2]+ " New salary: %d" % newsal)
print()
        
print("Bonus:")
j = 0
for words in wordlist:
    if int(words[2]) < 40000 or len(words[1]) < 5:
        newsal = int(words[2]) * 1.2
        print(words[1] +" "+"Old salary: " +words[2]+ " New salary: %d" % newsal)

        #bonus_2
        wordlist[j][2] = newsal
    j = j+1
print(wordlist)
        

