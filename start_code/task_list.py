tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# Print a list of uncompleted tasks

def uncompleted_tasks(lists, completion):
    false_completion_list = []
    true_completion_list = []
    for task_completion in lists:
        if task_completion ["completed"] == False:
            false_completion_list.append(task_completion)
        else:
            true_completion_list.append(task_completion)
    if completion == True:
        print(true_completion_list)
    else:
        print(false_completion_list)

uncompleted_tasks(tasks, True)

# Print a list of all task descriptions

def description_tasks(lists):
    description_list = []
    for descriptions in lists:
        description_list.append(descriptions["description"])
    print(description_list)

description_tasks(tasks)

# Print a list of tasks where time_taken is at least a given time

def taken_time(lists):
    start_time = 10.00
    total_minutes = 0
    hours = 0
    for time in lists:
        total_minutes += time["time_taken"]
        hours = total_minutes // 60
        # print(hours)
        actual_minutes = (total_minutes % 60) / 100
        # print(actual_minutes)
        print(str(start_time + hours + actual_minutes) + " " + time["description"] + " start time")

taken_time(tasks)

# Print any task with a given description

def print_task(list, description):
    requested_task = {}
    for descriptions in list:
        if descriptions["description"] == description:
            requested_task = descriptions
    print(requested_task)

print_task(tasks, "Make Dinner")




#  Given a description update that task to mark it as complete.

def update_task(list, description):
    task = {}
    for descriptions in list:
        if descriptions["description"] == description:
            status = input("Is the task complete? True or False")
            descriptions["completed"] = status
            task = descriptions
    print(task)

update_task(tasks, "Wash Dishes")



# Add a task to the list

