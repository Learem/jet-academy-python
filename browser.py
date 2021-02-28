import os

import sys

import requests

import bs4

from bs4 import BeautifulSoup, SoupStrainer

from colorama import init, Fore


py_args = sys.argv
history_log = []
last_site = True
cur_dir = os.getcwd()
links = []
tags = ["p", "a", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"]


def tag_print(tag):
    if tag.string:
        result_str = ""
        if tag.name == "a":
            result_str = result_str + Fore.BLUE + tag.string + Fore.RESET
        elif tag.name in tags:
            result_str = result_str + tag.string
        return result_str
    else:
        result_str = ""
        for item in tag.children:
            result_str = result_str + tag_print(item)
        return result_str


def text_print(node):
    for item in node.children:
        if isinstance(item, bs4.element.Tag):
            if item.name in tags:
                print(tag_print(item))
            else:
                text_print(item)


if len(py_args) > 1:
    cur_dir = py_args[1]
    if not os.access(cur_dir, os.F_OK):
        os.mkdir(cur_dir)
#    os.chdir(py_args[1])
#    print(os.getcwd())

while True:
    input_string = input()
    if input_string == "exit":
        break
    if input_string == "back":
        if last_site:
            history_log.pop()
            last_site = False
        if len(history_log) > 0:
            input_string = history_log.pop()
        else:
            continue
    if "." in input_string:
        if not input_string.startswith("https://"):
            input_string = "https://" + input_string
        url = input_string
        url_file = url.replace(".", "_").replace("https://", "")
        r = requests.get(url)
        if r:
            only_req_tags = SoupStrainer(tags)
            only_a_tags = SoupStrainer("a")
            soup = BeautifulSoup(r.content, "html.parser", parse_only=only_req_tags)
            soup_a = BeautifulSoup(r.content, "html.parser", parse_only=only_a_tags)
            init(autoreset=True)
            result_strings = []
            links = list(soup_a.stripped_strings)
            num_link = 0
            with open(cur_dir + "\\" + url_file, "w", encoding='utf-8') as file_cash:
                for string in soup.stripped_strings:
                    file_cash.write(string + "\n")
                    if num_link < len(links) and string == links[num_link]:
                        string = Fore.BLUE + string + Fore.RESET
                        num_link += 1
                    result_strings.append(string)
            for string in result_strings:
                print(string)

#            with open(cur_dir + "\\" + url_file, "w", encoding='utf-8') as file_cash:
#            for obj in soup.children:
#                if isinstance(obj, bs4.element.Tag):
#            text_print(soup.find("body"))
#                if obj.name in ["a", "p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"]:
#                    if obj.string:
#                        file_cash.write(obj.text + "\n")
#                    elif obj.name == "a":
#                        print(Fore.BLUE + obj.text)
#                        file_cash.write(obj.text + "\n")
#            print(soup.get_text())
            history_log.append(url_file)
            last_site = True
        else:
            print("Error: Incorrect URL")
        continue
    elif "." not in input_string:
        if os.access(cur_dir + "\\" + input_string, os.R_OK):
            with open(cur_dir + "\\" + input_string, "r") as file_cash:
                print(file_cash.read())
        else:
            print("Error: Incorrect URL")
        continue
