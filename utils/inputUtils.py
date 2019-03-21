# Utils file
import csv
import os


def csv_to_list(file_path):
    """
    Takes a file path to a csv file and returns an array of the data within the csv file
    :param file_path: path to a csv file as string
    :return: list of lists for each input data (Python list aka "array")
    """
    # Error Checking for file_path parameter
    if not isinstance(file_path, str):
        raise TypeError("File path parameter is not of type string but instead of type " + str(type(file_path)))
    if not file_path:
        raise ValueError("File path is an empty string, please enter an actual file path!")
    if not os.path.isfile(file_path):
        raise ValueError("The file path does not point to an actual file! File path: " + file_path)
    file_extension = os.path.splitext(file_path)[1]
    if not file_extension:
        raise TypeError("The file extension is not '.csv'! Current file extension: " + file_extension)

    # The actual csv format is not check directly but indirectly by the csv library! This can be changed later on
    with open(file_path) as csvfile:
        data = list(csv.reader(csvfile))

    # Test if data is actual an list of lists
    if not isinstance(data, list):
        raise TypeError(
            "Error something went wrong! The data is not of type list. The csv format must be incorrect.Data format: "
            + str(type(data)))
    for date in data:
        if not isinstance(date, list):
            raise TypeError(
                "The data within the csv is not of type list. The csv format must be incorrect. Data format: "
                + str(type(data)))

    # The content of the data is not checked within this function.
    return data


def get_input_data(file_name):
    """
    Function to get data from csv file. Build for the current project structure.
    :return: List of lists (python list) from the csv file
    """
    if not isinstance(file_name, str):
        raise TypeError("File name parameter is not of type string but instead of type " + str(type(file_name)))
    if not file_name:
        raise ValueError("File name is an empty string, please enter an actual file name!")

    # Get absolute file path for the current project structure (HARD CODED)
    full_filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'input', file_name)

    # Get Input
    csv_content = csv_to_list(full_filepath)
    if not csv_content:
        raise ValueError("CSV file is empty. Please enter a valid and filled csv file path!")

    return csv_content
