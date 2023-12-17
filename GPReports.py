import re
import time
from termcolor import colored

log_file_path = '/var/log/nginx/access.log'

def colorize_post_line(line):
    if re.search(r'POST', line):
        return colored(line, 'green')
    else:
        return line

def display_updated_log(file_path, interval=0.1):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            while True:
                current_position = file.tell()
                file.seek(current_position)
                new_lines = file.readlines()

                if new_lines:
                    lines += new_lines
                    for line in new_lines:
                        colored_line = colorize_post_line(line)
                        print(colored_line, end='')
                else:
                    time.sleep(interval)

    except FileNotFoundError:
        print()

if __name__ == "__main__":
    display_updated_log(log_file_path)
