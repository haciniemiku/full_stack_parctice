"""
Author: Cao Boyuan
Date: 2025-08-18
Description: Integrated exercises / small project
"""
# -------------------------------
# Project 3: Todo List CLI
# -------------------------------
tasks = []

def add_task(task):
    tasks.append(task)

def del_task(index):
    if 0<= index<len(tasks):
        del tasks[index]
    else:
        print("Invalid task index.")

def show_tasks():
    if not tasks:
        print('No tasks available.')
    else:
        for i,task in enumerate(tasks):
            print(f'{i}:{task}')

def main():
    while True:
        command=input("Enter command (add/del/show/exit): ").strip().lower()
        if command=='add':
            task=input('Enter task: ').strip()
            add_task(task)
        elif command=='del':
            index=int(input('Enter task index to delete: ').strip())
            del_task(index)
        elif command=='show':
            show_tasks()
        elif command=='exit':
            break
        else:
            print('Unknown command.')

if __name__=='__main__':
    main()