from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

from input_data import InputData


def run_saltelli():

    inputs = InputData()
    problem = inputs.inputs_salib()
    samples = inputs.num_samples
    model_dir = inputs.directory         # directory with all model files,  should be  separate for each model

    sys.path.insert(0, model_dir)
    os.chdir(model_dir)
    model = model_dir +'/'+ inputs.model_file 
    import model as m
    
    parameter_values = saltelli.sample(problem, samples, calc_second_order=False)

    out_array = np.zeros([parameter_values.shape[0], 1])
    for i, param in enumerate(parameter_values):
        out_array[i] = m.run_model(*param)

    SI = sobol.analyze(problem, out_array[:,0], print_to_console=True, calc_second_order=False)

    SI.plot()

if __name__=='__main__': 
    run_saltelli()

