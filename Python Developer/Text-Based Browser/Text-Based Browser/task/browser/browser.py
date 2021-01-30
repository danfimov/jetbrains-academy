import argparse
import os

import requests

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


# VALIDATED_URLS = ['nytimes.com', 'bloomberg.com']


def valid_url(check_url: str):
    if "." in check_url:
        return True
    else:
        return False


def save_content(file_content: str, file_directory: str, file_name: str):
    path = os.path.join(file_directory, file_name)
    with open(path, 'w') as file:
        file.write(file_content)


parser = argparse.ArgumentParser('This is a simple web-browser')
parser.add_argument('dir', default='')

directory = parser.parse_args().dir
if not os.access(directory, os.F_OK):
    os.mkdir(directory)

previous_page = ''
stack_pages = []
while (user_input := input()) != 'exit':
    if user_input == 'back':
        if stack_pages:
            print(stack_pages.pop())
    elif valid_url(user_input):
        if user_input[:8] != 'https://':
            user_input = 'https://' + user_input
        r = requests.get(user_input)
        content = r.text
        print(content)

        if previous_page:
            stack_pages.append(previous_page)
        previous_page = content

        user_input = user_input[8:]
        name = user_input.rpartition(".")[0]
        save_content(content, directory, name)

    else:
        print("Error: Incorrect command or URL")
