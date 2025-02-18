import os
import shutil

# Define categories for file extensions
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.csv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.tar', '.rar', '.gz'],
    'Code': ['.py', '.html', '.css', '.js'],
    'Others': []  # Files that don't fit into any category
}

# Function to organize files
def organize_files(directory):
    # Change to the specified directory
    os.chdir(directory)

    # Iterate through the files in the directory
    for filename in os.listdir(directory):
        # Check if it's a file (not a directory)
        if os.path.isfile(filename):
            # Get file extension
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Find the category for the file
            moved = False
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    # Create the category folder if it doesn't exist
                    if not os.path.exists(category):
                        os.makedirs(category)
                    
                    # Move the file into the appropriate folder
                    shutil.move(filename, os.path.join(category, filename))
                    print(f"Moved: {filename} -> {category}/")
                    moved = True
                    break
            
            # If no category is found, move it to 'Others'
            if not moved:
                if not os.path.exists('Others'):
                    os.makedirs('Others')
                shutil.move(filename, os.path.join('Others', filename))
                print(f"Moved: {filename} -> Others/")

# Main program
if __name__ == "__main__":
    # Specify the directory you want to organize (replace with your path)
    directory = input("Enter the path to the directory you want to organize: ")
    
    if os.path.isdir(directory):
        organize_files(directory)
    else:
        print("Invalid directory path. Please try again.")
