from pathlib import Path
from typing import List

"""
This module provides utility functions for working with file extensions 
and identifying file types (images, videos, music, documents) based on extensions. 
It also includes a function to list files in a directory.
"""

def get_file_extension(file_path: str) -> str:
    """
    Extracts the file extension from a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension, including the leading dot (e.g., '.txt').
    """
    return Path(file_path).suffix

def is_image(file_extension: str) -> bool:
    """
    Determines if a given file extension belongs to an image file.

    Args:
        file_extension (str): The file extension to check.

    Returns:
        bool: True if the file extension corresponds to an image file, otherwise False.
    """
    image_extensions = [
        ".bmp", ".jpg", ".jpeg", ".png", ".gif", ".webp", 
        ".svg", ".ai", ".eps", ".tiff", ".raw", ".ico", ".heic"
    ]
    
    return file_extension.lower() in image_extensions

def is_video(file_extension: str) -> bool:
    """
    Determines if a given file extension belongs to a video file.

    Args:
        file_extension (str): The file extension to check.

    Returns:
        bool: True if the file extension corresponds to a video file, otherwise False.
    """
    video_extensions = [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", 
        ".webm", ".3gp", ".mpeg", ".m4v"
    ]
    
    return file_extension.lower() in video_extensions

def is_music(file_extension: str) -> bool:
    """
    Determines if a given file extension belongs to an audio or music file.

    Args:
        file_extension (str): The file extension to check.

    Returns:
        bool: True if the file extension corresponds to a music file, otherwise False.
    """
    music_extensions = [
        ".flac", ".wav", ".aiff", ".alac", 
        ".mp3", ".aac", ".ogg", ".wma", 
        ".midi", ".m4a"
    ]
    
    return file_extension.lower() in music_extensions

def is_document(file_extension: str) -> bool:
    """
    Determines if a given file extension belongs to a document file.

    Args:
        file_extension (str): The file extension to check.

    Returns:
        bool: True if the file extension corresponds to a document file, otherwise False.
    """
    document_extensions = [
        ".txt", ".doc", ".docx", ".odt", 
        ".xls", ".xlsx", ".ods", 
        ".ppt", ".pptx", ".odp", 
        ".pdf", ".xps", ".rtf", ".csv", ".md", ".tex"
    ]
    
    return file_extension.lower() in document_extensions

def list_files_in_directory(directory_path: str) -> List[str]:
    """
    Lists all files in a given directory.

    Args:
        directory_path (str): The path to the directory.

    Raises:
        FileNotFoundError: If the specified path does not exist or is not a directory.

    Returns:
        List[str]: A list of filenames present in the directory.
    """
    directory = Path(directory_path)
    
    if not directory.is_dir():
        raise FileNotFoundError(f"The directory {directory_path} does not exist or is not a directory.")
    
    files_list = [file.name for file in directory.iterdir() if file.is_file()]

    return files_list
