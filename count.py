import os

path = r'G:\Tuts\Archive\ITCS Challenge - Conways Game of Life\Abgaben\Win'
list_of_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        list_of_files.append(os.path.join(root, file))
chars = []
for name in list_of_files:
    file = open(name, "r")
    data = file.read()
    number_of_characters = len(data)
    user = name.split("\\")[-1][:-3]
    chars.append((number_of_characters, user))
chars.sort()
for number_of_characters, user in chars:
    print(f'Number of characters in {user}:', number_of_characters)

print(f"Total Participants: {len(chars)}")