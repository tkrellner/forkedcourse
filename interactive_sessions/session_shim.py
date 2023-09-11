
def move_file_if_new_name_doesnt_exist(old_path, new_path):
    """ Rename a file, but only if new filename doesn't exist

    Args:
        old_path: Current file name
        new_path: New file name
    """
    # Check if the old file exists
    if not os.path.exists(old_path):
        print(f"Error: Source file '{old_path}' doesn't exist.")
        return
    
    # Check if the destination file exists
    if os.path.exists(new_path):
        print(f"Error: Destination file '{new_path}' already exists.")
        return
    
    # Move/Rename the file
    shutil.move(old_path, new_path)
    print(f"Moved '{old_path}' to '{new_path}'.")

def download_shim_file(url, old_filename, new_filename):
    """ Download a new file, but only if a backup exists

    """
    # Check if the new filename already exists
    if not os.path.exists(new_filename):
        print(f"Error: '{new_filename}' doesn't exist. Aborting download to avoid overwriting '{old_filename}'.")
        return
    
    # Download the file from the given URL
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(old_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Downloaded new content to '{old_filename}'.")
    else:
        print(f"Error: Failed to download the file from {url}. Status code: {response.status_code}")

def session_shim(session):
    """
    Provides the correct filenames and url for a session shim

    Args:
        session name (str)
        
        Should match the session name in the repository.
        For example: 
            "4-1_pandas"
            or "3-1_numpy", 
            etc...

    Returns:
        url, old_filename, new_filename
    """
    url = "https://raw.githubusercontent.com/" \
    "environmental-data-science/eds217_2023/" \
    f"main/interactive_sessions/{session}.ipynb"
    old_filename = f"{session}.ipynb"
    new_filename = f"no_track_{session}.ipynb"
    return url, old_filename, new_filename