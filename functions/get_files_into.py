import sys
import os

absolute_directory = '/app/bootDevAIAgent/calculator'

def get_files_info(working_directory, directory="."):
    if type(working_directory) != str or type(directory) != str:
        return print(f"Error: Either {working_directory}(Working Directory) or {directory}(Directory) were not formatted as a string")
    if os.path.isdir(os.path.abspath(os.path.join(working_directory, directory))) == False:
        return print(f'Error: "{directory}" is not a directory')
    if os.path.abspath(os.path.join(working_directory, directory)).startswith(absolute_directory) == False:
        return print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    items_list = []
    for item in os.listdir(os.path.join(working_directory, directory)):
        item_string = ''
        item_string = f'- {item}: '
        item_string += f'size={os.path.getsize(os.path.join(working_directory, directory, item))} bytes, '
        if os.path.isdir(os.path.join(working_directory, directory, item)) == True:
            item_string += f'is_dir=True'
        else:
            item_string += f'is_dir=False'
        items_list.append(item_string)
    
    return print(*items_list, sep='\n')