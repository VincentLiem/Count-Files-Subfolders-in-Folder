import os

path = input("Enter path >> ")
total_files = 0
total_dir = 0
for base, dirs, files in os.walk(path):
    dirs =  sorted(dirs)
    file_count = 0
    for directories in dirs:
        total_dir += 1
    for Files in files:
        total_files += 1
        file_count += 1
    print(base, " : ", file_count, " files")
print("Total files: ", total_files)
print("Total directories: ", total_dir)
