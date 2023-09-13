import os
import runSALib 
import yaml

cwd = os.getcwd()
with open(cwd + '/../config.yaml', 'r') as filename:
    configuration = yaml.load(filename, Loader=yaml.FullLoader)

if configuration['sobol_saltelli']:
    runSALib.run_saltelli()

