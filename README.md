# MIME Type File Renamer

Automatically rename files in a directory based on their MIME types. Perfect for organizing and labeling miscellaneous files with the correct extensions. Powered by the magic library.
Features

    Detects the MIME type of each file in the specified directory.
    Renames files to have the appropriate file extension based on their MIME type.
    Generates a log of processed files, detailing changes made and any encountered errors.

Prerequisites

Before you begin, ensure you have met the following requirements:

    Python 3.x
    magic library

You can install the required library using pip:

'''bash
pip install python-magic

Clone the repository:

'''bash
git clone https://github.com/Taskies/ExtensionFromMIME
cd ExtensionFromMIME

    Run the script:

'''bash
python mime_rename.py

    When prompted, enter the path to the directory you wish to scan and rename files.
    ex: 
    /media/where/your/folder/lives

Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. Don't forget to update tests as appropriate.
License

This project is MIT licensed.
