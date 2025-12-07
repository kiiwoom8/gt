import data
import text
import table
import bakup

def print_options():
    for key, value in data.opts.items():
        if 'Exit' in value["title"]:
            text.t_print(f"{data.GRAY}*{data.END}. Refresh [{data.YELLOW}ENTER{data.END}]")
            text.t_print(f"{data.GRAY}*{data.END}. Undo/Redo [{data.YELLOW}q{data.END}/{data.YELLOW}w{data.END}]")
            text.t_print(f"{data.GRAY}*{data.END}. Adjust font size [{data.YELLOW}ctrl{data.END} + '{data.YELLOW}+{data.END}' or '{data.YELLOW}-{data.END}']")

        text.t_print(f"{key}. {value["title"]}")


def get_option():
    option = text.t_input(f"Enter your choice: ")
    if option and not (option.isdigit() and (option := int(option)) in data.opts.keys() or option in ['q', 'w', 'z']):
        text.error_text = "\033[31mInvalid choice. Please select a valid option.\033[0m"

    return option


def execute_function(option):
    if option in data.opts.keys():
        data.opts[option]["function"]()
    elif option in ['q', 'w']:
        match option:
            case 'q': 
                bakup.undo()
            case 'w': 
                bakup.redo()


def main():
    data.reset()
    while True:
        table.print_table()
        text.check_error()
        print_options()
        option = get_option()
        execute_function(option)


if __name__ == "__main__":
    main()
