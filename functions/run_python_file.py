import sys
import os
import subprocess
from functions.config import ABSOLUTE_DIRECTORY_CONFIG

absolute_directory = ABSOLUTE_DIRECTORY_CONFIG

def run_python_file(working_directory, file_path, args=[]):
    if type(working_directory) != str or type(file_path) != str:
        return print(f"Error: Either the {working_directory}(Working Directory) or {file_path}(File Path) were not formatted as a string")
    if os.path.abspath(os.path.join(working_directory, file_path)).startswith(absolute_directory) == False:
        return print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if os.path.exists(os.path.join(working_directory, file_path)) == False:
        return print(f'Error: File "{file_path}" not found.')
    if os.path.join(working_directory, file_path).endswith('.py') == False:
        return print(f'Error: "{file_path}" is not a Python file.')
    args_for_subprocess = [os.path.abspath(os.path.join(working_directory, file_path))]
    for arg in args:
        args_for_subprocess.append(arg)
    try:
        completed_process = subprocess.run(args=["python3", file_path, *args], capture_output=True, text=True, timeout=30, cwd=working_directory)
    except Exception as e:
        f"Error: executing Python file: {e}"
    if completed_process.stdout == None and completed_process.stderr == None:
        return print(*['','No output produced.',''], sep='\n')
    string_to_return = [f'STDOUT: {completed_process.stdout}', f'STDERR: {completed_process.stderr}']
    if completed_process.returncode != 0:
        string_to_return.append(f'Process exited with error code {completed_process.returncode}')
    return print(*string_to_return, sep='\n')
