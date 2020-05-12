import re

def add_student(first_name):
    with open("students.txt", "a", encoding='utf-8') as file:
        file.write(first_name + '\n')


def find_student(first_name):
    with open("students.txt", "r", encoding='utf-8') as file:
        for l in file:
            if l.rstrip() == first_name:
                print("{} was found!". format(first_name))


def update_student(first_name, new_name):
    with open("students.txt", "r+", encoding='utf-8') as file:
        text = file.read()
        text = re.sub(first_name, new_name, text)
        file.seek(0)
        file.write(text)
        file.truncate()


def remove_student(first_name):
    with open("students.txt", "r+", encoding='utf-8') as file:
        text = file.read()
        text = re.sub(first_name, '', text)
        file.seek(0)
        file.write(text)
        file.truncate()
