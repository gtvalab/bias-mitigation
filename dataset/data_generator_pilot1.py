# -*- coding: utf-8 -*-
"""
Spyder Editor

Writing a script to produce a fictitious dataset of politicians. 
Based on 115th US Congress 
(https://www.senate.gov/CRSpubs/b8f6293e-c235-40fd-b895-6474d0f8e809.pdf)
"""

import random
import numpy as np
import names
import csv

# generate a line in a csv for a politician using the given specifications 
def get_politician_by_spec(pid, party, gender, occupation, experience, abortion):
    first = get_first_name(gender)
    last = get_last_name()
    return { 'id': pid, 'party': party, 'gender': gender, 
            'first_name': first, 'last_name': last, 
            'occupation': occupation, 'political_experience': experience, 
            'policy_strength_ban_abortion_after_6_weeks': abortion }

    
# get a random first name of given the gender of the politician
def get_first_name(gender): 
    if (gender == 'Female'): 
        name = names.get_first_name(gender = 'female')
    else: 
        name = names.get_first_name(gender = 'male')
    return name


# get a random last name
def get_last_name(): 
    last_name = names.get_last_name()
    return last_name
        
    
# write the dataset to a csv file
def write_to_file(keys, dataset, file_name): 
    print '**Writing to file'
    with open(file_name, mode = 'w') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames = keys)
        writer.writeheader()
        for line in dataset: 
            writer.writerow(line)


# generate dataset using combinatorial equality
def generate_equally(): 
    dataset = []
    party_options = ['Democrat', 'Republican']
    gender_options = ['Male', 'Female']
    occupation_options = ['Doctor', 'Lawyer', 'Business', 'Career Politician']
    political_experience_options = [0, 1, 2]
    abortion_options = [-1, 0, 1]
    counter = 1
    
    for party in party_options: 
        for gender in gender_options: 
            for occupation in occupation_options: 
                for experience in political_experience_options: 
                    for abortion in abortion_options: 
                        if counter < 10: 
                            pid = 'p00' + str(counter)
                        elif (counter < 100): 
                            pid = 'p0' + str(counter)
                        else: 
                            pid = 'p' + str(counter)
                        candidate = get_politician_by_spec(pid, party, gender, occupation, experience, abortion)
                        dataset.append(candidate)
                        counter += 1
    return dataset
    

if __name__ == '__main__':
    
    abbrev_keys = ['id', 'party', 'gender', 'first_name', 'last_name', 'occupation', 
                   'political_experience', 'policy_strength_ban_abortion_after_6_weeks']
    file_name = 'new_political_committee_likert_equal.csv'
    
    dataset = generate_equally()
    write_to_file(abbrev_keys, dataset, file_name)