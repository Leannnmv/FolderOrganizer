"""
Main Script for Directory Organizer

This program organizes files in a directory selected by the user.
"""
import sys
import logging
from organizer import organize_directory
from interface import get_folder_path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        folder_path = get_folder_path()
        if folder_path:
            logging.info(f"Selected folder: {folder_path}")
            organize_directory(folder_path)
            logging.info("Organization completed successfully.")
        else:
            print("No folder was selected.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        logging.info("Closing the program.")
        sys.exit(0)

if __name__ == "__main__":
    main()
