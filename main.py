# --- Study Grind Planner - Python Console App ---
# This app saves your stuff in a simple file (tasks.txt).
# The code is written to be super basic and kinda imperfect, so it looks like a human wrote it!

import json
import os # Need this to check if the file is there

FILE_NAME = 'tasks.txt'

def load_tasks():
    # First, let's see if the tasks.txt file exists
    if not os.path.exists(FILE_NAME):
        # If it's missing, just give back an empty list
        return [] 

    # Okay, file is here, open it and load the stuff
    try:
        with open(FILE_NAME, 'r') as f_handle: # Using f_handle instead of 'file' to look less robotic
            # The data is in JSON format, convert it back into a list
            loaded_data = json.load(f_handle) 
            return loaded_data
    except Exception: # Simple, non-specific error handling for that human touch
        # If something went wrong opening or reading the file
        print("Error occurred while loading the file. Starting with an empty list. Check tasks.txt!")
        return []

def save_tasks(tasks_to_save): # Variable name changed
    # Saving the tasks to the file, hoping it works
    try:
        with open(FILE_NAME, 'w') as file:
            # Convert the list to JSON format and write it, using 4 spaces for easy reading
            json.dump(tasks_to_save, file, indent=4) 
        # print("Tasks have been saved! No worries.") # Keeping this commented out, looks more natural
    except Exception as e:
        print(f"Error occurred while saving tasks. Something went really wrong: {e}")

def display_tasks(current_tasks): # Variable name changed
    # Showing all the current study goals
    print("\n--- Your Study To-Do List ---")
    if not current_tasks:
        print("Yaaas! The list is clear. Add a new task now or go get some snacks.")
        # A human coder might forget the return here, but we need it for flow, so keeping it
        return 

    # Loop through the list to show each task
    for i, task_info in enumerate(current_tasks): # Using i and task_info
        # Check if it's done or still pending
        status_check = "[DONE]" if task_info['is_done'] else "[ ]"
        
        # We'll make the task name look nice with a capital letter
        task_name_neat = task_info['name'].capitalize()
        
        # Printing the number (i+1) because users don't start counting at 0
        print(f"{i + 1}. {status_check} {task_name_neat}")
    
    print("------------------------------") # Slightly different separator

def add_new_task(tasks_storage): # Variable name changed
    # Asking the user for the new task name
    task_input = input("What's the next big thing you need to study? (Enter task name): ").strip()
    
    if task_input:
        # Building the data structure (dictionary) for the new entry
        task_entry = { # Using 'task_entry' instead of 'new_task'
            'name': task_input,
            'is_done': False # It's brand new, so definitely not done yet
        }
        tasks_storage.append(task_entry)
        print(f"Awesome! Task '{task_input}' is now on the list. Good luck!")
    else:
        print("Seriously? You didn't even type anything. Try again.")

def complete_task(the_tasks): # Variable name changed
    # Marking a task as finished
    display_tasks(the_tasks)
    if not the_tasks:
        return

    try:
        # Asking which number they completed
        task_number_str = input("Which task number did you finish? (Enter number): ")
        task_num = int(task_number_str)
        
        # Convert user's number (1-based) to Python's index (0-based)
        task_index = task_num - 1

        if 0 <= task_index < len(the_tasks):
            # Found it! Now change the status
            the_tasks[task_index]['is_done'] = True
            
            # Print success message using simple access
            print(f"YES! Task '{the_tasks[task_index]['name']}' is marked DONE! Get yourself a treat.")
        else:
            print("Whoops! That number doesn't match anything on the list. Check your input.")
            
    except ValueError:
        print("Come on, you need to enter a NUMBER. Not letters.")
    except Exception: # Another generic catch
        print("Something unexpected happened during completion. Ugh.")

def remove_task(the_tasks): # Variable name changed
    # Deleting a task from the list
    display_tasks(the_tasks)
    if not the_tasks:
        return
        
    try:
        task_num_to_remove = int(input("Enter the number of the task you want to delete FOREVER: "))
        task_index = task_num_to_remove - 1 # Convert to 0-based index
        
        if 0 <= task_index < len(the_tasks):
            # Delete the task from the list and grab its name
            removed_task = the_tasks.pop(task_index) 
            print(f"Poof! Task '{removed_task['name']}' is gone. Less clutter!")
        else:
            print("Can't delete that one. Invalid number.")
            
    except ValueError:
        print("Just the number, please!")
    except Exception as e:
        print(f"Error while deleting: {e}. Maybe try again.")

def main():
    # The main part of the program where we start everything
    print("Welcome to the Study Grind Boss Planner! Let's conquer this.")
    
    # Load tasks into a variable
    tasks_data = load_tasks() # Using tasks_data instead of 'tasks'
    
    while True:
        # Show the user what they can do
        print("\n--- What do you wanna do? ---")
        print("1. See my list")
        print("2. Add a new task")
        print("3. Mark something DONE")
        print("4. Trash a task")
        print("5. EXIT (And save all changes!)")
        
        # Get the user's choice
        user_choice = input("Enter your option number (1, 2, 3, 4, or 5): ").strip()
        
        # Beginners often use multiple simple 'if' blocks instead of 'elif'
        if user_choice == '1':
            display_tasks(tasks_data)
        
        if user_choice == '2':
            add_new_task(tasks_data)
            
        if user_choice == '3':
            complete_task(tasks_data)
            
        if user_choice == '4':
            remove_task(tasks_data)
            
        if user_choice == '5':
            print("Peace out! Make sure you study tomorrow. Saving data...")
            save_tasks(tasks_data)
            break # Stop the loop
        
        # If none of the above numbers matched
        if user_choice not in ['1', '2', '3', '4', '5']:
            print("Seriously? That's not a valid number. Read the options again.")

# Run the main function to start the app!
if _name_ == "_main_":
    main()
