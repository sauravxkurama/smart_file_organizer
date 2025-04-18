import os
import hashlib
import shutil

def get_file_hash(file_path):
    """Generate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        # Read file in chunks to avoid memory overload for large files
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicates(path):
    """Find duplicate files based on MD5 hash."""
    hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip Python script files
            if file.endswith('.py'):
                continue

            # Calculate hash for the current file
            file_hash = get_file_hash(file_path)

            # Check if hash is already in the dictionary
            if file_hash in hashes:
                # Duplicate found
                duplicates.append((file_path, hashes[file_hash]))
            else:
                hashes[file_hash] = file_path

    return duplicates

def remove_duplicates(duplicates):
    """Remove or handle duplicate files."""
    for duplicate, original in duplicates:
        print(f"Duplicate found: {duplicate} is a duplicate of {original}")
        # You can choose to delete the duplicate file
        os.remove(duplicate)
        print(f"Deleted: {duplicate}")
