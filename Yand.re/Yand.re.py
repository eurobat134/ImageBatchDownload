from ast import Num
from distutils.log import error
from fileinput import filename
from lib2to3.pgen2.driver import Driver
from optparse import Values
from textwrap import indent
import bs4
from matplotlib import image
import requests
from selenium import webdriver
import os
import urllib
import time
import pandas as pd
import urllib.request
import urllib3



os.chdir('Yand.re/')
folder_name = 'images'
if not os.path.exists('images'):
    os.makedirs('images')
Grabber_folder = 'Grabbers'
PageList = list()
i = 0
total = 0
idTxtfile = open('ids.txt', 'w')
yx = open('test.txt', 'w')





qualitybuttonXpath = """//*[@id="resized_notice"]/a[1]"""
v = -1
ID = ["0","1","2","3","4","5","6","7","8","9"]
secID = list()





postpostfix=input("What are you searching for?")
if postpostfix.startswith("https://yande.re"):
    sURL = postpostfix.split("tags=")
    postpostfix = sURL[1]
driver=webdriver.Chrome()








vv = open('hope.txt', 'w')








#search_URL = "https://yande.re/post?page=1&tags=domestic_na_kanojo"
prefixURL= "https://yande.re/post?page="
postFixUrl="&tags="
p1 = "1"
driver.get(f"{prefixURL}{p1}{postFixUrl}{postpostfix}")




#gets all ids
###
ss = driver.find_elements_by_xpath('//*[@id="paginator"]/div/a')




for ii in ss:
    vv.write(f"{ii.get_attribute('aria-label')}\n")
    PageList.append(f"{ii.get_attribute('aria-label')}\n")

vv.close()
vv = open('hope.txt', 'r')
PL = open('PageList.txt', 'w')

BigPage = PageList[-2]   
to_str = str(BigPage)






page_num = to_str[5:]
to_int = int(page_num)

print(f"{to_int} Pages To Download")


all = to_int
input2 = False
while input2 == False:
    
    PagesInput = input(f"How Many Pages Would You Like To Download?(1 / half({round(to_int/2)}) / all).")
    
    
    
    if PagesInput == "1":
        to_int = 1
        input2 = True
    elif PagesInput == "half":
        to_int = round(to_int/2)
        input2 = True
    elif PagesInput == "all":
        to_int = to_int
        input2 = True
    else:
        try:
            intTest = int(PagesInput)
            if intTest <= to_int:
                to_int = intTest
                input2 = True
        except:
            if int(PagesInput) > to_int:
                print(f"Please Enter A Number From 1 - {to_int}.")
                continue
            elif int(PagesInput) < 1:
                print(f"Please Enter A Number From 1 - {to_int}.")
            else:
                print("Please Enter A Correct Page Number.")
                continue




print (f"Starting To Download {to_int} Pages")

def getSecondLetter(txt):
    if len(txt) > 1:
        secID.append(txt[1])

def download_image(url, folder_name, num):

    # write image to file
    reponse = requests.get(url)
    if reponse.status_code==200:
        with open(os.path.join(folder_name, str(num)+".jpg"), 'wb') as file:
            file.write(reponse.content)


TT = 0
strTT = str(TT + 1)

HD2 = False
k4k2 = False
qqcc = False
while qqcc == False:
    
    QualityCheck = input("What Quality Would You Like? (HD / Best(4k-8k) ).")
    
    
    
    
    
    
    if QualityCheck == "HD":
        HD2 = True
        qqcc = True

    
    elif QualityCheck == "hd":
        HD2 = True
        qqcc = True
    
    elif QualityCheck == "Best":
        k4k2 = True
        qqcc = True
    
    elif QualityCheck == "best":
        k4k2 = True
        qqcc = True
    
    elif QualityCheck == "BEST":
        k4k2 = True
        qqcc = True
    
    elif QualityCheck == "4k":
        k4k2 = True
        qqcc = True
    
    elif QualityCheck == "8k":
        k4k2 = True
        qqcc = True
    else:
        print("Please Enter A Correct Quality Option.")





