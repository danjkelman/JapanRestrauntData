import os
import pandas as pd
#sys patch for my PC
import sys
sys.__stdout__ = sys.stdout
from xml.etree import ElementTree
file_name='getStatsData.xml'
full_file = os.path.abspath(os.path.join(file_name))
dom = ElementTree.parse(full_file)
root = dom.getroot()
#might edit it to make it based on user input of either code or name
tr = "1106"
t2r = "812"
c1r = "000"
c2r = "17770"
g=[]
def make_list(t,c1,c2):
        #makes g a dictionary that holds values and variable/constants IDs
        for i in root.iter('VALUE'):
                teep = i.attrib
                if teep.get('tab') == t and teep.get('cat01') == c1 and teep.get('cat02') == c2:
                        teep['value'] = i.text
                        #del teep['tab']
                        #del teep['cat01']
                        #del teep['cat02']
                        #del teep['time']
                        g.append(teep)
        p={}
        #makes p a dictionary to convert theses IDs into their corrisponding names
        for i in root.iter('CLASS'):
                tpo = i.attrib
                p[tpo.get('code')] = tpo.get('name')
        #replaces area code with name
        for i in g:
                i['area']=p.get(i['area'])
        q = []

        r=[]
        for i in range(len(g)):
                r.append([])
                r[-1].append(g[i].get('area'))
                r[-1].append(int(g[i].get('value')))
        h=[]
        #patch for when this function is called several times
        for i in range(len(r)):
                if r[i][0] != None:
                        h.append(r[i])
        return h
ramen = make_list(tr, c1r, c2r)
print(ramen)

