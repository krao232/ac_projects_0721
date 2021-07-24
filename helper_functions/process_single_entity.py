import pandas as pd
from helper_functions.get_kg_synonyms import *
from tqdm.notebook import tqdm
import copy

def get_single_entity_expansion(df_input): 
    df = copy.deepcopy(df_input)
    df['syns'] = [get_kg_synonyms(n) for n in tqdm(df.orig)]
    df = df.explode('syns')
    
    substrings = [] 
    for orig, syn in df.to_numpy(): 
        subs = df[df.orig == orig].syns.tolist()
        subs.remove(syn)
        lis = []
        for elem in subs: 
            if syn in elem: 
                lis.append(elem)
        substrings.append(','.join(lis))
    df['substrings'] = substrings
    df = df.drop_duplicates('syns')
    return df

def process_single_entity(df_input): 
    df = get_single_entity_expansion(df_input)
    df = df.reset_index().drop('index', axis = 1)
    
    test = df.sample(frac = 0.1)
    train = df.drop(test.index)
    
    return train, test
    