import os
import shutil
from dataclasses import dataclass


@dataclass
class MoveFiles:
    """
    ### Moves files from a source path to a destination path.
    #### Args:
    source_dir (str): Path to source dir of files you want to move.
    dest_dit (str): Path to destination dir of where you want to move the files to.
    file_type (str): File extension of the files you want to move.
    """

    source_dir: str
    dest_dir: str
    file_type: str

    def move(self):
        """Moves specified file_types from source to destination."""
        for filename in os.listdir(self.source_dir):
            # If filename ends with specified file type.
            if filename.endswith(self.file_type.lower()) or filename.endswith(
                self.file_type.upper()
            ):
                # Move files from source to destination.
                shutil.move(os.path.join(self.source_dir, filename), self.dest_dir)

    def move_recursively(self):
        """Moves specified file_types from source to destination recursively."""
        for root, dirs, files in os.walk(self.source_dir):
            for filename in files:
                # If filename ends with specified file_type.
                if filename.endswith(self.file_type.lower()) or filename.endswith(
                    self.file_type.upper()
                ):
                    # Move files from source to destination.
                    shutil.move(os.path.join(root, filename), self.dest_dir)
