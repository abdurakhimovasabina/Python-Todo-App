import sys
from rich.console import Console
from rich.table import Table

console = Console()


def add_task(todos: list[list[str, bool]]) -> None:
    task_name = input('Task Name: ').strip().capitalize()
    todos.append(
        [task_name, False]
    )


def show_tasks(todos: list[list[str, bool]]) -> None:
    table = Table(title="Todos")
    table.add_column("Number")
    table.add_column("Name")
    table.add_column("Status")

    for index, todo in enumerate(todos, start=1):
        if todo[1]:
            table.add_row(str(index), todo[0], "Bajarilgan")
        else:
            table.add_row(str(index), todo[0], "Bajarilmagan")

    console.print(table)


def delete_task(todos: list[list[str, bool]]) -> None:
  show_tasks(todos)
  try:
      num = int(input("number to delete: "))
      if 1 <= num <= len(todos):
          todos.pop(num - 1)
          print("deleted.")
      else:
          print("Invalid number.")
  except:
      print("Enter a valid number.")
       

def update_task(todos: list[list[str, bool]]) -> None:

    show_tasks(todos)
    try:
       num = int(input("number to update: "))
       if 1 <= num <= len(todos):
           task = todos[num - 1]
           name = input("new name(leave blank to keep):").strip()
           if name:
               task[0] = name.capitalize()
           status = input("Done?(y/n): ").lower()
           if status == 'y':
               task[1] == True
           elif status == 'n':
               task[1] = False
           print("Updated.")
       else:
           print("Invalid number.")
    except:
        print("Enter a valid number.")

           
def main():
    todos: list[list[str, bool]] = [
        ["Yugirish", False],
        ["Kitob oqish", True]
    ]

    while True:
        print('----menu----')
        print('1. add task')
        print('2. show task')
        print('3. delete task')
        print('4. update task')
        print('0. exit')

        choice = input("> ")
        if choice == '1':
            add_task(todos)
        elif choice == '2':
            show_tasks(todos)
        elif choice == '3':
            delete_task(todos)
        elif choice == '4':
            update_task(todos)
        elif choice == '0':
            sys.exit()
        else:
            print('bunday menu mavjud emas.')

main()
