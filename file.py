import data
import text as t
import table
import bakup
import json
from json.decoder import JSONDecodeError

def choose_option():
    while True:
        t.t_print("s. Export current table")
        t.t_print("l. Load table from file")
        t.t_print("z. Go back")
        choice = t.t_input("Choose option: ")
        match choice:
            case 's':
                export_current_table()
            case 'l':
                load_table_from_file()
            case 'z':
                return
        

def export_current_table():
    delete_backup = False
    if bakup.backup_state():
        delete_backup = True

    with open('table.json', 'w') as file:
        json.dump(bakup.undo_stack[-1], file)

    if delete_backup:
        bakup.undo_stack.pop()
    t.t_print(f"{data.GREEN}Exported current table successfully!{data.END}")


def load_table_from_file():
    try:
        with open('table.json', 'r') as file:
            state = json.load(file)

        bakup.restore_state(state)
        data.characters = {int(char_num): char_name for char_num, char_name in data.characters.items()} # json doesn't support int key so convert it
        table.print_table()
        t.t_print(f"{data.GREEN}Loaded table successfully!{data.END}")
        
    except FileNotFoundError:
        t.t_print(f"{data.RED}Error: 'table.json' file not found.{data.END}")
    except JSONDecodeError:
        t.t_print(f"{data.RED}Error: Failed to parse 'table.json'. Ensure it contains valid JSON.{data.END}")
    except KeyError as e:
        t.t_print(f"{data.RED}Error: Missing key in the loaded table: {e}{data.END}")
    except AttributeError as e:
        t.t_print(f"{data.RED}Error: Invalid structure in the loaded table: {e}{data.END}")
    except Exception as e:
        t.t_print(f"{data.RED}An unexpected error occurred: {e}{data.END}")