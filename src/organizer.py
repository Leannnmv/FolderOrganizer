import logging
from pathlib import Path
import utilities as util

"""
This module provides functions to organize files into specific directories
based on their extensions. It allows creating necessary folders and moving 
files into their corresponding folder (Images, Videos, Music, Documents).
"""

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_folders(base_path: str) -> None:
    """
    Creates folders for organizing files into specific categories (Images, Videos, Music, Documents) 
    inside the given base path, if they do not already exist.

    Args:
        base_path (str): The base path where the folders should be created.

    Returns:
        None
    """
    directories = ['Images', 'Videos', 'Music', 'Documents', 'Others']
    
    for folder in directories:
        dir_path = Path(base_path) / folder
        if not dir_path.is_dir():
            dir_path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created folder: {dir_path}")
        else:
            logging.info(f"Folder already exists: {dir_path}")
    return None

def move_file(file_path: str, target_folder: str) -> None:
    """
    Moves a file to a target folder. If a file with the same name already exists 
    in the target folder, it appends a counter to the filename to avoid overwriting.

    Args:
        file_path (str): The path of the file to move.
        target_folder (str): The target folder where the file should be moved.

    Returns:
        None
    """
    file = Path(file_path)
    destiny = Path(target_folder)
    
    destination_file = destiny / file.name
    
    # Ensure the filename is unique in the target directory by appending a counter
    counter = 1
    while destination_file.exists():
        destination_file = destiny / f"{file.stem}_{counter}{file.suffix}"
        counter += 1
    
    # Move the file
    file.rename(destination_file)
    logging.info(f"Moved file: {file} to {destination_file}")
    
    return None

def organize_directory(directory_path: str) -> None:
    """
    Organizes files in the given directory by moving them into appropriate folders
    (Images, Videos, Music, Documents) based on their file extensions. It uses
    utility functions to check file types and moves them accordingly.

    Args:
        directory_path (str): The path of the directory to organize.

    Returns:
        None
    """
    try:
        files_list = util.list_files_in_directory(directory_path)
        logging.info(f"Found {len(files_list)} files in {directory_path}.")
    
        # Mapping functions that check file type against corresponding folder paths
        folder_mapping = {
            util.is_image: Path(directory_path) / "Images",
            util.is_video: Path(directory_path) / "Videos",
            util.is_music: Path(directory_path) / "Music",
            util.is_document: Path(directory_path) / "Documents"
        }
        
        others_folder = Path(directory_path) / "Others"
        
        # Create the "Others" folder if it doesn't exist
        if not others_folder.is_dir():
            others_folder.mkdir(parents=True, exist_ok=True)

        # Iterate over the files and move them to the appropriate folder
        for file in files_list:
            file_path = Path(directory_path) / file
            file_extension = util.get_file_extension(file_path)
            
            moved = False  # Flag to check if the file was moved to a valid folder
            
            for check_function, folder_name in folder_mapping.items():
                if check_function(file_extension):
                    move_file(file_path, folder_name)
                    moved = True
                    break
            
            # If the file wasn't moved to any of the valid folders, move it to "Others"
            if not moved:
                move_file(file_path, others_folder)
                
    except Exception as e:
        logging.error(f"Error organizing directory {directory_path}: {e}")
    
    return None
