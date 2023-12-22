# -*- coding: utf-8 -*-
"""
Nama : Ahmad Fauzan Zaky
NIM : 21523201

PositiveView
"""

#import nltk
#from nltk.metrics.distance import jacard_distance
#from nltk.util import ngrams
#nltk.download('words')
#from nltk.corpus import words
import re
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#correctWords = words.words()
textYoutubeComments = ""
commentValuePos = 0
commentValueNeg = 0
commentValueNet = 0

def Convert(string):
    lis = list(string.split('\n'))
    return lis

fPos = open("positiveWords.txt", "r", encoding='utf-8')
teksP = fPos.read()
teksPlist = Convert(teksP) 

fNeg = open("negativeWords.txt", "r", encoding='utf-8')
teksN = fNeg.read()

with Chrome() as driver:
    wait = WebDriverWait(driver,10)
    driver.get("https://www.youtube.com/watch?v=DuWrjg5EbU8")

    for item in range(6):
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(6)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
        textYoutubeComments += comment.text + "\n"
        print(comment.text + "\n")

listYoutubeComments = textYoutubeComments.splitlines()
flagA=0
for n in listYoutubeComments:
    for i in teksPlist:
        if re.search(i, n.lower()):
                flagA=1 
                break
    if flagA==1:
        commentValuePos +=1
        print (n + "[POSITIF]"+"\n")
    else:
        print (n + "[?]"+"\n")
    flagA=0
print("Komentar positif : ", commentValuePos)

"""
for i in teksPlist:
    if i == teksPlist:
            flagA=1
            break
if flagA==1:
"""

    