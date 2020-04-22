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


# generate a line in a csv for a politician
def get_politician(pid): 
    party = get_party()
    gender = get_gender(party)
    first_name = get_first_name(gender)
    last_name = get_last_name()
    occupation = get_occupation()
    religion = get_religion()
    age = get_age()
    experience = get_experience()
    
    abortion = get_policy_republican_pro(party)
    
    return { 'id': pid, 'party': party, 'gender': gender, 'first_name': first_name, 
            'last_name': last_name, 'occupation': occupation, 
            'religion': religion, 'age': age, 
            'political_experience': experience, 
            'policy_strength_ban_abortion_after_6_weeks': abortion }
    
    
# get the party of the politician
# 238 R, 201 D in House => 54% R
def get_party(): 
    p = random.random()
    if (p < 0.54): 
        party = 'Republican'
    else: 
        party = 'Democrat'
    return party
    
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


# get the gender of the politician, given the party
# 92 / 439 women in House => 21% total
# 67 / 238 D (28%), 25 / 201 R (12%)
def get_gender(party): 
    p = random.random()
    if (party == 'Democrat'): 
        if (p < 0.28): 
            gender = 'Female'
        else: 
            gender = 'Male'
    else: 
        if (p < 0.12): 
            gender = 'Female'
        else: 
            gender = 'Male'
    return gender


# get the occupation of the politician (many list multiple occupations, picked a subset)
# assume these highest degrees achieved mapped to the associated profession
# doctor: 18 medical degrees -> 4% of total
# scientist: 22 doctoral degrees -> 5% of total
# law (167): law degrees -> 38% of total
# then, of the remaining 232 congressmen, these were reported... split up the proportion accordingly
# public serivce / politics (194): politician -> 43% of remaining -> 100 people -> 23% of total
# business (179): business person -> 40% of remaining -> 93 people -> 21% of total
# education: 79 -> 17% of remaining -> 40 people -> 9% of total
def get_occupation(): 
    p = random.random()
    
    if (p < 0.05): # 5% scientists 
        occupation = 'Scientist'
    elif (p < 0.09): # 4% doctors 
        occupation = 'Doctor'
    elif (p < 0.47): # 38% lawyer 
        occupation = 'Lawyer'
    elif (p < 0.7): # 23% politician 
        occupation = 'Career Politician'
    elif (p < 0.91): # 21% business 
        occupation = 'Business' 
    else: # 9% educator 
        occupation = 'Educator'
        
    return occupation
    
    
# get the religion of the politican
# christian: 88%
# jewish: 6%
# mormon: 2%
# muslim: 1%
# hindu: 1%
# unaffiliated: 2%    
def get_religion(): 
    p = random.random()
    if (p < 0.88): 
        religion = 'Christian'
    elif (p < 0.94): 
        religion = 'Jewish'
    elif (p < 0.96): 
        religion = 'Mormon'
    elif (p < 0.97): 
        religion = 'Muslim'
    elif (p < 0.98): 
        religion = 'Hindu'
    else: 
        religion = 'Unaffiliated'
    return religion
    
    
# get the age of a politician
# average age in House is 57.8 years
# min age 32, max age 87
# assume stdv of 10
# *in equal dataset, range is 32 to 82 uniformly distributed    
def get_age(): 
    mu, sigma = 58, 10
    age = np.random.normal(mu, sigma, 1)[0]
    if (age < 32): 
        age = 32
    if (age > 87): 
        age = 87
    return int(age)


# get the political experience of a politician
# average length of service in House is 9.4 years
# assume stdv of 3
# *in equal dataset, range is 0-19 years uniformly distributed    
def get_experience(): 
    mu, sigma = 9, 3
    experience = np.random.normal(mu, sigma, 1)[0]
    return int(experience)


# get a number representing the politician's policy on 
# something democrats are typically in favor of
def get_policy_democrat_pro(party): 
    p = random.random()
    if (party == 'Republican'): 
        if (p < 0.05): # abstain
            val = 'Neutral'    
        elif (p < 0.06): # 1% vote against party
            val = 'In Favor'
        else: 
            val = 'Opposed'
    else: # Democrat
        if (p < 0.05): # abstain
            val = 'Neutral'
        elif (p < 0.06): # 1% vote against party
            val = 'Opposed'
        else: 
            val = 'In Favor'
    return val


# get a number representing the politician's policy on 
# something republicans are typically in favor of
def get_policy_republican_pro(party): 
    p = random.random()
    if (party == 'Democrat'): 
        if (p < 0.05): # abstain
            val = 'Neutral'  
        elif (p < 0.06): # 1% vote against party
            val = 'In Favor'
        else: 
            val = 'Opposed'
    else: # Republican
        if (p < 0.05): # abstain
            val = 'Neutral' 
        elif (p < 0.06): # 1% vote against party
            val = 'Opposed'
        else: 
            val = 'In Favor'
    return val
        
    
# write the dataset to a csv file
def write_to_file(keys, dataset, file_name): 
    print '**Writing to file'
    with open(file_name, mode = 'w') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames = keys)
        writer.writeheader()
        for line in dataset: 
            writer.writerow(line)


# generate dataset randomly
def generate_randomly(n): 
    dataset = []
    for i in range(0, n): 
        if (i < 9): 
            pid = 'p00' + str(i + 1)
        elif (i < 99): 
            pid = 'p0' + str(i + 1)
        else: 
            pid = 'p' + str(i + 1)
        candidate = get_politician(pid)
        dataset.append(candidate)
    return dataset
    

if __name__ == '__main__':
    all_keys = ['id', 'party', 'gender', 'first_name', 'last_name', 'occupation', 
        'religion', 'age', 'political_experience', 
        'policy_strength_ban_abortion_after_6_weeks']
    
    n = 200
    file_name = 'new_political_committee_likert_distr_3.csv'
    
    dataset = generate_randomly(n)
    write_to_file(all_keys, dataset, file_name)