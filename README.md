Name: Vivek Milind Aher

#Assignment Discription
This Python package is designed to interact with the FBI's Most Wanted API to retrieve information about most wanted individuals. The package provides functionality to either download data from the FBI’s API or load it from a local JSON file, extract relevant information, and then print the results in a specific format. The information extracted includes the title of the wanted person, the subjects (reasons for being wanted), and the field offices involved, all formatted in a thorn-separated output (þ).

#how to Install
To run this program, you will need Python 3.12 and the requests library installed.
Install Python 3.12 from the official Python website.
Install the required Python library requests using pip
Download or clone this package
Navigate to the directory containing the package


#How to run
There are two ways to run the program:
1. Fetch data from the FBI API by page number:
Run the following command:
python main.py --page <N>
Where <N> is the page number you want to retrieve
Example:
python main.py --page 1

2. Load data from a local JSON file:
You can specify a file location containing the JSON data for testing purposes:
python main.py --file <path-to-json-file>
Example: 
python main.py --file test_data.json
This will load the data from the JSON file and print it in the thorn-separated format.


#Functions

def get_data_from_url(url, page):
Sends a GET request to the FBI API using the requests library to retrieve data from the specified page. The page number is passed as a parameter to get the results.
If the response status is not 200 (success), it prints "failed" and returns nothing. Otherwise, it returns the JSON data.

def get_data_from_json(filepath):
Loads JSON data from the provided file path. Useful for testing without accessing the live API.
Returns the parsed JSON data.

def extract_title(record):
Extracts the title from a given record in the dataset. If no title is found, it returns an empty space (' ').

def extract_subjects(record):
Extracts the subjects from a record. If no subjects are found, it returns a list with an empty space (' ').
Joins the list of subjects into a comma-separated string for easier reading.

def extract_field_offices(record):
Extracts the field_offices from a record. If no field offices are found, it returns a list with an empty space (' ').
Joins the field offices into a comma-separated string.

def output_print(response):
Iterates over the items in the response data and extracts the title, subjects, and field offices for each record.
Formats the extracted information into a thorn-separated string and prints it to the standard output.

def main(page = None, thefile = None):
This function serves as the main entry point. Depending on the command-line arguments, it either fetches data from the API or loads data from a local JSON file.
It writes the API response to a JSON file (test.json) if the page parameter is provided and prints the output.
Calls output_print to print the data in the desired format.



#Assumptions:

The API or file always provides valid JSON data.
The fields title, subjects, and field_offices exist in each record, although they might be empty.
Only one of the parameters --page or --file will be provided at a time. If both are provided, only the first will be processed.

#Approach:

I used the requests library to fetch data from the FBI API and json to handle JSON data.
The program extracts and formats only the specified fields: title, subjects, and field_offices. The formatting follows the thorn-separated format as required.
Output is printed directly to the console using the print() function.

