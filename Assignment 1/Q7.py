#7.1
with open("example.txt", "w") as file:
    file.write("Hello World")
with open("example.txt", "r") as file:
    content = file.read()
print("File content",content)

#7.2
with open("example.txt", "a") as file:
    file.write("Appended text to file")
with open("example.txt", "r") as file:
    content = file.read()
print("Updated content ", content)

#7.3
with open("example.txt", "r") as file:
    lines = file.readlines()
print("No. of lines", len(lines))




