MIME Type File Renamer

Automatically rename files in a directory based on their MIME types. Perfect for organizing and labeling miscellaneous files with the correct extensions. Powered by the magic library.

Features

- Detects the MIME type of each file in the specified directory.
- Renames files to have the appropriate file extension based on their MIME type.
- Generates a log of processed files, detailing changes made and any encountered errors.

Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.x
    magic library

You can install the required library using pip:

```bash
pip install magic-python
```

Clone the repository:

```bash
git clone https://github.com/Taskies/ExtensionFromMIME
cd ExtensionFromMIME
```
Run the script:

```bash
python mime_rename.py
```
When prompted, enter the path to the directory you wish to scan and rename files.
Example:

```bash
/media/where/your/folder/lives
```

Compilation and Execution Instructions for C++ Script
For Debian-Based Linux
Prerequisites:

- C++ Compiler (g++): Install with sudo apt-get install g++ if not already installed.
- Compiling and Running the C++ Program:

1. Open a terminal.
2. Navigate to the directory containing the C++ file (prime_finder_multithreaded.cpp).
3. Compile the program:

```bash
g++ -o prime prime.cpp -lpthread
```

4. Run the program:

```bash
./prime
```

For Windows
Prerequisites:

- C++ Compiler: Install a C++ compiler like MinGW or Microsoft Visual C++. Ensure it's added to the system's PATH. 

Compiling and Running the C++ Program:

1. Open Command Prompt or PowerShell.
2. Navigate to the directory containing the C++ file (prime.cpp).
3. Compile the program (using MinGW as an example):

- For Command Prompt (CMD):

```cmd
g++ -o prime.exe prime.cpp -lpthread
prime.exe
```

- For Powershell:

```powershell
g++ -o prime.exe prime.cpp -lpthread
.\prime.exe
```

Note:

- These instructions assume standard installations of the necessary tools. Users might need to adjust commands based on their specific setup.
- For Windows, using a development environment like Cygwin or Windows Subsystem for Linux (WSL) can provide a more Unix-like experience.


Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. Don't forget to update tests as appropriate.
License

This project is MIT licensed.

