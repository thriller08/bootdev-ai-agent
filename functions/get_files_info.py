import os
from pathlib import Path

def get_files_info(working_directory, directory=None):
    try:
        work_dir_path = os.path.abspath(Path(working_directory).resolve(strict=True))
        dir_path = os.path.abspath(os.path.join(work_dir_path, directory))
    except:
        return "Error: Cannot resolve working directory"

    if not dir_path.startswith(work_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'

    items = os.listdir(dir_path)
    if len(items) > 0:
        entries = []
        for item in items:
            file = os.path.join(dir_path, item)
            try:
                file_size = os.path.getsize(file)
                is_dir = "False" if os.path.isfile(item) else "True"
                entries.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
            except Exception as e:
                return f'Error: {e}'
    else:
        return f'"{directory}" is empty'
    r"""
    try:
        work_dir_path = Path(working_directory).resolve(strict=True)
    except OSError:
        return f'Error: "{working_directory}" is not a directory'

    try:
        dir_path = Path(directory).resolve(strict=True)

        if not dir_path.is_relative_to(work_dir_path):
            raise Exception("outside working directory")
    except OSError:
    except:

    return "It worked"
    """

    return "\n".join(entries)
