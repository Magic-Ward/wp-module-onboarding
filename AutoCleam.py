import os
import random

def delete_random_file(directory='.'):
    # Get all regular (non-hidden) files in the directory
    files = [
        f for f in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, f))  # must be a file
        and not f.startswith('.')                      # skip hidden files
        and not f.lower().endswith(('.sys', '.dll'))   # skip system-like files
    ]

    if not files:
        print("No eligible files found to delete.")
        return

    # Pick one at random
    target = random.choice(files)
    path = os.path.join(directory, target)

    try:
        os.remove(path)
        print(f"Deleted random file: {target}")
    except Exception as e:
        print(f"Failed to delete {target}: {e}")

# Run it
delete_random_file()
