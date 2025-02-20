# Folder Generator (v3)

This **Python script** provides an intuitive graphical user interface (GUI) to create folder structures dynamically. Users can select a base directory and define a folder hierarchy using indentation. The script then generates the folders accordingly.

---

## Features

- ✅ **User-friendly GUI** built with Tkinter.
- ✅ **Directory selection** via a file browser.
- ✅ **Real-time text input** for defining folder structures.
- ✅ **Error handling** for invalid paths.
- ✅ Works across platforms (**Windows**, **macOS**, **Linux**).

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.6 or later**
- **Tkinter** (Included with standard Python installations)

---

## Installation

Clone or download the repository:

```bash
git clone https://github.com/your-username/folder-generator.git
cd folder-generator
```

Install dependencies (if needed):

```bash
pip install tk
```

---

## Usage Instructions

### Step 1: Run the Script

- Open a terminal or command prompt.
- Navigate to the script folder.
- Execute:

```bash
python folder_generator.py
```

---

### Step 2: Select the Base Directory

- Click the **"Browse"** button to select the base directory where the folders should be created.

---

### Step 3: Enter the Folder Structure

- Type your desired folder structure in the text box.
- Use **2 spaces** per indentation level to define subfolders.
- Example:

```
project-name
  src
  hello
    new
    one
```

---

### Step 4: Click "Create Folders"

- The script will generate the folder structure in the selected base directory.
- A confirmation message will appear upon successful creation.

---

## Example Output Structure

### Input:

```
project-name
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

### Output Folder Structure:

```
Base Directory/
  project-name/
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

## Troubleshooting

- **Folders not created properly:**
  - Ensure you are using **2 spaces** per indentation level.
  - Avoid mixed indentation (spaces vs tabs).

- **Script not running:**
  - Ensure Python is installed and added to your system PATH.

- **Incorrect base directory:**
  - Verify the selected path in the GUI.

---

## Contribution

Contributions are welcome! Fork the repository and submit a pull request with improvements or additional features.

---

## Author

Developed by Jal Bafana.

Happy coding! 🚀
