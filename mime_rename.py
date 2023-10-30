import os
import magic
import sys

# Define a dictionary to map MIME types to file extensions
mime_to_extension = {
    'JPEG image data': '.jpg',
    'PNG image data': '.png',
    'ASCII text': '.txt',
    'PDF document': '.pdf',
    'FLV (Flash Video)': '.flv',
    'ISO Media, MPEG v4 system': '.mp4',
    'ISO Media, Apple QuickTime movie': '.mov',
    'AVI (Audio Video Interleaved)': '.avi',
    'ASF (Advanced / Active Streaming Format)': '.wmv',
    'WebM': '.webm',
    'Ogg data': '.ogv',
    '3GPP multimedia file': '.3gp',
    '3GPP2 multimedia file': '.3g2',
    'MPEG sequence': '.mpeg',
    'Matroska data': '.mkv',
    'H.264 video': '.h264',
    'H.265 video': '.h265',
    # Add 'video/vnd.mpegurl': '.m3u8' if you find a corresponding detailed MIME description.
}

# Function to get the MIME type of a file
def get_mime_type(magic_obj, file_path):
    return magic_obj.from_file(file_path)

def process_directory(directory):
    magic_obj = magic.Magic()
    output_file = "xresults.txt"
    counter = 0
    while os.path.exists(output_file):
        counter += 1
        output_file = f"xresults{counter}.txt"
    with open(output_file, 'w') as f:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                mime_type = get_mime_type(magic_obj, file_path)

                f.write(f"Processing: {file_path} - Detected MIME type: {mime_type}\n")

                found_extension = None
                for key in mime_to_extension:
                    if key in mime_type:
                        found_extension = mime_to_extension[key]
                        break

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

if __name__ == "__main__":
    user_input = input("Enter the path to the folder you want to scan: ")
    root_folder = user_input.strip()  # Remove any leading/trailing white spaces

    if os.path.exists(root_folder) and os.path.isdir(root_folder):
        print(f"Writing results to xresults.txt")
        process_directory(root_folder)
    else:
        print(f"The path '{root_folder}' does not exist or is not a directory.")
        sys.exit(1)
