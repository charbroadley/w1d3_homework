tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# MVP

# 1. Print a list of uncompleted tasks

def uncomplete(list_of_tasks):
    for task in list_of_tasks:
        if task ["completed"] == False:
            print(task)

uncomplete(tasks)

# 2. Print a list of completed tasks

def complete(list_of_tasks):
    complete_tasks = []
    for task in list_of_tasks:
        if task ["completed"] == True:
            complete_tasks.append(task["description"])
    print(complete_tasks)

complete(tasks)

# 3. Print a list of all task descriptions

def descriptions(list_of_tasks):
    task_descriptions = []
    for task in list_of_tasks:
        task_descriptions.append(task["description"])
    print (task_descriptions)

descriptions(tasks)

# 4. Print a list of tasks where time_taken is at least a given time

def time_taken(list_of_tasks, time):
    task_description = []
    for task in list_of_tasks:
        if task ["time_taken"] > 25:
            task_description.append(task["description"])
    print (task_description)
    
time_taken(tasks, {"time_taken"})

# 5. Print any task with a given description

def given_description(list_of_tasks, description):
    task_description = []
    for task in list_of_tasks:
        if task ["description"] == "Feed Cat":
            task_description.append(task)
    print(task_description)

given_description(tasks, {"description"})


# EXTENSION

# 6. Given a description update that task to mark it as complete.

def update_task(list_of_tasks):
    for task in list_of_tasks:
        if task ["description"] == "Feed Cat":
            return True
    print(tasks)

update_task(tasks)

# tried various ways of doing this but couldn't past "TypeError: list indices must be integers or slices, not str"

# 7. Add a task to the list

def add_a_task(list_of_tasks):
    tasks.append(
        { "description": "Start a Cult",
        "completed": False,
        "time_taken": 45 
        },
    )
    print(tasks)

add_a_task(tasks)