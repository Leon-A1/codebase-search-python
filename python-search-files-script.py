import os
import sys

# Add a simple check to determine if a file is likely to be a binary file
# based on its extension. This list can be expanded based on your needs.
binary_file_extensions = [
    '.png', '.ico', '.jpg', '.jpeg', '.gif', '.ttf', '.woff', '.eot', '.woff2',
    '.pdf', '.zip', '.tar', '.gz', '.rar', '.exe', '.dll', '.bin', '.mp3', '.mp4',
    '.avi', '.mov', '.flv', '.mkv', '.webm'
]

def is_binary(file_name):
    return any(file_name.endswith(ext) for ext in binary_file_extensions)

def search_files(keyword, directory='.'):
    for root, dirs, files in os.walk(directory):
        # Skip 'node_modules' and '.git' directories and any of their subdirectories
        dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'build']]
        
        for file in files:
            file_path = os.path.join(root, file)
            if is_binary(file):
                continue  # Skip binary files based on the extension check
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if keyword in f.read():
                        print(file_path)
            except Exception as e:
                # Handles errors for files that weren't caught by the extension check
                print(f"Error opening {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python python-search-files-script [keyword]")
    else:
        keyword = sys.argv[1]
        search_files(keyword)
