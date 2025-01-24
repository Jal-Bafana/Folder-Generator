# Folder Generator

This **Python script** allows you to create a folder structure dynamically based on an input hierarchy provided by the user. The structure is created recursively with proper folder depth and hierarchy, making it ideal for setting up project directories efficiently.

---

## Features

- ✅ Dynamically generates folder structures based on user input.
- ✅ Supports hierarchical indentation to define subfolder depth.
- ✅ Handles incorrect folder depth issues with clear debugging messages.
- ✅ Works across platforms (**Windows**, **macOS**, **Linux**).

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.6 or later**

---

## Usage Instructions

### **Step 1: Clone or Download the Repository**

```bash
git clone https://github.com/your-username/folder-generator.git
cd folder-generator
```
---
### Step 2: Run the Script
- Open a terminal or command prompt.
- Navigate to the folder containing the script (e.g., folder_generator.py).
- Execute the script by running:
```bash
python folder_generator.py
```
---
### Step 3: Input the Folder Structure
When prompted, enter your desired folder structure. Use 2 spaces for each level of indentation to define subfolders. For example:
```bash
project-name2
  src
  hello
    new
    one
```
Press Enter on a blank line to finish the input.

---
### Step 4: View the Created Folder Structure
The script will create the folder structure on your Desktop inside a folder named project-name2.
Example
Input:
```bash
project-name2
  docs
  src
    assets
    components
    pages
    utils
  tests
  config
  build
```
Output Folder Structure:
```bash
Desktop/
  project-name2/
    docs/
    src/
      assets/
      components/
      pages/
      utils/
    tests/
    config/
    build/
```
---
## Debugging
The script provides real-time debugging messages to ensure the folder structure is created correctly. Example messages:
```bash
Processing: 'project-name2' at depth 0
Creating folder: C:\Users\YourName\Desktop\project-name2
Processing: 'src' at depth 1
Creating folder: C:\Users\YourName\Desktop\project-name2\src
Processing: 'hello' at depth 1
Creating folder: C:\Users\YourName\Desktop\project-name2\hello
Processing: 'new' at depth 2
Creating folder: C:\Users\YourName\Desktop\project-name2\hello\new
Processing: 'one' at depth 2
Creating folder: C:\Users\YourName\Desktop\project-name2\hello\one
```
---
## Troubleshooting
-Folder structure not created properly:
  -Ensure you are using 2 spaces per indentation level.
  -Check for mixed indentation (e.g., spaces vs tabs).

-Empty output folder:
  -Ensure you pressed Enter on a blank line to finish the input.
  -Script not running:

-Ensure Python is installed and added to your system PATH.

---
## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or additional features.

---
### Make your changes
### Submit a pull request
---
## Author
Developed by Jal Bafana.

Happy coding! 🚀
