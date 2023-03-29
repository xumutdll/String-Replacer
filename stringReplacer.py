import os
import re

# Define the regular expression pattern to search for
pattern = re.compile(r"String to be replaced here.")

# Counters for tracking replacements and files processed
replacements = 0
files_processed = 0
file_extension = ".dpr"

# Iterate over all files with the specific extension in the current directory and its subdirectories
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(file_extension):
            # Open the file and read its contents
            filename = os.path.join(root, file)
            with open(filename, "r") as f:
                contents = f.read()

            # Search for and replace the pattern in the contents
            new_contents, count = re.subn(
                pattern, r"New string here.", contents)

            # If replacements were made, write the modified contents back to the file
            if contents != new_contents:
                with open(filename, "w") as f:
                    f.write(new_contents)
                replacements += count

            # Increment the files processed counter
            files_processed += 1

# Print a message indicating the number of files processed and replacements made
if files_processed == 0:
    print("No files with the specific extension found.")
elif replacements == 0:
    print("No instances of the pattern found in any files with the specific extension.")
else:
    print(
        f"Processed {files_processed} files and made {replacements} replacements.")
    print("Done!")

input()
