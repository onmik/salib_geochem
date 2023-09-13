import subprocess
import pandas as pd
from re import sub


def run_model(X_1, X_2):
    
    #----------------prepares the model file----------------
    f1 = open('ex13a','r')          # original file
    f1_read = f1.read()
    f1.close()
    f2 = open("outa", "w")          # file to run model
    def replace_param(dict_replace, target):
        for old_param, new_param in list(dict_replace.items()):
            target = sub(old_param, new_param, target)
        return target
    dict_replace = {
        'X_1': str(X_1),
        'X_2': str(X_2)
        }
    f2.write(replace_param(dict_replace, f1_read))
    f2.close() 
    
    #------------------- runs simulation------------------------
    subprocess.run(["bash", "-c", "phreeqc outa"])
    
    #----------------- write quantity of interest to be evaluated-----------------
    out_data = pd.read_csv("ex13a.sel", skiprows=1, header=None, delim_whitespace=True)
    out_data = out_data.iloc[38]
    out_data = out_data.loc[2]
    #pH_data = float(pH_data)
    return out_data 



