import os
import sys

file_path = "/aloy/home/acomajuncosa/Jupyter/Random/Look4Errors.ipynb"

# Open file with O_NOATIME flag
fd = os.open(file_path, os.O_RDONLY | os.O_NOATIME)
with os.fdopen(fd, 'r') as f:
    contents = f.read()

print(contents)
