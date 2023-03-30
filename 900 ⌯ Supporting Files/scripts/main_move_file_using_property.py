import os
from lib_md_file import *


directory1 = os.path.join("..", "..",  "000_Drafts", "Clipper")
directory2 = os.path.join("..", "..",  "000_Drafts")


directory_literature = os.path.join("..", "..", "500 ⌯ Knowledge Management","510 ⌯ 📚 Literature Notes")
directory_atomic = os.path.join("..", "..", "500 ⌯ Knowledge Management","530 ⌯ 📝 Atomic Notes")
directory_evergreen = os.path.join("..", "..", "500 ⌯ Knowledge Management","550 ⌯ 🌲 Evergreen Notes")
directory_topic = os.path.join("..", "..", "500 ⌯ Knowledge Management", "570 ⌯ 🧵 Topics")

directory_event = os.path.join("..", "..", "300 ⌯ Journal", "320_🎉Events")
directory_meeting = os.path.join("..", "..", "300 ⌯ Journal", "340 ⌯ 🔖 Meetings")
directory_person = os.path.join("..", "..", "300 ⌯ Journal",  "391 ⌯ 🕺 People")

directories = [directory1, directory2, directory_literature, directory_atomic, directory_evergreen, directory_topic, directory_meeting]
directories_draft = [directory1, directory2]

for directory in directories_draft:
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            full_filename = os.path.join(directory, filename)
            fileClass = get_fileClass(full_filename)
            # print(filename + " is " + fileClass)
            if fileClass == "literature-note":
                os.rename(full_filename, os.path.join(directory_literature, filename))
                print(filename + " moved.")
            elif fileClass == "atomic-note":
                os.rename(full_filename, os.path.join(directory_atomic, filename))
                print(filename + " moved.")
            elif fileClass == "evergreen-note":
                os.rename(full_filename, os.path.join(directory_evergreen, filename))
                print(filename + " moved.")
            elif fileClass == "topic":
                os.rename(full_filename, os.path.join(directory_topic, filename))
                print(filename + " moved.")
            elif fileClass == "meeting-minute":
                os.rename(full_filename, os.path.join(directory_meeting, filename))
                print(filename + " moved.")
            elif fileClass == "person":
                os.rename(full_filename, os.path.join(directory_person, filename))
                print(filename + " moved.")
