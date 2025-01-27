import os

def create_folders_from_structure(structure, base_dir="."):
    lines = structure.strip().split("\n")
    stack = []  # Tracks the folder hierarchy

    for line in lines:
        # Calculate the depth based on leading spaces (2 spaces per level)
        stripped_line = line.lstrip()
        depth = (len(line) - len(stripped_line)) // 2  # Assume 2 spaces per level
        folder_name = stripped_line

        # Debugging: Print details of the line being processed
        print(f"Processing: '{folder_name}' at depth {depth}")

        # Adjust the stack to match the current depth
        while len(stack) > depth:
            stack.pop()

        # Build the full path for the current folder
        current_path = os.path.join(base_dir, *stack, folder_name)

        # Debugging: Print the path being created
        print(f"Creating folder: {current_path}")

        # Create the folder
        os.makedirs(current_path, exist_ok=True)

        # Add the folder to the stack
        stack.append(folder_name)

if __name__ == "__main__":
    # Prompt the user to specify the base directory
    base_directory = input("Enter the base path where folders should be created: ").strip()

    # Validate the path
    if not os.path.exists(base_directory):
        print(f"The path '{base_directory}' does not exist. Please provide a valid path.")
    else:
        print("Enter the folder structure (indent with 2 spaces per hierarchy level):")
        folder_structure = ""

        # Capture the folder structure input
        while True:
            try:
                line = input()
                if line.strip() == "":
                    break
                folder_structure += line + "\n"  # Add a newline after each input
            except EOFError:
                break

        # Create the folder structure
        create_folders_from_structure(folder_structure, base_dir=base_directory)
        print(f"Folders created successfully in {os.path.abspath(base_directory)}")
