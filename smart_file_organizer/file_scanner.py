import os

class FileNode:
    def __init__(self, name, is_file):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def build_file_tree(path):
    root = FileNode(os.path.basename(path), False)
    try:
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                child = build_file_tree(full_path)
                root.add_child(child)
            else:
                root.add_child(FileNode(entry, True))
    except PermissionError:
        pass  # Skip restricted folders
    return root

def print_file_tree(node, indent=0):
    print("  " * indent + ("📁 " if not node.is_file else "📄 ") + node.name)
    for child in node.children:
        print_file_tree(child, indent + 1)
