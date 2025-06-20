"""
The shutil module in Python provides high-level file operations,
such as copying, moving, and removing files and directories.
It is part of the standard library and is commonly used for tasks
like copying files, creating archives, and managing directory trees
"""

import shutil

shutil.make_archive("output",'zip','../files')