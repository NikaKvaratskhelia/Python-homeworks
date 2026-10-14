def create_user_profile(
    first_name: str,
    last_name: str,
    role: str = "student",
    is_active: bool = True,
):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active,
    }


user = create_user_profile("nika", "kvaratskhelia")
print(user)


# davaleba 2
def add_task(task_name: str, task_list=[]):
    task_list.append(task_name)
    print(task_list)


add_task("task 1")
add_task("task 2")
add_task("task 3")


# Shedegi
["task 1", "task 2", "task 3"]

# List is mutable element in python it only gets created once in the RAM and the value of the memory address is changed when calling append,
# it does not generate a new list that is the reason why it all three tasks are in one list.


def add_task_refactored(task_name: str, task_list=None):
    if task_list == None:
        task_list = []

    task_list.append(task_name)
    print(task_list)


add_task_refactored("task 1")
add_task_refactored("task 2")
add_task_refactored("task 3")

# davaleba 3

def analyze_text(text: str, min_length: int = 3, ignore_stopwords=None):
    if ignore_stopwords is None:
        ignore_stopwords = []

    divided_text = text.split(" ")
    count = 0

    for w in divided_text:
        if len(w) >= min_length and w not in ignore_stopwords:
            count += 1
            
    return count  

result = analyze_text('heelo world', ignore_stopwords=['world'])
print(result)  