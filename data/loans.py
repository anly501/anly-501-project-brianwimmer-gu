#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:50:51 2022

@author: brianwimmer
"""

# Import libraries
import pandas as pd
import numpy as np

# Read in loans.csv
loans = pd.read_csv('/Users/brianwimmer/Desktop/data/loans.csv')

# rename columns
loans.rename(columns = {'id':'loan_id', 'amount':'loan_amount', 'payments':'loan_payments'}, inplace = True)

# make values with '-' empty
loans = loans.replace('-', '')

# replace X in column values with column name
loans['24_A'] = loans['24_A'].replace(['X'],'24A')
loans['12_B'] = loans['12_B'].replace(['X'],'12B')
loans['12_A'] = loans['12_A'].replace(['X'],'12A')
loans['60_D'] = loans['60_D'].replace(['X'],'60D')
loans['48_C'] = loans['48_C'].replace(['X'],'48C')
loans['36_D'] = loans['36_D'].replace(['X'],'36D')
loans['36_C'] = loans['36_C'].replace(['X'],'36C')
loans['12_C'] = loans['12_C'].replace(['X'],'12C')
loans['48_A'] = loans['48_A'].replace(['X'],'48A')
loans['24_C'] = loans['24_C'].replace(['X'],'24C')
loans['60_C'] = loans['60_C'].replace(['X'],'60C')
loans['24_B'] = loans['24_B'].replace(['X'],'24B')
loans['48_D'] = loans['48_D'].replace(['X'],'48D')
loans['24_D'] = loans['24_D'].replace(['X'],'24D')
loans['48_B'] = loans['48_B'].replace(['X'],'48B')
loans['36_A'] = loans['36_A'].replace(['X'],'36A')
loans['36_B'] = loans['36_B'].replace(['X'],'36B')
loans['60_B'] = loans['60_B'].replace(['X'],'60B')
loans['12_D'] = loans['12_D'].replace(['X'],'12D')
loans['60_A'] = loans['60_A'].replace(['X'],'60A')

# create loan_term column
loans['loan_term1'] = loans[['24_A', '12_B', '12_A', '60_D', '48_C', '36_D', '36_C', '12_C', '48_A', '24_C', '60_C', '24_B', '48_D', '24_D', '48_B', '36_A', '36_B', '60_B', '12_D', '60_A']].agg(' '.join, axis=1)

# remove whitespace from loan_term
loans['loan_term1'] = loans['loan_term1'].str.strip()

# split loan_term into two columns
loans['loan_term']=loans['loan_term1'].str.slice(stop=2)
loans['loan_status']=loans['loan_term1'].str.slice(start=2)

# remove unnecessary columns
loans = loans.drop(loans.columns[5:26], axis=1)

# create loan_default column
loans['loan_default'] = np.where((loans["loan_status"] == 'B') | (loans["loan_status"] == 'D'), True, False)

# change to expired/current for loan_status
loans.loc[loans['loan_status'] == 'A', 'loan_status'] = 'expired'
loans.loc[loans['loan_status'] == 'B', 'loan_status'] = 'expired'
loans.loc[loans['loan_status'] == 'C', 'loan_status'] = 'current'
loans.loc[loans['loan_status'] == 'D', 'loan_status'] = 'current'

# write loans to loans_py.csv
loans.to_csv('/Users/brianwimmer/Desktop/data/codes-and-outputs/loans_py.csv', index=False)
















