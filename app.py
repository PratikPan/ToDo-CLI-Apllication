from commands import command_dict


def parse(command):
    """
    Tasks the command as input and returns the command name and arguments 
    """
    cmd_list = command.split()
    cmd_type = cmd_list[0]
    if(cmd_type == 'help' or cmd_type == 'quit'):
        return cmd_type, []
    # elif (cmd_type == 'list'):
    #     cmd_name = cmd_list[1]
    #     if (cmd_name in ['show', 'use', 'create']):
    #         return cmd_name, cmd_list[2:]
    #     else:
    #         return 'invalid', []
    elif (cmd_type == 'todo'):
        cmd_name = cmd_list[1]
        if(cmd_name in ['add', 'all', 'edit', 'remove', 'complete', 'incomplete']):
            return cmd_name, cmd_list[2:]
        else:
            return 'invalid', []
    else:
        return 'invalid', []


def main():
    print('Started the todo aplliction....')
    while(1):
        command = input('$ ')
        # command_type = command.split()[0]
        command_name, command_args = parse(command)
        if(command_name == 'quit'):
            break
        elif(command_name == "invalid"):
            print('Please enter a valid command')
        elif(command_name == 'help'):
            print(''' Command 
    1. todo all -> Show all the list
    2. todo add task_name -> Add the task in todo list
    3. todo edit -> Edit the selected task in todo list 
        - view all the list with index
        - then write the index you want edit the task
        - then write new task_name 
    4. todo remove -> Remove the selected task in todo list
        - view all the list with index
        - then write the index you want remove the task  
    5. todo complete -> Complete the selected task in todo list
        - view all the list with index
        - then write the index you want complete the task
    6. todo incomplete -> Incomplete the selected task in todo list
        - view all the list with index
        - then write the index you want incomplete the task
        ''')
        else:
            command_dict[command_name](command_args)


if __name__ == '__main__':
    main()
