# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import time
import xml.etree.ElementTree as ET
import geopandas

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

tree = ET.parse('../input/japan-restaurant-database/getStatsData.xml')

file = open('../input/japan-restaurant-database/getStatsData.xml')
#for text in file:
#print(text)

root = tree.getroot()

#The first legend corrisponds to different tables such as "number of stores", "number of employees", "amount of sales", etc.
legend1 = {}
for i in root.findall(".//CLASS_OBJ[@id='tab']//"):
    legend1[i.attrib.get('name')]=i.attrib.get('code')
#The second legend corrisponds to different types of businesses such as "private", "company" (chain), etc.
legend2 = {}
for i in root.findall(".//CLASS_OBJ[@id='cat01']//"):
    legend2[i.attrib.get('name')]=i.attrib.get('code')
#The third legend corrisponds to different types of restaurants from sushi shops to cafes. You may notice here that you can alternatively select a catagory that encompasses several types of restraunts.
legend3 = {}
for i in root.findall(".//CLASS_OBJ[@id='cat02']//"):
    legend3[i.attrib.get('name')]=i.attrib.get('code')
#Finally, the last legend corrisponds to all the prefectures in Japan and one code for the entire country, "全国".
legend4 = {}
for i in root.findall(".//CLASS_OBJ[@id='area']//"):
    legend4[i.attrib.get('name')]=i.attrib.get('code')
#I want to bundle up all four dictionaries in another dictionary indexed by number to call later.
legends = {1 : legend1 , 2 : legend2, 3 : legend3, 4 : legend4}
legendkeys1 = list(legend1.keys())
legendkeys2 = list(legend2.keys())
legendkeys3 = list(legend3.keys())
legendkeys4 = list(legend4.keys())
masterlist=[legendkeys1, legendkeys2, legendkeys3, legendkeys4]

s=[]
b=['tab','cat01','cat02','area']
for t in b:
    for i in root.findall(".//CLASS_OBJ[@id='{}']".format(t)):
        s.append(i.attrib['name'])
d=1
t=[]
for i in s:
    t.append('[{}]'.format(d)+i)
    d += 1
print(t)
print('上のリストから変数を選択してください。他は定数になります（例：１)')
var = int(input())
variable = s[var-1]
print(s[var-1] + 'を選択しました')
const = [1,2,3,4]
del const[var-1]
constants=[]
constnum=[]
for i in const:
    d=1
    h=[]
    for l in masterlist[i-1]:
        h.append('[{}]'.format(d)+l)
        d += 1
    print(h)
    k = int(input())
    constants.append(masterlist[i-1][k-1])
    constnum.append(k)
