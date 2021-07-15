import numpy as np
import pandas as pd

# takes state name and dataframe as parameters, returns list of total state dry population
def get_dry_pop(state, county_pops):
    i = 0 
    sum = []
    while i < county_pops.shape[0]:
        if state == county_pops['state'][i]:
            if county_pops['pop1910'][i] != 0:
                dry_pop = county_pops['proh1910'][i] * county_pops['pop1910'][i]
            else:
                dry_pop = 0
            sum.append(int(dry_pop))
        i += 1
    return sum

#takes state name, list of dry pops, and state population dataframe; returns percent dry
def get_percent_dry(dry_pops, state_pops, state):
    total_dry_pop = 0
    i = 0
    pop_index = 0
    index = 0
    while index < state_pops.shape[0]:
        if state == state_pops['state'][index]:
            pop_index = index
        index += 1
        while i < len(dry_pops):
            total_dry_pop = total_dry_pop + dry_pops[i]
            i += 1
    percent_dry = total_dry_pop / state_pops['pop1910'][pop_index]
    return percent_dry


# Dictionary of state populations
state_pops = pd.read_csv("state_pops.csv")
percent_dry_dataset = pd.read_csv("percent_dry_dataset_1910.csv")

#list of state names
state_names = ["Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Iowa", "Idaho", "Illinois", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

#set desired state
state = "West Virginia"

print("Here is the dry percentage of the population of:", state)
print(get_percent_dry(get_dry_pop(state, percent_dry_dataset), state_pops, state))

