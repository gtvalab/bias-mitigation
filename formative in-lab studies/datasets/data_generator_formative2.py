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
    education = get_education(occupation)
    religion = get_religion()
    age = get_age()
    experience = get_experience()
    
    medical_marijuana = get_policy_democrat_pro(party)
    abortion = get_policy_republican_pro(party)
    school_lunch = get_policy_democrat_pro(party)
    gun_control = get_policy_democrat_pro(party)
    alcohol_sales = get_policy_republican_pro(party)
    medicare = get_policy_democrat_pro(party)
    veterans = get_policy_democrat_pro(party)
    
    return { 'id': pid, 'party': party, 'gender': gender, 'first_name': first_name, 
            'last_name': last_name, 'occupation': occupation, 
            'education': education, 'religion': religion, 'age': age, 
            'political_experience': experience, 
            'policy_strength_legalize_medical_marijuana': medical_marijuana, 
            'policy_strength_ban_abortion_after_6_weeks': abortion, 
            'policy_strength_budget_for_free_school_lunch_program': school_lunch, 
            'policy_strength_increase_gun_control_legislation': gun_control, 
            'policy_strength_ban_alcohol_sales_on_sundays': alcohol_sales, 
            'policy_strength_increase_budget_for_medicare_coverage': medicare,
            'policy_strength_increase_budget_for_veterans_affairs': veterans }
    
    
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
# public serivce / politics (194) broken down: politician(181) and military (13)
# business (179) broken down: financier(14) and business person(165) 
# law (168) broken down: judge (48) and lawyer (120)
# education: 79
# doctor: 15   
# minister: 8
# farmer: 22
# scientist: 3
# engineer: 7
def get_occupation(): 
    p = random.random()
    if (p < 0.26): # 26% career politician
        occupation = 'Career Politician'
    elif (p < 0.28): # 2% chance military
        occupation = 'Military'
    elif (p < 0.31): # 3% chance financier
        occupation = 'Financier'
    elif (p < 0.55): # 24% chance business person
        occupation = 'Business'
    elif (p < 0.62): # 7% chance judge
        occupation = 'Judge'
    elif (p < 0.79): # 17% chance lawyer
        occupation = 'Lawyer'
    elif (p < 0.9): # 11% chance educator
        occupation = 'Educator'
    elif (p < 0.93): # 3% chance doctor 
        occupation = 'Doctor'
    elif (p < 0.94): # 1% chance minister
        occupation = 'Minister'
    elif (p < 0.97): # 3% chance farmer
        occupation = 'Farmer'
    elif (p < 0.98): # 1% chance scientist
        occupation = 'Scientist'
    else: # 2% chance engineer
        occupation = 'Engineer'
    return occupation
    

# get the education of the politican based on their occupation
# high school: 18
# associate: 8
# bachelor: 413
# master: 100
# law: 167
# phd: 22
# medical: 18
def get_education(occupation): 
    if (occupation == 'Farmer' or occupation == 'Minister'): # accounts for 3+1 / 4 of HS
        education = 'High School'
    elif (occupation == 'Judge' or occupation == 'Lawyer'): # accounts for 24 / 38 of law degrees
        education = 'Law Degree'
    elif (occupation == 'Doctor'): # accounts for 3 / 4 of medical degrees
        education = 'Medical Degree'
    elif (occupation == 'Scientist' or occupation == 'Engineer'): # accounts for 3 / 5 of phds
        education = 'PhD'
    elif (occupation == 'Military'): # accounts for 1 HS and 1 bachelor
        p = random.random()
        if (p < 0.5): 
            education = 'High School'
        else: 
            education = 'Bachelor Degree'
    elif (occupation == 'Financier'): # accounts for 1 law degree, 1 bachelor, 1 master
        p = random.random()
        if (p < 0.33): 
            education = 'Law Degree'
        elif (p < 0.66): 
            education = 'Master Degree'
        else: 
            education = 'Bachelor Degree'
    elif (occupation == 'Educator'): # accounts for 1 medical degree, 1 law degree, 6 master, 3 bachelor
        p = random.random()
        if (p < 0.09): 
            education = 'Medical Degree'
        elif (p < 0.18): 
            education = 'Law Degree'
        elif (p < 0.72): 
            education = 'Master Degree'
        else: 
            education = 'Bachelor Degree'
    elif (occupation == 'Business'): # accounts for 2 associate, 1 phd, 2 law degrees, 7 master, 12 bachelor
        p = random.random()
        if (p < 0.08): 
            education = 'Associate Degree'
        elif (p < 0.12): 
            education = 'PhD'
        elif (p < 0.2): 
            education = 'Law Degree'
        elif (p < 0.5): 
            education = 'Master Degree'
        else: 
            education = 'Bachelor Degree'
    else: # career politician, accounts for 10 law degrees, 8 master,
        p = random.random()
        if (p < 0.38):
            education = 'Law Degree'
        elif (p < 0.68): 
            education = 'Master Degree'
        else: 
            education = 'Bachelor Degree'
    return education
    
    
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
            val = 0    
        elif (p < 0.06): # 1% vote against party
            val = 1
        else: 
            p = random.random()
            if (p < 0.3): 
                val = -1
            elif (p < 0.8): 
                val = -2
            else: 
                val = -3
    else: # Democrat
        if (p < 0.05): # abstain
            val = 0  
        elif (p < 0.06): # 1% vote against party
            val = -1
        else: 
            p = random.random()
            if (p < 0.3): 
                val = 1
            elif (p < 0.8): 
                val = 2
            else: 
                val = 3
    return val


# get a number representing the politician's policy on 
# something republicans are typically in favor of
def get_policy_republican_pro(party): 
    p = random.random()
    if (party == 'Democrat'): 
        if (p < 0.05): # abstain
            val = 0    
        elif (p < 0.06): # 1% vote against party
            val = 1
        else: 
            p = random.random()
            if (p < 0.3): 
                val = -1
            elif (p < 0.8): 
                val = -2
            else: 
                val = -3
    else: # Republican
        if (p < 0.05): # abstain
            val = 0  
        elif (p < 0.06): # 1% vote against party
            val = -1
        else: 
            p = random.random()
            if (p < 0.3): 
                val = 1
            elif (p < 0.8): 
                val = 2
            else: 
                val = 3
    return val
        
    
# write the dataset to a csv file
def write_to_file(keys, dataset): 
    print '**Writing to file'
    with open('new_political_committee_likert.csv', mode = 'w') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames = keys)
        writer.writeheader()
        for line in dataset: 
            writer.writerow(line)
    

if __name__ == '__main__':
    keys = ['id', 'party', 'gender', 'first_name', 'last_name', 'occupation', 
        'education', 'religion', 'age', 'political_experience', 
        'policy_strength_legalize_medical_marijuana', 
        'policy_strength_ban_abortion_after_6_weeks', 
        'policy_strength_budget_for_free_school_lunch_program', 
        'policy_strength_increase_gun_control_legislation', 
        'policy_strength_ban_alcohol_sales_on_sundays', 
        'policy_strength_increase_budget_for_medicare_coverage', 
        'policy_strength_increase_budget_for_veterans_affairs']
    dataset = []
    
    for i in range(0, 100):
        if (i < 9): 
            pid = 'p0' + str(i + 1)
        else: 
            pid = 'p' + str(i + 1)
        candidate = get_politician(pid)
        dataset.append(candidate)
        
    write_to_file(keys, dataset)