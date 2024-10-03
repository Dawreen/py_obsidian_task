from py_obsidian_task.markdown_tasks import extract_tasks

def main():
    tasks_dict = extract_tasks(".")
    for key, value in tasks_dict.items():
        print(f'key: {key}, value: {value}')

if __name__ == "__main__":
  main()
