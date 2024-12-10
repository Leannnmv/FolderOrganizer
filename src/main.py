"""
Main Script for Directory Organizer

Este programa organiza los archivos en un directorio seleccionado por el usuario.
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
            logging.info(f"Carpeta seleccionada: {folder_path}")
            organize_directory(folder_path)
            logging.info("Organización completada con éxito.")
        else:
            print("No se seleccionó ninguna carpeta.")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
    finally:
        logging.info("Finalizando el programa.")
        sys.exit(0)

if __name__ == "__main__":
    main()
