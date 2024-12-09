from interface import get_folder_path
import organizer as org

def main():
    folder_path = get_folder_path()
    
    if folder_path:
        org.create_folders(folder_path)
        org.organize_directory(folder_path)

if __name__ == "__main__":
    main()