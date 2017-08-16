import os  # the os module provides misc OS functionality
import sys  # the sys module provides system-specific functions
import shutil  # shutil provides functions for copying files around the directory tree


def main():
    # get the folder we want to read files from
    # sys.argv is the list of command line arguments
    print("Arguments:", sys.argv)
    folder_path = sys.argv[1]
    word = sys.argv[2]
    # there are standard library modules that help with argument parsing
    # e.g. argparse, but for  simple script like this we don't need to use it

    for dirpath, dirnames, filenames in os.walk(folder_path):
        # os.walk allows us to 'walk' a filesystem tree and for each folder (each loop)
        # we are given the path to the directory, the names of subdirectories in that directory
        # and the names of files in that directory

        for filename in filenames:
            # looping through the list of filenames, we open each file in turn
            # and read the contents
            filepath = os.path.join(dirpath, filename)
            f = open(filepath)
            text = f.read()
            f.close()

            # and then check if the value of variable 'word' is in the file contents
            if word in text:
                print(filepath, "DOES contain", word)

                # if the file did contain a match, lets copy it to the 'contains_{word}' folder
                # first, we make the name for the folder and create it if it doesn't already exist
                output_folder_name = "contains_%s" % word
                # this %s syntax is one of the ways to format a string in python
                os.makedirs(output_folder_name, exist_ok=True)
                # and then we copy the file to the directory we just made sure existed
                file_destination = os.path.join(output_folder_name, filename)
                # note that filename and not filepath are used here - so we aren't copying the
                # folder structure, just the files themselves
                shutil.copyfile(filepath, file_destination)

            else:
                print(filepath, "does not contain", word)

    print("Done!")


# You'll often see this __name__ in python programs
# Because when they are imported python code begins executing it's often a
# good idea to check that the program was run on the command line BEFORE
# you do any actual logic
# if this file was the one run on the command line the special builtin
# '__name__' will have the value "__main__"

if __name__ == "__main__":
    main()
