import os
from pathlib import Path

def write_file(working_directory, file, content):
    try:
        work_dir_path = os.path.abspath(Path(working_directory).resolve(strict=True))
        file_path = os.path.abspath(os.path.join(work_dir_path, file))
    except:
        return "Error: Cannot resolve working directory"

    if not file_path.startswith(work_dir_path):
        return f'Error: Cannot write to "{file}" as it is outside the permitted working directory'

    try:
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, "w+") as f:
            bytes_written = f.write(content)
    except:
        return f'Error: Error writing file: "{file}"'

    return f'Successfully wrote to "{file}" ({bytes_written} characters written)'

