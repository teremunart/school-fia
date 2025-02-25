import os
import requests
import webbrowser


def download_images(start, end, save_folder):
    base_url = ""

    # Create the folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    for i in range(start, end + 1):
        img_url = f"{base_url}{i}.jpg"
        img_path = os.path.join(save_folder, f"{i}.jpg")

        webbrowser.open(img_url)

if __name__ == "__main__":
    start_number = 1  # Change as needed
    end_number = 28  # Change as needed
    save_directory = "downloaded_images"  # Folder name

    download_images(start_number, end_number, save_directory)
