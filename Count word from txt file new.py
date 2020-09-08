# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 21:05:45 2020

@author: VICKY JUNGHARE
"""
import pandas as pd


file="C:/Users/VICKY JUNGHARE/Documents/Speech/31 may 2020.txt"

dataset = pd.read_csv(file,delimiter = '\t', quoting = 3)


dataset.columns.values[0] = "new_name"

df=dataset.new_name
df = df.str.replace(',', '').str.replace('.', '').str.lower()

df=df.tolist()

df123 = pd.DataFrame([sub.split(" ") for sub in df])

n=len(df123) 
m=len(df123.columns) 

result = []
for i in range(m):
    for j in range(n):
        x=df123[i][j]
        if x!= None :
            result.append(x)
        else:
            j=j+1
            
result.sort() 

p=len(result)
count1=0
count2=0
count3=0
count4=0
count5=0
count6=0
count7=0
count8=0


word="economy"
for k in range(p):
    if result[k]==word:
        count1=count1+1
word="aatmanirbhar"
for k in range(p):
    if result[k]==word:
        count2=count2+1
word="education"
for k in range(p):
    if result[k]==word:
        count3=count3+1        
word="nep"
for k in range(p):
    if result[k]==word:
        count4=count4+1
word="doctors"
for k in range(p):
    if result[k]==word:
        count5=count5+1
word="farmers"
for k in range(p):
    if result[k]==word:
        count6=count6+1
word="china"
for k in range(p):
    if result[k]==word:
        count7=count7+1
word="trump"
for k in range(p):
    if result[k]==word:
        count8=count8+1
        
print(file, "Economy=", count1,"Aatmanirbhar=",count2,"Education(NEP)=",count3+count4,"Doctors=",count5,"Farmers=",count6,"China=",count7,"Trump=",count8)