if k4k2 == True:
    
    while TT < to_int:
    
        driver.get(f"{prefixURL}{strTT}{postFixUrl}{postpostfix}")
        idTxtfile = open('ids.txt','w')
    
        ids = driver.find_elements_by_xpath('//*[@id]')
        for ii in ids:
            idTxtfile.write(f"{ii.get_attribute('id')}\n")
    
        idTxtfile.close()
        idTxtfile = open('ids.txt', 'r')
        yx = open('test.txt', 'w')
    
    
        for word in idTxtfile:
            if word.startswith("p"):
                #print(word)
                x = getSecondLetter(word)
                v = v+1
                if secID[v] in ID:
                    s = word
                    s = s[1:]
                    yx.write(f"https://yande.re/post/show/{s}")
        yx.close
        yx = open('test.txt', 'r')
        count = len(open('test.txt').readlines())
        
        for url in yx:
            try:
                driver.get(url)
                driver.find_element_by_xpath(qualitybuttonXpath).click()
                timeStarted = time.time()
            except:
                driver.get(url)
                timeStarted = time.time()
                
            
            while True:
                imageElement = driver.find_element_by_xpath("""//*[@id="image"]""")
                imageURL= imageElement.get_attribute('src')
                currentTime = time.time()
                if currentTime - timeStarted > 2:
                    break
            try:
                i = i+1
                name = (f"P{TT}!i{i}")
                download_image(imageURL, folder_name, name)
                print(f"Downloaded Image {i} Out of {count} ")
            except:
                print("Couldn't download an image %s, continuing downloading the next one"%(i))
        if i == count:
            total = total + i
            i=0
            TT = TT + 1
            strTT = str(TT)
            name = (f"P{TT}!i{i}")
            print(i)
            print (f"Now Downloading Page {TT}")
        else:
            total = total + i
            i=0
            TT = TT + 1
            
            strTT = str(TT)
            name = (f"P{TT}!i{i}")
            print("Error didn't Download All will go to the next page tho")
            print (f"Now Downloading Page {TT}")




elif HD2 == True:
    while TT < to_int:
    
        driver.get(f"{prefixURL}{strTT}{postFixUrl}{postpostfix}")
        idTxtfile = open('ids.txt','w')
    
        ids = driver.find_elements_by_xpath('//*[@id]')
        for ii in ids:
            idTxtfile.write(f"{ii.get_attribute('id')}\n")
    
        idTxtfile.close()
        idTxtfile = open('ids.txt', 'r')
        yx = open('test.txt', 'w')
    
    
        for word in idTxtfile:
            if word.startswith("p"):
                #print(word)
                x = getSecondLetter(word)
                v = v+1
                if secID[v] in ID:
                    s = word
                    s = s[1:]
                    yx.write(f"https://yande.re/post/show/{s}")
        yx.close
        yx = open('test.txt', 'r')
        count = len(open('test.txt').readlines())
        
        for url in yx:

            driver.get(url)
            timeStarted = time.time()
                
            
            while True:
                imageElement = driver.find_element_by_xpath("""//*[@id="image"]""")
                imageURL= imageElement.get_attribute('src')
                currentTime = time.time()
                if currentTime - timeStarted > 2:
                    break
            try:
                i = i+1
                name = (f"P{TT+1}!i{i}")
                download_image(imageURL, folder_name, name)
                print(f"Downloaded Image {i} Out of {count} ")
            except:
                print("Couldn't download an image %s, continuing downloading the next one"%(i))
        if i == count:
            total = total + i
            i=0
            TT = TT + 1
            strTT = str(TT)
            name = (f"P{TT}!i{i}")
            print(i)
            print (f"Now Downloading Page {TT}")
        else:
            total = total + i
            i=0
            TT = TT + 1
            
            strTT = str(TT)
            name = (f"P{TT}!i{i}")
            print("Error didn't Download All will go to the next page tho")
            print (f"Now Downloading Page {TT}")
else:
    print("An Error Has Occured Please Retry.")

os.remove("hope.txt")
os.remove("ids.txt")
os.remove("PageList.txt")
os.remove("test.txt")

print(f"Finished Downloading All {to_int} Pages")
print(f"Total Downloaded Images:{total}")


    


        
