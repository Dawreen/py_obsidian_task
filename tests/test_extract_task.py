from py_obsidian_task.extract_task import extract_tasks

def main():
    tasks = extract_tasks(".")
    for task in tasks:
        print(task)

if __name__ == "__main__":
  main()
