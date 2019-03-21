# Import utils
from utils.inputUtils import get_input_data


# File name of csv input file within the input directory
input_filename = "test_data.csv"
# Get Data specific for this project structure
input_data = get_input_data(input_filename)

print(input_data)









# TODO Wait for more detailed data to build full data model
# Current suggestion List of dicts where all possible information are keys that only exists if the info is available


# Possible lib for bayesian networks
# https://pomegranate.readthedocs.io/en/latest/BayesianNetwork.html
# https://pypi.org/project/bayespy/ | http://www.bayespy.org/intro.html
# http://pgmpy.org/models.html
