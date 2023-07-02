# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:23:08 2023

@author: kkzin
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 01:18:13 2023

@author: kkzin
"""

#!/bin/python3
#0 finding prime number
for num in range(1,11):
    if num > 1:
        for i in range(2,num):
            if num%i ==0:
                print('Not a prime number', num)
                break
            #print('Áfter Break')
        else:
            print('Prime Number',num)


#(1)  Multiple of 3  or 5
number = int(input('Enter Integer Number: '))
sum = 0
for num in range(number):
    if num%3==0 or num%5==0:
        sum = sum +  num

print(sum)

#(2) Even Fibonacci numbers
a = 1
n = 0
even_sum = 0
num = 0
while num < 4000000:
    n = a
    #print('n is',n)
    a = num 
   # print('a is',a)
    num = a + n
    print(num)
    if(num%2==0):
        even_sum = even_sum + num
print(even_sum)


#(3) Largest Prime Factor
n = 10
i = 2
prime = []
x = 0
largest = 0
while i <= n:
    if n % i == 0:
        prime.append(i)
        n = n/i
        print(n)
    else:
        i = i + 1

print(prime)

print(i)

#(4) Sum square difference
square_sum = 0
sum_square = 0
sum = 0
for i in range(101):
    square_sum = square_sum + i**2

print(square_sum)

for i in range(101):
    sum = sum + i

sum_square = sum ** 2
print(sum_square)

difference = sum_square - square_sum
print(difference)


#(5) Smallest multiple
num = 20

while True:
    divisible = True
    for i in range(1, 21):
        if num % i != 0:
            divisible = False
            break
    if divisible:
        print(num)
        break
    else:
        num += 20

        
#My Exercise

num = ''
n_list = []
summary = 0
while num != 'done':
    num = input('Enter the integer: ')
    try:
        n = int(num)
        n_list.append(n)
        summary = summary + n
        print('Input is integer')
    except:
        print('Invalid Value',num, 'Please Enter Integer')
        print('If you are done with calculation, please type "done"')
        
else:
    print('your input value is',n_list)
    print('Summary of input value is',summary)
    smallest = n_list[0]
    largest = n_list[0]
    for number in n_list:
        print('number is',number)
        if number > largest:
            largest = number
            print('largest is',largest)
        if number < smallest:
            smallest = number
            print('smallest is',smallest)
    print('Your input largest number is',largest)
    print('Your input smallest number is',smallest)
    print(n_list[0:])
            
fruit = 'banana'
index = 0
while index !=len(fruit):
    print(fruit[index])
    index = index +1
print('Index after loop is',index)

fruit = 'APPLE'
count = 0
for f in fruit:
    if f=='P':
        count = count +1
else:
    print('The count of letter P is',count)
    
print('The count of letter P is ',fruit.count('P'))
    
word = 'LOVE YOU KOKO'
print(len(word))
print(word[0:-3])
print(word.lower())
lower = word.lower()
print(lower)
dir(word)
print(word.split())
w_list = word.split()
print(w_list)
found = word.find('OU')
print(found)
new_word = word.replace('KO','BABY',1)
print(new_word)
print(word)
new_without_space = word.strip()
print(new_without_space)

word_2 = 'kkzin.january1994@gmail.com is my email. Please contact me.'
search_1 = word_2.find('@')
print(search_1)
search_2 = word_2.find(' ',search_1)
print(search_2)
print(word_2[search_2])
searched_word = word_2[search_1:search_2]
print(searched_word)

import os
cur_dir = 'D:\Core_SI\Learning\Coursera\Python'
os.chdir(cur_dir)
root = os.getcwd()


'''The reason why you cannot see any data or line count when using the read() 
function is because after calling the read() function, the file pointer moves to 
the end of the file. So when you try to read the contents of the file again using 
a for loop, there is nothing left to read.'''
'''
As you can see, the output is different. 
This code reads the entire contents of the file into the contents variable 
using the read() function. But when it tries to loop through the file again, 
there is nothing left to read, so the for loop does not execute at all. 
As a result, the line count remains at 0, and no data is printed.

To fix this issue, you can use the seek() function to move the file pointer
 back to the beginning of the file after calling read(), like this:'''

file = open('test.txt')
file_data = file.read()
print(file_data)
print(len(file_data))
file.seek(0) # move the file pointer back to the beginning of the file
count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith('PROD'):
        continue
    else:
        print(line)
        count = count +1
print(count)

count = 0
for line in file:
    if line.startswith('PROD'):
        print(line)
        count = count +1

print('PROD',count)

filename = input('Enter the file name: ')
try:
    file = open(filename)
except:
    print('File cannot be opened: ',filename)
    
count = 0
for line in file:
    if line.startswith('PROD'):
        count = count +1
print('PROD Count is',count)


import os
cur_dir = 'D:\Core_SI\Learning\Coursera\Python'
os.chdir(cur_dir)
root = os.getcwd()

existing_filename = ['test.txt','file.txt']
count = 0
while True:
    input_file_name = input('Enter the file name in this folder: ')
    try:
        input_file = open(input_file_name)
        #print(type(input_file))
        for line in input_file:
            if line.startswith('PROD') or line.startswith('Kyawt'):
                count = count +1
        if input_file_name== 'test.txt':
            print('PROD count is',count)
        else:
            print('Kyawt count is',count)
        input_file.seek(0)
        count = 0
        break
    except:
        print('Enter the correct name in this folder.')
        continue
    


filename = input('Enter the filename')
file = open(filename)
count = 0
for line in file:
    if line.startswith('PROD'):
        count = count +1
print('PROD Count is',count)


filename = 'mbox-short.txt'
file_data = open(filename)
#data_read = file_data.read()
#file_data.seek(0)
#print(data_read)
line_count = 0
summary = 0
for data in file_data:
    print(data)
    if data.startswith('X-DSPAM-Confidence: '):
        print(data)
        line_count = line_count + 1
        index = data.find('0')
        print('index is',index)
        hold_data = float(data[index:-1])
        summary = summary + hold_data
    else:
        continue
file_data.seek(0)

print(line_count)
print('Average spam confidence:',summary/line_count)

name_list = ['Kyawt','Zin','Aye','Mya']
for name in name_list:
    print(name)
print(name_list[0:])
#List
#List are mutable and String are immutable
#Lists have length
#value in list can be different type
#can sort
#split() of String can be changed into list, also used with splitter

name_list[0] = 'Zin Zin'
for name in name_list:
    print(name)
print(len(name_list))
name = name_list[0:]
print(name)

friend_name = ['Johny','Mia','Suzy','Zen']

for i in range(len(friend_name)):
    friend = friend_name[i]
    print('Happy New Year:',friend)
#They are the same
for friend in friend_name:
    print('Happy New Year:',friend)

friend_name.append('William')
print(friend_name)

'Mia' in friend_name

friend_name.sort()
print(friend_name)

string = 'Mia Kyawt Kyawt Zin'
string_list = string.split(' ')
print(string_list)
print(len(string_list))

string_1 = 'KKZ_KKZZ_KKZIN_KKKK'
string_list = string_1.split('_')
print(string_list)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))
print(c)

#To summarize, append() adds a single element to the end of a list, 
# while extend() adds multiple elements from an iterable to the end of a list, treating each element individually.

import os
cur_dir = 'D:\Core_SI\Learning\Coursera\Python'
os.chdir(cur_dir)
root = os.getcwd()

file_list = []
file_name = 'romeo.txt'

with open(file_name) as file_data:
    for data in file_data:
        print(data)
        words = data.strip().split()
        print(words)
        for word in words:
            file_list.append(word)
        #print(file_list)
file_list.sort()
print(file_list)

with open(file_name) as file_data:
    for data in file_data:
        print(data)
        words = data.strip().split()
        print(words)
        #for word in words:
            #file_list.append(word)
        #print(file_list)
        file_list.extend(words)
#file_list.sort()
print(file_list)

word_list = []
with open(file_name) as file_data:
    for data in file_data:
        words = data.strip().split()
        print(words)
        for word in words:
            word_list.append(word)

print(word_list)
        
import os

cur_dir = r'D:\Core_SI\Learning\Coursera\Python'
os.chdir(cur_dir)

file_name = 'romeo.txt'
file_list = []

with open(file_name) as file_data:
    for line in file_data:
        print(line)
        words = line.strip().split()
        file_list.extend(words)

print(len(file_list))
        
file_list.sort()
print(len(file_list))
print(file_list)
hold_data = ''

unique_list = []
for data in file_list:
    if data not in unique_list:
        unique_list.append(data)
        print(unique_list)
print(unique_list)
print(len(unique_list))

file_name = 'mbox-short.txt'

file_data = open(file_name)
count = 0
with open(file_name) as file_data:
    for line in file_data:
        #print(line)
        line = line.rstrip()
        #print(line)
        split_data = line.split()
        #print(split_data)
        #print(len(split_data))
        if len(split_data) < 1 or  split_data[0] != 'From':
            #print(split_data)
            #print('------------------------------')
            continue
        else:
            print(split_data[1])
            count = count +1
print(count)
        
#dictionary - Python for Everybody
#mutable , key, value
purse = dict()
purse['Money'] = 58
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
    
purse['candy'] = purse['candy']  + 3
print(purse)

name = None
name_list = []
while True:
    name = input('Enter the name: ')
    if name !='done':
        name_list.append(name)
        continue
    else:
        break
    
print(name_list)

name_dict = {}
type(name_dict)

for name in name_list:
    if name not in name_dict:
        name_dict[name] = 1
    else:
        name_dict[name] = name_dict[name] + 1
print(name_dict)

dir(name_dict)

for name in name_dict:
    x = name_dict.get(name,0)
    print(name,x)

name = None
name_list = []
name_dict = {}
while True:
    name = input('Enter the name: ')
    if name !='done':
        name_list.append(name)
        continue
    else:
        break
    
print(name_list)

for name in name_list:
    name_dict[name] = name_dict.get(name,0) + 1
    
print(name_dict)

''''For bass fishing, use 8 to 12 pound test monofilament or fluorocarbon line with
 finesse presentations using spinning gear. Bump it up to 15 or 20 pound test in heavy cover. 
 When casting big swimbaits, crankbaits, jigs and topwater tackle, a braided main line in the 30-50 pound 
 test range is incredibly versatile.'''

print('Enter the text line.')
line = input('')
print(line)

words = line.rstrip().split()
print(words)
word_dict = {}

for word in words:
    word_dict[word] = word_dict.get(word,0) + 1
print(word_dict)

for key  in word_dict:
    print(key,word_dict[key])

print(list(word_dict.keys()))
print(list(word_dict.values()))
print(word_dict.items())
type(word_dict.items())

for key,value in word_dict.items(): #items() results the list of tuple so, we can do with two iterations (keys and values)
    print(key,value)

#######################################################
# Dictionary Exerciese
import os
cur_dir = 'D:\Core_SI\Learning\Coursera\Python'
os.chdir(cur_dir)
root = os.getcwd()

word_list = []
word_dict = {}
bigword = None
bigcount = None


while True:
    file_name = input('Enter File Name: ')
    try:
        with open(file_name) as file_data:
            for data in file_data:
                word_list = data.rstrip().split()
                #print(word_list)
                for word in word_list:
                    word_dict[word] = word_dict.get(word,0) + 1
            #print(word_dict)
            for key,value in word_dict.items():
                if bigcount is None or value > bigcount:
                    bigword = key
                    bigcount = value
                    
            print(bigword,bigcount)
            break
    except:
        print('Please enter the correct file.')
        continue

import os
cur_dir = 'D:\Core_SI\Learning\Coursera\Python' #directory of current python
os.chdir(cur_dir)
root = os.getcwd()


word = ''
word_list = []
word_dic = {}
big_word = ''
big_value = 0
while True:
    filename = input('Enter File Name :')
    try:
        file_data = open(filename)
        for data in file_data:
            word = data.rstrip().split()
            print(word)
            if len(word) <1 or word[0]!='From':
                continue
            else:
                word_list.append(word[1])
        #print(word_list)
        for word in word_list:
            word_dic[word] = word_dic.get(word,0) + 1
        print(word_dic)
        for key,value in word_dic.items():
            if value > big_value:
                big_word = key
                big_value = value
        print(big_word, big_value)
        break             
    except:
        print('Enter the correct name')
        continue
print(word_dic.items())
############################################################################

#Tuple - immutable
#cannot sort

x = ('Aye','Nwe','Khin')
print(x[2])
            
x[2] = 'Min' #Tuple are immutable

y = (1,2,3,4)
print(y)
for num in y:
    print(num)

(a,b) = (4,'fred')
print(a)

name_id = {'Kyawt Kyawt Zin':215,'Wai Yan Ye Min':236}

print(name_id.items())

type(name_id.items())

name_id_list = name_id.items()

print(name_id_list)

for name in name_id_list:
    print(name[0])

(a,b,c) = (4,'fred','Kyawt')

print(sorted([(v,k) for (k,v) in name_id.items()]))
################################################

import os
cur_dir = r'C:\Users\Kyawt Kyawt Zin\Desktop\Learning\python'
os.chdir(cur_dir)
root = os.getcwd()

file_name = 'mbox-short.txt'
file_data = open(file_name)
word_list = []
time_list = []
word_dic = {}
for data in file_data:
    split_data = data.rstrip().split()
    #print(split_data)
    if len(split_data)<1 or split_data[0]!='From':
        continue
    else:
        split_data = split_data[5].split(':')
        #print(split_data)
        #split_data.sort()
        #print(split_data)
        word_dic[split_data[0]] = word_dic.get(split_data[0],0)+1
        #print(word_dic)

list_sorted = sorted([(k,v) for (k,v) in word_dic.items()])
list_1 = []
for k,v in word_dic.items():
    #print(k,v)
    list_1.append((k,v))
    #print(list_1)
    list_sorted = sorted(list_1)
    print(list_sorted)


for k,v in list_sorted:
    print(k,v)
    
for line in file_data:
    line=line.rstrip()
    if line.startswith('From: '):
        print(line)


#Set

numbers = [1,2,3,4,1,1,1,5,6,8,5,4]
unique_nums = set(numbers)
print(unique_nums)

fruit = {'apple','banana','orange','grapefruit'}
print('watermelon' in fruit)
fruit.add('watermelon')
print(fruit)
print(fruit.pop())



# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for fruit, count in basket_items.items():
    if fruit in fruits:
        result = result + count
        
print(result)
#Iterate through the dictionary

#if the key is in the list of fruits, add the value (number of fruits) to result

##############################
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:',line):
        print(line)
###########################
#Regular Expression, ^X.*: , . is any character, * any character zero or more time
#

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:',line):
        print(line)

y = []        
import re
x = 'My 2 00  favourite numbers are 19 and 42'
y = re.findall('[0-9]+',x) #return the list of the characther 
print(y)
z = re.findall('[aeiou]+',x)
print(z)

import re

x = 'From: Using The Character: Hello'
y = re.findall('^F.+:',x)
print(y)

y = re.findall('^F.+?:',x)
print(y)


y = re.findall('@([^ ]*)','From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008')
print(y)


mail_list = []
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('From:.*@([^ ]*)',line)
    if len(x)<1:
        continue
    else:
        mail_list.extend(x)
print(mail_list)
print(len(mail_list))

mail_list = []
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From:([^@]*)',line)
    if len(x)<1:
        continue
    else:
        mail_list.extend(x)
print(mail_list)
print(len(mail_list))


num_list = []
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(x)< 1:
        continue
    else:
        num = float(x[0])
        num_list.append(num)
print(num_list)
print(len(num_list),max(num_list))

x = 'I got $25.55 from my mother as a gift.'
y = re.findall('\$[0-9.]+',x)
print(y)

num_list = []
file_data = open('regex_sum_1797563.txt')
for line in file_data:
    #line = line.rstrip()
    #print(line)
    
    data = re.findall('[0-9]+',line)
    for data_str in data:
        num_list.append(int(data_str))

print(sum(num_list))
#################################################

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #byte
mysock.send(cmd)

while True:
    data = mysock.recv(512) #byte
    if len(data) < 1:
        break
    print(data.decode(),end='') #Unicode, String

mysock.close()

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.globalnet.com.mm/')

counts = dict()
for line in fhand:
    #print(type(line))
    #print(line)
    print(line.decode())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) +1
print(counts)
######################################################

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

# Retrive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href',None))
    
import ssl

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_2 = input('Enter URL -')
html_2 = urllib.request.urlopen(url_2,context = ctx).read()
soup_2 = BeautifulSoup(html_2,'html.parser')
#retrive all the anchor tags
tags = soup_2('a')
for tag in tags:
    print(tag.get('href',None))
  

import re
line = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
data = re.findall('href=(".*")',line)
print(data)

########################################################
#Exercise
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('tr')
num_list = []
for tag in tags:
    # Look at the parts of a tag
    #print(type(tag))
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[1].decode())
    hold_data = tag.contents[1].decode()
    #print(hold_data)
    data = re.findall('">([0-9]*)<',hold_data)
    if len(data)<1:
        continue
    num_list.append(int(data[0]))
    #print(num_list)
   # print('span',)
print(num_list)
print(sum(num_list))

#####################################################
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Shazil.html'
count = 7  # number of times to repeat the process
position = 18  # position of the link to follow

for i in range(count):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    #print(type(tags[position-1]))
    url = tags[17].get('href', None)
    print(type(url))
    print("Retrieving:", url)
    #print(url.split())

# Extract the last name from the final url
last_name = url.split('_')[-1].split('.')[0]
print(last_name)
######################################################
import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Kyawt Kyawt Zin</name>
    <phone type = 'intl'>+959 448543172</phone>
    <email hide = "yes"/>
</person>
'''

tree = ET.fromstring(data)
print(tree)
print('Phone Number: ',tree.find('phone').text)
phone_number = tree.find('phone').text
print(type(phone_number))
print('Name : ',tree.find('name').text)
print('Email : ',tree.find('email').get('hide'))

input = '''
<stuff>
    <users>
        <user x = '2'>
            <id>001</id>
            <name>KKZ</name>
        </user>
        <user x ='7'>
            <id>002</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User Count: ',len(lst))
for item in lst:
    name = item.find('name').text
    id   = item.find('id').text
    attr = item.get('x')
    print(name)
    print(id)
    print(attr)

###################################################
#Exercise
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
#from bs4 import BeautifulSoup

url = input('Enter URL : ')
html = urllib.request.urlopen(url, context=ctx)
summary = 0
data = html.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
for item in lst:
    count = item.find('count').text
    #print(type(count))
    count_int = int(count)
    summary = summary + count_int

print(summary)
##################################################

x = -100
from math import sqrt
x > 0 and sqrt(x)
sqrt(x)

language = ['p','y','t','h','o','n']
print(language[0:-4])

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count_odd = 0
i = 0
odd_sum = 0

while count_odd < 5:
    if num_list[i]%2!=0:
        odd_sum = odd_sum + num_list[i]
        count_odd = count_odd + 1
    i = i +1
    
print(count_odd)
print(odd_sum)


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))


manifest = [('banana',15),('apple',10)]
print(manifest[0])


manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

total_weight = 0
weight_items = []

for item,weight in manifest:
    if total_weight >= 100:
        print(item)
        print('Over Weight')
        break
    else:
        total_weight = total_weight + weight
        weight_items.append((item,weight))
        print(item)
        #print(weight_items)
        #print(total_weight)
 
print(total_weight)
print(weight_items)

for item,weight in manifest:
    if total_weight > 100:
        break
    if total_weight+weight >= 100:
        print('Over Weight: ',weight,item)
        continue
    else:
        total_weight = total_weight + weight
        weight_items.append((item,weight))
        print(item)
        #print(weight_items)
        #print(total_weight)
 
print(total_weight)
print(weight_items)

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

total_weight = 0
weight_items = []

for item,weight in manifest:
    if weight < 100:
        if total_weight < 100:
            total_weight = total_weight + weight
            weight_items.append((item,weight))
        else:
            break
    else:
        continue
            
        
print(total_weight)
print(weight_items)

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
hold_data = ""

for headline in headlines:
    if len(hold_data) < 141:
        hold_data = hold_data + headline + ' '
    else:
        break

news_ticker = hold_data[0:140]
print(news_ticker)
print(len(news_ticker))
# write your loop here
# write your loop here

###############################################################
#Exercise Prime Number

check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:
    for i in range(2,num):
        if num%i ==0:
            print(num,'is the not a prime number.')
            print(i,'is the factor of ',num)
            break
        if i == num-1:
            print(num,'is a prime number.')
#############################################

letters = ['a','b','c','d']
nums = [1,2,3,4]
new_list = []
for letter, num in zip(letters,nums):
    new_list.append((letter,num))
    print(new_list)
for i, li in enumerate(new_list):
    print(i,li)
    
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
#############################################

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
point = {}
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    #print(point)
    points.append("{}: {}, {}, {}".format(*point))
    #print(points)

for point in points:
    print(point)
################################################

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))

for name,height in zip(cast_names,cast_heights):
    cast[name] = height

print(cast)

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = zip(*cast) # replace with your code
print(names,heights)


data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
a , b, c = zip(*data)
data_transponse = (a,b,c)
print(data_transponse)

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]
# write your for loop here
cast_list = []

for ch in zip(cast,heights):
    cast_list.append('{} {}'.format(*ch))
    #print(cast_list)
cast = cast_list
print(cast)

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.split(' ')[0].lower() for name in names] # write your list comprehension here
print(first_names)

multiples_3 = [i*3 for i in range(1,21)]
print(multiples_3)

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
passed = [ key for key,value in scores.items() if value > 65]
print(passed)

nominated = {1931: ['Norman Taurog', 'Wesley Ruggles', 'Clarence Brown', 'Lewis Milestone', 'Josef Von Sternberg'], 1932: ['Frank Borzage', 'King Vidor', 'Josef Von Sternberg'], 1933: ['Frank Lloyd', 'Frank Capra', 'George Cukor'], 1934: ['Frank Capra', 'Victor Schertzinger', 'W. S. Van Dyke'], 1935: ['John Ford', 'Michael Curtiz', 'Henry Hathaway', 'Frank Lloyd'], 1936: ['Frank Capra', 'William Wyler', 'Robert Z. Leonard', 'Gregory La Cava', 'W. S. Van Dyke'], 1937: ['Leo McCarey', 'Sidney Franklin', 'William Dieterle', 'Gregory La Cava', 'William Wellman'], 1938: ['Frank Capra', 'Michael Curtiz', 'Norman Taurog', 'King Vidor', 'Michael Curtiz'], 1939: ['Sam Wood', 'Frank Capra', 'John Ford', 'William Wyler', 'Victor Fleming'], 1940: ['John Ford', 'Sam Wood', 'William Wyler', 'George Cukor', 'Alfred Hitchcock'], 1941: ['John Ford', 'Orson Welles', 'Alexander Hall', 'William Wyler', 'Howard Hawks'], 1942: ['Sam Wood', 'Mervyn LeRoy', 'John Farrow', 'Michael Curtiz', 'William Wyler'], 1943: ['Michael Curtiz', 'Ernst Lubitsch', 'Clarence Brown', 'George Stevens', 'Henry King'], 1944: ['Leo McCarey', 'Billy Wilder', 'Otto Preminger', 'Alfred Hitchcock', 'Henry King'], 1945: ['Billy Wilder', 'Leo McCarey', 'Clarence Brown', 'Jean Renoir', 'Alfred Hitchcock'], 1946: ['David Lean', 'Frank Capra', 'Robert Siodmak', 'Clarence Brown', 'William Wyler'], 1947: ['Elia Kazan', 'Henry Koster', 'Edward Dmytryk', 'George Cukor', 'David Lean'], 1948: ['John Huston', 'Laurence Olivier', 'Jean Negulesco', 'Fred Zinnemann', 'Anatole Litvak'], 1949: ['Joseph L. Mankiewicz', 'Robert Rossen', 'William A. Wellman', 'Carol Reed', 'William Wyler'], 1950: ['Joseph L. Mankiewicz', 'John Huston', 'George Cukor', 'Billy Wilder', 'Carol Reed'], 1951: ['George Stevens', 'John Huston', 'Vincente Minnelli', 'William Wyler', 'Elia Kazan'], 1952: ['John Ford', 'Joseph L. Mankiewicz', 'Cecil B. DeMille', 'Fred Zinnemann', 'John Huston'], 1953: ['Fred Zinnemann', 'Charles Walters', 'William Wyler', 'George Stevens', 'Billy Wilder'], 1954: ['Elia Kazan', 'George Seaton', 'William Wellman', 'Alfred Hitchcock', 'Billy Wilder'], 1955: ['Delbert Mann', 'John Sturges', 'Elia Kazan', 'Joshua Logan', 'David Lean'], 1956: ['George Stevens', 'Michael Anderson', 'William Wyler', 'Walter Lang', 'King Vidor'], 1957: ['David Lean', 'Mark Robson', 'Joshua Logan', 'Sidney Lumet', 'Billy Wilder'], 1958: ['Richard Brooks', 'Stanley Kramer', 'Robert Wise', 'Mark Robson', 'Vincente Minnelli'], 1959: ['George Stevens', 'Fred Zinnemann', 'Jack Clayton', 'Billy Wilder', 'William Wyler'], 1960: ['Billy Wilder', 'Jules Dassin', 'Alfred Hitchcock', 'Jack Cardiff', 'Fred Zinnemann'], 1961: ['J. Lee Thompson', 'Robert Rossen', 'Stanley Kramer', 'Federico Fellini', 'Robert Wise', 'Jerome Robbins'], 1962: ['David Lean', 'Frank Perry', 'Pietro Germi', 'Arthur Penn', 'Robert Mulligan'], 1963: ['Elia Kazan', 'Otto Preminger', 'Federico Fellini', 'Martin Ritt', 'Tony Richardson'], 1964: ['George Cukor', 'Peter Glenville', 'Stanley Kubrick', 'Robert Stevenson', 'Michael Cacoyannis'], 1965: ['William Wyler', 'John Schlesinger', 'David Lean', 'Hiroshi Teshigahara', 'Robert Wise'], 1966: ['Fred Zinnemann', 'Michelangelo Antonioni', 'Claude Lelouch', 'Richard Brooks', 'Mike Nichols'], 1967: ['Arthur Penn', 'Stanley Kramer', 'Richard Brooks', 'Norman Jewison', 'Mike Nichols'], 1968: ['Carol Reed', 'Gillo Pontecorvo', 'Anthony Harvey', 'Franco Zeffirelli', 'Stanley Kubrick'], 1969: ['John Schlesinger', 'Arthur Penn', 'George Roy Hill', 'Sydney Pollack', 'Costa-Gavras'], 1970: ['Franklin J. Schaffner', 'Federico Fellini', 'Arthur Hiller', 'Robert Altman', 'Ken Russell'], 1971: ['Stanley Kubrick', 'Norman Jewison', 'Peter Bogdanovich', 'John Schlesinger', 'William Friedkin'], 1972: ['Bob Fosse', 'John Boorman', 'Jan Troell', 'Francis Ford Coppola', 'Joseph L. Mankiewicz'], 1973: ['George Roy Hill', 'George Lucas', 'Ingmar Bergman', 'William Friedkin', 'Bernardo Bertolucci'], 1974: ['Francis Ford Coppola', 'Roman Polanski', 'Francois Truffaut', 'Bob Fosse', 'John Cassavetes'], 1975: ['Federico Fellini', 'Stanley Kubrick', 'Sidney Lumet', 'Robert Altman', 'Milos Forman'], 1976: ['Alan J. Pakula', 'Ingmar Bergman', 'Sidney Lumet', 'Lina Wertmuller', 'John G. Avildsen'], 1977: ['Steven Spielberg', 'Fred Zinnemann', 'George Lucas', 'Herbert Ross', 'Woody Allen'], 1978: ['Hal Ashby', 'Warren Beatty', 'Buck Henry', 'Woody Allen', 'Alan Parker', 'Michael Cimino'], 1979: ['Bob Fosse', 'Francis Coppola', 'Peter Yates', 'Edouard Molinaro', 'Robert Benton'], 1980: ['David Lynch', 'Martin Scorsese', 'Richard Rush', 'Roman Polanski', 'Robert Redford'], 1981: ['Louis Malle', 'Hugh Hudson', 'Mark Rydell', 'Steven Spielberg', 'Warren Beatty'], 1982: ['Wolfgang Petersen', 'Steven Spielberg', 'Sydney Pollack', 'Sidney Lumet', 'Richard Attenborough'], 1983: ['Peter Yates', 'Ingmar Bergman', 'Mike Nichols', 'Bruce Beresford', 'James L. Brooks'], 1984: ['Woody Allen', 'Roland Joffe', 'David Lean', 'Robert Benton', 'Milos Forman'], 1985: ['Hector Babenco', 'John Huston', 'Akira Kurosawa', 'Peter Weir', 'Sydney Pollack'], 1986: ['David Lynch', 'Woody Allen', 'Roland Joffe', 'James Ivory', 'Oliver Stone'], 1987: ['Bernardo Bertolucci', 'Adrian Lyne', 'John Boorman', 'Norman Jewison', 'Lasse Hallstrom'], 1988: ['Barry Levinson', 'Charles Crichton', 'Martin Scorsese', 'Alan Parker', 'Mike Nichols'], 1989: ['Woody Allen', 'Peter Weir', 'Kenneth Branagh', 'Jim Sheridan', 'Oliver Stone'], 1990: ['Francis Ford Coppola', 'Martin Scorsese', 'Stephen Frears', 'Barbet Schroeder', 'Kevin Costner'], 1991: ['John Singleton', 'Barry Levinson', 'Oliver Stone', 'Ridley Scott', 'Jonathan Demme'], 1992: ['Clint Eastwood', 'Neil Jordan', 'James Ivory', 'Robert Altman', 'Martin Brest'], 1993: ['Jim Sheridan', 'Jane Campion', 'James Ivory', 'Robert Altman', 'Steven Spielberg'], 1994: ['Woody Allen', 'Quentin Tarantino', 'Robert Redford', 'Krzysztof Kieslowski', 'Robert Zemeckis'], 1995: ['Chris Noonan', 'Tim Robbins', 'Mike Figgis', 'Michael Radford', 'Mel Gibson'], 1996: ['Anthony Minghella', 'Joel Coen', 'Milos Forman', 'Mike Leigh', 'Scott Hicks'], 1997: ['Peter Cattaneo', 'Gus Van Sant', 'Curtis Hanson', 'Atom Egoyan', 'James Cameron'], 1998: ['Roberto Benigni', 'John Madden', 'Terrence Malick', 'Peter Weir', 'Steven Spielberg'], 1999: ['Spike Jonze', 'Lasse Hallstrom', 'Michael Mann', 'M. Night Shyamalan', 'Sam Mendes'], 2000: ['Stephen Daldry', 'Ang Lee', 'Steven Soderbergh', 'Ridley Scott', 'Steven Soderbergh'], 2001: ['Ridley Scott', 'Robert Altman', 'Peter Jackson', 'David Lynch', 'Ron Howard'], 2002: ['Rob Marshall', 'Martin Scorsese', 'Stephen Daldry', 'Pedro Almodovar', 'Roman Polanski'], 2003: ['Fernando Meirelles', 'Sofia Coppola', 'Peter Weir', 'Clint Eastwood', 'Peter Jackson'], 2004: ['Martin Scorsese', 'Taylor Hackford', 'Alexander Payne', 'Mike Leigh', 'Clint Eastwood'], 2005: ['Ang Lee', 'Bennett Miller', 'Paul Haggis', 'George Clooney', 'Steven Spielberg'], 2006: ['Alejandro Gonzaalez Inarritu', 'Clint Eastwood', 'Stephen Frears', 'Paul Greengrass', 'Martin Scorsese'], 2007: ['Julian Schnabel', 'Jason Reitman', 'Tony Gilroy', 'Paul Thomas Anderson', 'Joel Coen', 'Ethan Coen'], 2008: ['David Fincher', 'Ron Howard', 'Gus Van Sant', 'Stephen Daldry', 'Danny Boyle'], 2009: ['James Cameron', 'Quentin Tarantino', 'Lee Daniels', 'Jason Reitman', 'Kathryn Bigelow'], 2010: ['Darren Aronofsky', 'David O. Russell', 'David Fincher', 'Ethan Coen', 'Joel Coen', 'Tom Hooper']}
winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}

# Question 1A: Create dictionary with the count of Oscar nominations for each director 
win_count_dict = {}
# Add your code here, make sure your result is stored in `nom_count_dict`

for year, names in winners.items():
    #print(names)
    for name in names:
        win_count_dict[name] = win_count_dict.get(name,0) + 1
print(win_count_dict)


winners = {1931: ['Norman Taurog'], 1932: ['Frank Borzage'], 1933: ['Frank Lloyd'], 1934: ['Frank Capra'], 1935: ['John Ford'], 1936: ['Frank Capra'], 1937: ['Leo McCarey'], 1938: ['Frank Capra'], 1939: ['Victor Fleming'], 1940: ['John Ford'], 1941: ['John Ford'], 1942: ['William Wyler'], 1943: ['Michael Curtiz'], 1944: ['Leo McCarey'], 1945: ['Billy Wilder'], 1946: ['William Wyler'], 1947: ['Elia Kazan'], 1948: ['John Huston'], 1949: ['Joseph L. Mankiewicz'], 1950: ['Joseph L. Mankiewicz'], 1951: ['George Stevens'], 1952: ['John Ford'], 1953: ['Fred Zinnemann'], 1954: ['Elia Kazan'], 1955: ['Delbert Mann'], 1956: ['George Stevens'], 1957: ['David Lean'], 1958: ['Vincente Minnelli'], 1959: ['William Wyler'], 1960: ['Billy Wilder'], 1961: ['Jerome Robbins', 'Robert Wise'], 1962: ['David Lean'], 1963: ['Tony Richardson'], 1964: ['George Cukor'], 1965: ['Robert Wise'], 1966: ['Fred Zinnemann'], 1967: ['Mike Nichols'], 1968: ['Carol Reed'], 1969: ['John Schlesinger'], 1970: ['Franklin J. Schaffner'], 1971: ['William Friedkin'], 1972: ['Bob Fosse'], 1973: ['George Roy Hill'], 1974: ['Francis Ford Coppola'], 1975: ['Milos Forman'], 1976: ['John G. Avildsen'], 1977: ['Woody Allen'], 1978: ['Michael Cimino'], 1979: ['Robert Benton'], 1980: ['Robert Redford'], 1981: ['Warren Beatty'], 1982: ['Richard Attenborough'], 1983: ['James L. Brooks'], 1984: ['Milos Forman'], 1985: ['Sydney Pollack'], 1986: ['Oliver Stone'], 1987: ['Bernardo Bertolucci'], 1988: ['Barry Levinson'], 1989: ['Oliver Stone'], 1990: ['Kevin Costner'], 1991: ['Jonathan Demme'], 1992: ['Clint Eastwood'], 1993: ['Steven Spielberg'], 1994: ['Robert Zemeckis'], 1995: ['Mel Gibson'], 1996: ['Anthony Minghella'], 1997: ['James Cameron'], 1998: ['Steven Spielberg'], 1999: ['Sam Mendes'], 2000: ['Steven Soderbergh'], 2001: ['Ron Howard'], 2002: ['Roman Polanski'], 2003: ['Peter Jackson'], 2004: ['Clint Eastwood'], 2005: ['Ang Lee'], 2006: ['Martin Scorsese'], 2007: ['Ethan Coen', 'Joel Coen'], 2008: ['Danny Boyle'], 2009: ['Kathryn Bigelow'], 2010: ['Tom Hooper']}
win_count_dict = {}
# Add your code here, make sure your result is stored in `nom_count_dict`

for year, names in winners.items():
    #print(names)
    for name in names:
        win_count_dict[name] = win_count_dict.get(name,0) + 1
print(win_count_dict)
bigger_count = 0
bigger_name = ''
most_win_director = []
for name,count in win_count_dict.items():
    if bigger_count == 0:
        bigger_count = count
    else:
        if count > bigger_count:
            bigger_count = count
            bigger_name = name
            most_win_director.clear()
            most_win_director.append(bigger_name)
print(most_win_director)
             
# Add your code here, make sure your result is stored in `most_win_director`

highest = max(win_count_dict.values())

most_win_director = [key for key , value in win_count_dict.items() if value == highest] 

print(most_win_director)

###############################################################################
#Exercise 2.15 from Python for Everybody
#2
name = input('Please Enter Your Name: ')
print('Hello {}'.format(name))
#3
hour = float(input('Enter hour : '))
rate = float(input('Enter rate : '))
pay = round(hour*rate,2)
print(pay)
#4

'''This causes an UnboundLocalError, since Python doesn't allow functions 
to modify variables that are outside the function's scope. A better way would be 
to pass the variable as an argument and reassign it outside the function.'''
egg_count = 0

def count_eggs():
    egg_count = egg_count + 12

count_eggs()



egg_count = 0

def buy_eggs():
    print(egg_count) # purchase a dozen eggs

buy_eggs()


str1 = 'Functions are important programming concepts.'

def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()


#####################################################################

# Function to square a number
def square(x):
    return x ** 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map() to square each number in the list
squared_numbers = map(square, numbers)

# Converting the result to a list (since map() returns an iterator in Python 3)
squared_numbers_list = list(squared_numbers)

# Output the squared numbers
print(squared_numbers_list)

