import json
from datetime import datetime


def get_data(list_file_name):
    data = []
    with open(list_file_name, 'r') as todo_list:
        data = json.load(todo_list)
    return data


def add_item(args):
    # list_name = set_list(args[0])
    title = args[0]
    data = get_data('list.json')
    # title = args[0]

    # print(data)
    # print(title)

    data.append({
        'title': title,
        'created_at': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'completed': False
    })

    # print(data)

    with open('list.json', 'w') as todo_list:
        json.dump(data, todo_list, sort_keys=True, indent=True)


def show_items(args):
    data = get_data('list.json')
    if(len(data) == 0):
        print('No todo item in this list!')
        return
    completed = 0
    for index, todo_item in enumerate(data):
        print(index, todo_item['title'])
        if(todo_item['completed'] == True):
            completed += 1
    print(f'{completed}/{len(data)} tasks completed!')


def edit_item(args):
    show_items(args)
    new_data = []
    data = get_data('list.json')
    data_length = len(data) - 1
    print("Which index number would you like to edit task ?")
    edit_option = input(f"Select a number 0-{data_length} : ")

    for index, todo_item in enumerate(data):
        if(index == int(edit_option)):
            title = todo_item['title']
            created_at = todo_item['created_at']
            completed = todo_item['completed']
            print(f"Current Title : {title}")
            title = input("What would you like the new title to be ? : ")
            created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            new_data.append({
                'title': title,
                'created_at': created_at,
                'completed': completed
            })
            index += 1
        else:
            new_data.append(todo_item)
            index += 1
    # if(index != int(edit_option)):

    with open('list.json', 'w') as todo_list:
        json.dump(new_data, todo_list, sort_keys=True, indent=True)

    # print(edit_option)

    # item_id = args[0]
    # new_title = args[1]

    # data.append({
    #     'title': new_title,
    #     'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    #     'completed': False
    # })

    # for todo_item in data:
    # print(todo_item['title'])
    # if (item_id == todo_item['title']):
    # print(todo_item)
    # del todo_item['title']
    # del todo_item['created_at']
    # del todo_item['completed']
    # with open('list.json', 'w') as todo_list:
    #     json.dump(data, todo_list, sort_keys=True, indent=True)

    # print(item_id)
    # print(new_title)

    # updated_todo = {
    #     'title': new_title,
    #     'created_at': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    #     'completed': False
    # }


def remove_item(args):
    show_items(args)
    new_data = []
    data = get_data('list.json')
    data_length = len(data) - 1
    print("Which index number would you like to remove task ?")
    remove_option = input(f"Select a number 0-{data_length} : ")

    for index, todo_item in enumerate(data):
        if(index == int(remove_option)):
            pass
            index += 1
        else:
            new_data.append(todo_item)
            index += 1
    with open('list.json', 'w') as todo_list:
        json.dump(new_data, todo_list, sort_keys=True, indent=True)


def complete_item(args):
    show_items(args)
    new_data = []
    data = get_data('list.json')
    data_length = len(data) - 1
    print("Which index number would you like to complete task ?")
    complete_option = input(f"Select a number 0-{data_length} : ")

    for index, todo_item in enumerate(data):
        if(index == int(complete_option)):
            title = todo_item['title']
            created_at = todo_item['created_at']
            completed = todo_item['completed']
            completed = True
            new_data.append({
                'title': title,
                'created_at': created_at,
                'completed': completed
            })
            index += 1
        else:
            new_data.append(todo_item)
            index += 1

    with open('list.json', 'w') as todo_list:
        json.dump(new_data, todo_list, sort_keys=True, indent=True)


def incomplete_item(args):
    show_items(args)
    new_data = []
    data = get_data('list.json')
    data_length = len(data) - 1
    print("Which index number would you like to incomplete task ?")
    complete_option = input(f"Select a number 0-{data_length} : ")

    for index, todo_item in enumerate(data):
        if(index == int(complete_option)):
            title = todo_item['title']
            created_at = todo_item['created_at']
            completed = todo_item['completed']
            completed = False
            new_data.append({
                'title': title,
                'created_at': created_at,
                'completed': completed
            })
            index += 1
        else:
            new_data.append(todo_item)
            index += 1
    with open('list.json', 'w') as todo_list:
        json.dump(new_data, todo_list, sort_keys=True, indent=True)
