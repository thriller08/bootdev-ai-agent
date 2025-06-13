import os
import subprocess
from pathlib import Path

def run_python_file(working_directory, file):
    try:
        work_dir_path = os.path.abspath(Path(working_directory).resolve(strict=True))
        file_path = os.path.abspath(os.path.join(work_dir_path, file))
    except:
        return "Error: Cannot resolve working directory"

    if not file_path.startswith(work_dir_path):
        return f'Error: Cannot execute "{file}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path):
        return f'Error: File "{file}" not found'

    if not file_path.endswith(".py"):
        return f'Error: "{file}" is not a Python file'

    try:
        output = subprocess.run(["python", file_path], capture_output=True, cwd=work_dir_path, text=True, timeout=30)
    except Exception as e:
        return f'Error: executing python file: {e}'

    response = f'STDOUT:\n{output.stdout}\nSTDERR:\n{output.stderr}'
    if output.returncode != 0:
        response += f'\nProcess exited with code {output.returncode}'

    if len(output.stdout) == 0 and len(output.stderr) == 0:
        response = 'No output produced.'

    return response
