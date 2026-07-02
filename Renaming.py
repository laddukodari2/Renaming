import os

folder = "."

files = os.listdir(folder)

count = 1

for file in files:
    if os.path.isfile(file):
        extension = os.path.splitext(file)[1]
        new_name = f"file_{count}{extension}"
        os.rename(file, new_name)
        print(file, "->", new_name)
        count += 1

print("Files renamed successfully!")
