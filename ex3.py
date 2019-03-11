import sys

def main():
    tasks = {}

    while True:
        choice_index = int(showprompt())
        choice_index -= 1

        if choice_index == 0:
            print("\nInsert task details:")
            name = input("\tTask name: ")

            if len(name) == 0:
                print("Error: you must insert a name of your task.", file=sys.stderr)
                continue
            elif name in tasks:
                print("Error: a task with this name already exists.", file=sys.stderr)
                continue

            description = input("\tInsert a task description (optional): ")

            tasks[name] = description
            print("Done.")
        
        elif choice_index == 1:
            name = input("\nInsert task name to remove: ")
            
            if len(name) == 0:
                print("Error: you must insert a name of your task.", file=sys.stderr)
                continue
            elif not name in tasks:
                print("Error: a task with this name doesn't exist.", file=sys.stderr)
                continue

            tasks.pop(name)
            print("Done.")

        elif choice_index == 2:
            count = 1

            for key in tasks:
                print("\t[ TASK %d ]" % (count))
                print("\tName:", key)
                print("\tDescription:", tasks[key], end="\n\n")
                count += 1
        
        elif choice_index == 3:
            break

def showprompt():
    prompt_str = ["insert a new task",
                  "remove a task",
                  "show all the tasks",
                  "close the program"
                 ]
    
    print("\nInsert the number corresponding to the action you want to perform:\n")
    for i in range(0, len(prompt_str)):
        print("\t%d. %s" % (i + 1, prompt_str[i]), end="")
        
        if i < len(prompt_str) - 1:
            print(";", end="")
        else:
            print(".", end="")

        print("")

    while True:
        choice = input("\nYour choice: ")
        if len(choice) > 0:
            return choice


if __name__ == "__main__":
    main()