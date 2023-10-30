import os
import magic
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

# Define a dictionary to map MIME types to file extensions
mime_to_extension = {
    'image/jpeg': '.jpg',
    'image/png': '.png',
    'text/plain': '.txt',
    'application/pdf': '.pdf',
    'video/x-flv': '.flv',
    'video/mp4': '.mp4',
    'video/quicktime': '.mov',
    'video/x-msvideo': '.avi',
    'video/x-ms-wmv': '.wmv',
    'video/webm': '.webm',
    'video/ogg': '.ogv',
    'video/3gpp': '.3gp',
    'video/3gpp2': '.3g2',
    'video/mpeg': '.mpeg',
    'video/x-matroska': '.mkv',
    'video/h264': '.h264',
    'video/h265': '.h265',
    # Additional MIME types can be added as needed
}

# Function to get the MIME type of a file
def get_mime_type(file_path):
    return magic.from_file(file_path, mime=True)

def process_directory(directory):
    output_file = "xresults.txt"
    counter = 0
    while os.path.exists(output_file):
        counter += 1
        output_file = f"xresults{counter}.txt"
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                mime_type = get_mime_type(file_path)

                f.write(f"Processing: {file_path} - Detected MIME type: {mime_type}\n")

                found_extension = mime_to_extension.get(mime_type)

                if found_extension:
                    new_extension = found_extension
                    if not file_path.endswith(new_extension):
                        new_file_path = file_path + new_extension
                        try:
                            os.rename(file_path, new_file_path)
                            f.write(f"Renamed {file_path} to {new_file_path}\n")
                        except Exception as e:
                            f.write(f"Failed to rename {file_path} due to error: {e}\n")
                    else:
                        f.write(f"{file_path} already has the correct extension.\n")
                else:
                    f.write(f"Unknown MIME type: {mime_type}. No changes made to {file_path}.\n")

def run_command_line_version():
    user_input = input("Enter the path to the folder you want to scan: ")
    root_folder = user_input.strip()  # Remove any leading/trailing white spaces
    if os.path.exists(root_folder) and os.path.isdir(root_folder):
        print(f"Writing results to xresults.txt")
        process_directory(root_folder)
    else:
        print(f"The path '{root_folder}' does not exist or is not a directory.")
        sys.exit(1)

def run_gui_version():
    root = tk.Tk()
    root.title("MIME Type File Renamer")

def run_gui_version():
    root = tk.Tk()
    root.title("MIME Type File Renamer")

    def process_with_gui():
        root_folder = filedialog.askdirectory()
        if not root_folder:
            return
        if os.path.exists(root_folder) and os.path.isdir(root_folder):
            processing_window = tk.Toplevel()
            processing_window.title("Processing...")
            tk.Label(processing_window, text="I may not seem like I'm doing anything but trust me, I am.").pack(pady=20)
            root.update()  # Update main GUI to reflect the processing window
            process_directory(root_folder)
            processing_window.destroy()
            messagebox.showinfo("Info", f"Processing finished. Check the xresults.txt file for details.")
        else:
            messagebox.showerror("Error", f"The path '{root_folder}' does not exist or is not a directory.")

    run_button = tk.Button(root, text="Select Folder and Run Script", command=process_with_gui)
    run_button.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    choice = input("Do you want to use the GUI version? (yes/no): ").lower().strip()
    if choice in ["yes", "y", ""]:  # Checks for 'yes', 'y', or an empty string (just pressing Enter)
        run_gui_version()
    else:
        run_command_line_version()
