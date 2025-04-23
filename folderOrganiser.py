import os
import shutil

# Set this to the folder you want to clean up
TARGET_FOLDER = os.path.expanduser("~/Downloads")

# Define categories and file extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh", ".bat"],
    "bins": [".bin", ".exe"],
    "Others": [] # Catch-all for uncategorised files

}

# List to store moved files for undo functionality
moved_files = []

# Track created category folders to avoid redundant mkdir calls
created_categories = set ()


def organise_folder(folder, dry_run=False):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath):
            moved = False
            for category, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    move_file(filepath, folder, category, dry_run)
                    moved = True
                    break
            if not moved:
                move_file(filepath, folder, "Others", dry_run)

def move_file(filepath, folder, category, dry_run=False):
    category_folder = os.path.join(folder, category)
    os.makedirs(category_folder, exist_ok=True)

    # Determine the new file path
    new_path = os.path.join(category_folder, os.path.basename(filepath))

    if dry_run:
        print(f"[Dry Run] would move {os.path.basename(filepath)} → {category}")
    else:
        moved_files.append((filepath, new_path))
        shutil.move(filepath, new_path)
        print(f"Moved {os.path.basename(filepath)} → {category}")

def undo_changes():
    # Loop through the list and move them back to their original location
    for original, moved in reversed(moved_files):
        if os.path.exists(moved): # Check if the moved file still exists
            shutil.move(moved, original)
            print(f"Reverted {os.path.basename(moved)} back to its original location.")

    # Clear the moved files list after undo
    moved_files.clear()

if __name__ == "__main__":
    action = input("Choose action - [o]organise / [u]ndo / [d]ry run: ").strip().lower()
    if action == "o":
        organise_folder(TARGET_FOLDER, dry_run=False) # Actual move
        print("🎉 Done organising!")
    elif action == "u": # Undo moves
        undo_changes()
        print("🔄 Undo complete!")
    elif action == "d":
        organise_folder(TARGET_FOLDER, dry_run=True) # Dry ru only
        print("👀 Dry run complete! Check the output for simulated moves.")
    else:
        print("❓ Unknown choice.")

