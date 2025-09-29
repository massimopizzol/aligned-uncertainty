#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import bw2calc as bc
import bw2data as bd
import bw2io as bi
import bw_processing as bwp
from bw2data.parameters import *
from bw2data.backends.schema import ExchangeDataset

"""
@author: Rebecca Belfiore, INSAT 2025
"""

def parameters_to_bw(df):
    '''
    This function allows to import Activity parameters in an existing database.
    Inputs:
    - df: pandas dataframe which should contain all the infomation relative to the parameters
        at a minimum: group, database, name, amount
        extra fields: uncertainty type, loc, scale, minimum, maximum, formula
    '''

    groups = df['group'].dropna().unique() # list of unique groups
    groups_left = set(groups) # a set of groups that have not yet been imported 

    for group in groups:
        group_df = df[df['group'] == group] # subset of the .csv with only the parameters of the given group

        param_list = [] # get a list of dictionaries containing parameters info
        


        for _, row in group_df.iterrows(): # get the index and the info of every row
            param = {
                'group': group,
                'database': row['database'],
                'name': row['name'],
                'amount': float(row['amount']),
            }

            # save the db name
            mydb = param['database']
            
            # create a code, the code equals the code of the activity to which the group belongs
            for a in bd.Database(mydb):
                for e in a.exchanges():
                    # find out if e is parametrised and get its group
                    if e.get('formula') is not None and param['name'] in str(e.get('formula')):
                        if e['group'] == param['group']:
                            param['code'] = a['code']
                            break

            # if a formula is specified add it
            if pd.notnull(row['formula']):
                param['formula'] = row['formula']

            # Add optional fields for the uncertainty specification
            if pd.notnull(row['uncertainty type']):
                param['uncertainty type'] = int(row['uncertainty type'])

            for field in ['loc', 'scale', 'minimum', 'maximum']:
                if pd.notnull(row[field]):
                    param[field] = float(row[field])

            param_list.append(param) 
        
        # Load the parameters
        parameters.new_activity_parameters(param_list, group)

    for a in bd.Database(mydb):
        for e in a.exchanges():
            # find out if e is parametrised and get its group
            if e.get('formula') is not None:
                e_group = e['group']
                parameters.add_exchanges_to_group(e_group, a)
                break