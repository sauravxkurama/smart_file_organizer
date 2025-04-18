import os
from file_scanner import build_file_tree, print_file_tree
from trie_search import Trie
from organizer import organize_files
from duplicate_detector import find_duplicates, remove_duplicates  # Import duplicate detection functions
from file_search import search_in_file  # Import the full-text search function

# Step 1: Build the file tree
root_path = "C:/smart_file_organizer"  # Change this to your desired path
tree = build_file_tree(root_path)

# Step 2: Print the folder structure (optional, for reference)
print("\n📂 Folder Structure:\n")
print_file_tree(tree)

# Step 3: Organize the files
print("\n📂 Organizing files...\n")
organize_files(root_path)  # Organize files in the scanned folder

# Step 4: Find and remove duplicate files
print("\n🔍 Finding duplicates...\n")
duplicates = find_duplicates(root_path)
if duplicates:
    print("\n🚨 Duplicate files detected:")
    remove_duplicates(duplicates)  # Remove or handle duplicates
else:
    print("\n✅ No duplicates found.")

# Step 5: Extract file names from the tree
filenames = []

# Define extract_filenames function
def extract_filenames(node, filenames):
    """Recursively extract filenames from the folder tree."""
    if node.is_file:
        filenames.append(node.name)
    for child in node.children:
        extract_filenames(child, filenames)

extract_filenames(tree, filenames)

# Step 6: Insert file names into Trie
trie = Trie()
for name in filenames:
    trie.insert(name)

# Step 7: Command-line search interface (for file names)
print("\n🔍 Search your files by name prefix (type 'exit' to quit):\n")

while True:
    prefix = input("Search: ")
    if prefix.lower() == "exit":
        print("Goodbye 👋")
        break
    matches = trie.search_prefix(prefix)
    if matches:
        print("Suggestions:")
        for m in matches:
            print(" -", m)
    else:
        print("No matches found.")

# Step 8: Full-text search for files (type 'exit' to quit)
def search_files_in_directory(path, search_term):
    """Search for a term in all files in a directory."""
    matches = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip Python script files
            if file.endswith('.py'):
                continue

            # Search in the file if it contains the search term
            if search_in_file(file_path, search_term):
                matches.append(file_path)

    return matches

print("\n🔍 Full-text search in files (type 'exit' to quit):\n")
while True:
    search_term = input("Search term: ")
    if search_term.lower() == "exit":
        print("Goodbye 👋")
        break
    
    results = search_files_in_directory(root_path, search_term)
    if results:
        print("\n📄 Search Results:")
        for result in results:
            print(result)
    else:
        print("No matching files found.")
