import os
from pathlib import Path

def get_file_content(working_directory, file):
    try:
        work_dir_path = os.path.abspath(Path(working_directory).resolve(strict=True))
        file_path = os.path.abspath(os.path.join(work_dir_path, file))
    except:
        return "Error: Cannot resolve working directory"

    if not file_path.startswith(work_dir_path):
        return f'Error: Cannot read "{file}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file}"'

    MAX_CHARS = 10000
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) == MAX_CHARS:
                file_content_string = file_content_string + f'[...File "{file}" truncated at 10000 characters]'
    except:
        return f'Error: Error reading file: "{file}"'

    return file_content_string

