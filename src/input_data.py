import yaml
import os
class InputData:
    def __init__(self):
        self.model_file = None     # input python model file (or wrapped external code)
        self.names = []                 # names od parameters
        self.numvar = None                # number of dimensions (variables)
        self.parameters_bounds = []     # upper and lower bound
        self.distr = []               # distribution type (default uniform)
        self.directory = None
        self.num_samples = None
        
    def read_config_file(self):
        cwd = os.getcwd()
        with open(cwd + '/../config.yaml', 'r') as filename:
            configuration = yaml.load(filename, Loader=yaml.FullLoader)
        self.directory = configuration['model_directory']
        self.model_file = configuration['model_file']
        self.num_samples = configuration['num_samples']
        return configuration["parameter"]
    
    def inputs_salib(self):
        param_list = self.read_config_file()
        for par in param_list:
            self.parameters_bounds.append(par['bounds'])
            self.names.append(par['name'])
            self.distr.append(par['distribution'])
        self.numvar = len(self.names)
    
        problem = {'num_vars': self.numvar,
                       'names': self.names,
                       'bounds': self.parameters_bounds,
                       #'dists': self.distr
                       }
        print("READY FOR SALib!")
        print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in problem.items()) + "}")
        return problem
    
if __name__=='__main__':        # kontrola formatu vystupu
    inputs = InputData()
    inputs.inputs_salib()
