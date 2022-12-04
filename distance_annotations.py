"""
To calculate  the distance between 2 documents ann1 et ann2, the tokens don't change so just gonna calculate the distance between 2 vectors 
of the good column in the dataframe
"""

import pandas as pd
from scipy.spatial import distance
from difflib import SequenceMatcher
import glob


path = r'/home/mathilde/Documents/terminology & ontology/set_dist' # use your path
all_ann1 = glob.glob(path + "/*.ann1")
all_ann1 = sorted(all_ann1)
all_ann2 = glob.glob(path + "/*.ann2")
all_ann2 = sorted(all_ann2)
all_finals = glob.glob(path + "/*.final")
all_finals = sorted(all_finals)


def get_in_df():
    list_ann1 = []
    list_ann2 = []
    list_final = []
    cols = ['Token', 'Tag']
    # for ann1
    for filename in all_ann1:
        df = pd.read_csv(filename, names = cols,on_bad_lines='skip', sep='\s+', engine='python')
        list_ann1.append(df)

    # for ann2
    for filename in all_ann2:
        df = pd.read_csv(filename, names = cols,on_bad_lines='skip', sep='\s+', engine='python')
        list_ann2.append(df)

    # for finals
    for filename in all_finals:
        df = pd.read_csv(filename, names = cols,on_bad_lines='skip', sep='\s+', engine='python')
        list_final.append(df)

    return list_ann1, list_ann2, list_final


def compute_dist(list1, list2):
    list_dist = []
    for i in range(len(list1)):
        df1 = list1[i]
        tag_val1 = df1['Tag'].values
        df2 = list2[i]
        tag_val2 = df2['Tag'].values
        dist = SequenceMatcher(None, tag_val1, tag_val2).ratio()
        list_dist.append(dist)

    dist = sum(list_dist)/len(list_dist)
    return dist

# Preprocessing
l_ann1, l_ann2, l_final = get_in_df()

# computations
sm_ann1_ann2 = compute_dist(l_ann1, l_ann2)
sm_ann1_final = compute_dist(l_ann1, l_final)
sm_ann2_final = compute_dist(l_ann2, l_final)

print(round(sm_ann1_ann2, 4))
print(round(sm_ann1_final, 4))
print(round(sm_ann2_final, 4))



