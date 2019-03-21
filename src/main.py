# Import utils
from utils.inputUtils import get_input_data


# File name of csv input file within the input directory
input_filename = "test_data.csv"
# Get Data specific for this project structure
input_data = get_input_data(input_filename)

print(input_data)
