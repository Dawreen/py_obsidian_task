from py_obsidian_task.google_tasks import google_tasks


def main():
    all_tasks = google_tasks()
    if all_tasks != None:
        for task in all_tasks:
            print(task['title'])

if __name__ == "__main__":
  main()
