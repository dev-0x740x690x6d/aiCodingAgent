import sys
import os
from functions.config import MAX_CHAR_READ_LIMIT

absolute_directory = '/app/bootDevAIAgent/calculator'

def get_file_content(working_directory, file_path):
    if type(working_directory) != str or type(file_path) != str:
        return print(f"Error: Either {working_directory}(Working Directory) or {file_path}(File Path) were not formatted as a string")
    if os.path.isfile(os.path.abspath(os.path.join(working_directory, file_path))) == False:
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    if os.path.abspath(os.path.join(working_directory, file_path)).startswith(absolute_directory) == False:
        return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    truncated_message = f'[...File "{file_path}" truncated at 10000 characters]'
    with open(os.path.abspath(os.path.join(working_directory, file_path)), "r") as f:
        file_content_string = f.read(MAX_CHAR_READ_LIMIT + 1)
        if len(file_content_string) > MAX_CHAR_READ_LIMIT:
            file_content_string = file_content_string[:-1]
            file_content_string += f'\n {truncated_message}'
        return print(file_content_string)
    