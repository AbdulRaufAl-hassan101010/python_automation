import os

path = os.path.join(os.getcwd(), 'text.txt')

# write to file
# writeFile = open(path, 'a')
# writeFile.write("Hello world \n")
# writeFile.close()

with open(path, 'a') as file:
    file.write("Hello world there \n")


# read file
# readFile = open(path)
# content = readFile.read()
# # content = readFile.readlines()
# readFile.close()

with open(path) as file:
    content = file.read()


print(content)
