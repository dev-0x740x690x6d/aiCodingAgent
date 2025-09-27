import sys
import os
from functions.config import *

absolute_directory = ABSOLUTE_DIRECTORY_CONFIG

def write_file(working_directory, file_path, content):
    if type(working_directory) != str or type(file_path) != str or type(content) != str:
        return print(f"Error: The {working_directory}(Working Directory), {file_path}(File Path) or {content}(content) was not formatted as a string")
    if os.path.abspath(os.path.join(working_directory, file_path)).startswith(absolute_directory) == False:
        return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if len(content) > MAX_CHAR_READ_LIMIT:
        return print('Error: Content to be written to fie is too long.')
    if os.path.exists(os.path.abspath(working_directory)) == False:
        os.makedirs(os.path.join(working_directory))
        if os.path.exists(os.path.abspath(working_directory)) == False:
            return print('Error: Unable to create the parent directories for this file.')
    with open(os.path.abspath(os.path.join(working_directory, file_path)), "w") as f:
        f.write(content)
        f.close()
    with open(os.path.abspath(os.path.join(working_directory, file_path)), "r") as f:
        if f.read(MAX_CHAR_READ_LIMIT) == content:
            return print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
        else:
            return print('Error: The content was not written to the file. Please try again.')