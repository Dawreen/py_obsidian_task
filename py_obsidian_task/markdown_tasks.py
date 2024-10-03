import os
import re

def extract_tasks(path):
    tasks_dict = {}

    # Walk through all files and subdirectories in the given path
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Find all unchecked boxes and their associated text
                    matches = re.findall(r'- \[ \](.*)', content)

                    # Add tasks to the list, including the file name
                    for task in matches:
                        key = file_path + "|" + task.strip()
                        value = task.strip()
                        tasks_dict.update({key:value})

    return tasks_dict
