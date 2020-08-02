# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 10:33:31 2020

@author: David Fong, Rachel ChengJie Ren, Cesar Martinez, Bruce Bothwell
""" 

import os
import pandas as pd

os.getcwd()
    
spending = pd.read_csv('DataFiles/Police_Spending.csv',low_memory=False)
spend_corr = spending.corr()

colToDrop = ['DETAILED ITEM DESCRIPTION','VENDOR NUM']
myFile = myFile.drop(colToDrop,axis=1)
len(myFile.columns)

crimeData = pd.read_csv('DataFiles/Crime_Data_from_2020_to_Present.csv')
crimeDataCorr = crimeData.corr()

with pd.ExcelWriter('DataFiles/Correlations.xlsx') as writer:
    spend_corr.to_excel(writer,sheet_name='spendingCorr')
    crimeDataCorr.to_excel(writer,sheet_name='crimeDataCorr')




