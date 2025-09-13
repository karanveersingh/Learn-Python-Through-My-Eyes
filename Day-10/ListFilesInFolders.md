# List Files in Folders with Python

You can use the `os` and `os.path` modules to list files in a folder. Here’s a simple example:

```python
import os

folder_path = 'path/to/your/folder'

# List all files and directories in the specified folder
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        print(item)
```

## List Files in All Subfolders

To list files recursively in all subfolders, use `os.walk`:

```python
import os

folder_path = 'path/to/your/folder'

for root, dirs, files in os.walk(folder_path):
    for file in files:
        print(os.path.join(root, file))
```

## Using `glob` for Pattern Matching

You can also use the `glob` module to list files matching a pattern:

```python
import glob

folder_path = 'path/to/your/folder'
for file in glob.glob(f"{folder_path}/*.txt"):
    print(file)
```