import shutil
from pathlib import Path


def move_jpg_files(source_folder, destination_folder):
    """Move JPG files from the source folder into the destination folder."""
    source = Path(source_folder).expanduser()
    destination = Path(destination_folder).expanduser()

    if not source.exists() or not source.is_dir():
        print(f"Error: Source folder does not exist: {source}")
        return

    # Prevent moving files into the same folder or one of its subfolders.
    source_resolved = source.resolve()
    destination_resolved = destination.resolve()

    if destination_resolved == source_resolved or source_resolved in destination_resolved.parents:
        print("Error: Destination must be different from, and outside, the source folder.")
        return

    destination.mkdir(parents=True, exist_ok=True)

    jpg_files = [
        file_path for file_path in source.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == ".jpg"
    ]

    if not jpg_files:
        print("No .jpg files were found in the source folder.")
        return

    moved_count = 0

    for file_path in jpg_files:
        target_path = destination / file_path.name

        # Avoid overwriting a file with the same name.
        if target_path.exists():
            stem = file_path.stem
            suffix = file_path.suffix
            counter = 1

            while target_path.exists():
                target_path = destination / f"{stem}_{counter}{suffix}"
                counter += 1

        try:
            shutil.move(str(file_path), str(target_path))
            print(f"Moved: {file_path.name} -> {target_path.name}")
            moved_count += 1
        except OSError as error:
            print(f"Could not move {file_path.name}: {error}")

    print(f"\nCompleted! {moved_count} JPG file(s) moved.")


def main():
    print("=" * 48)
    print("       JPG FILE ORGANIZER - TASK AUTOMATION")
    print("=" * 48)

    source_folder = input("Enter the source folder path: ").strip().strip('"')
    destination_folder = input("Enter the destination folder path: ").strip().strip('"')

    if not source_folder or not destination_folder:
        print("Error: Please enter both folder paths.")
        return

    move_jpg_files(source_folder, destination_folder)


if __name__ == "__main__":
    main()
