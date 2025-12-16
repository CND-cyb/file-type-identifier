# main.py

import argparse
import os
from signatures import FILE_SIGNATURES

def get_file_type(file_path):
    """
    Reads the first 20 bytes of a file
    """
    with open(file_path, 'rb') as f:
        file_header = f.read(20)
        hex_signature = ' '.join(f'{byte:02X}' for byte in file_header)

        for file_type, signature in FILE_SIGNATURES.items():
            if hex_signature.startswith(signature):
                return file_type
    return "unknown"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the extension of a file")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-f","--file", action="store_true")
    group.add_argument("-d","--directory", action="store_true")
    parser.add_argument("path", help="a path of file/directory")
    args = parser.parse_args()

    if args.file:
        try:
            file_type = get_file_type(args.path)
            name, ext = os.path.splitext(args.path)
            if file_type != ext[1:].lower() and file_type!="unknown":
                print(f"ALERT MISMATCH! The file type is : {file_type}")
            else:
                print(f"The file type is: {file_type}")
        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print(f"Error : {e}")

    if args.directory:
        try:
            for root, dirs, files in os.walk(f'{args.path}', topdown=True):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_type = get_file_type(file_path)
                    name, ext = os.path.splitext(file)
                    if file_type != ext[1:].lower() and file_type!="unknown":
                        print(f"\n- ALERT MISMATCH! The file type of {file} is : {file_type}")
                    else:
                        print(".", end="")
        except Exception as e:
            print(f"Error : {e}")