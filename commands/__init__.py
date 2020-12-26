import commands.todos as todos

command_dict = {
    'all': todos.show_items,
    'add': todos.add_item,
    'edit': todos.edit_item,
    'remove': todos.remove_item,
    'complete': todos.complete_item,
    'incomplete': todos.incomplete_item
}
