import os
import shutil
from dataclasses import dataclass


@dataclass
class CopyFiles:
    """
    Copy specified file_types from source to destination directories.
    """

    source_dir: str
    dest_dir: str
    file_type: str

    def copy(self):
        """
        Step through the dir list and check for specified file_type. If found copy to dest_dir.
        """
        for filename in os.listdir(self.source_dir):
            # If filename ends with specified file type.
            if filename.endswith(self.file_type.lower()) or filename.endswith(
                self.file_type.upper()
            ):
                # Copy files from source to destination.
                shutil.copy(os.path.join(self.source_dir, filename), self.dest_dir)

    def copy_recursively(self):
        """
        Walk through the dirs from root dir to find all specified files. If specified file is found copy to dest_dir.
        """
        for root, dirs, files in os.walk(self.source_dir):
            for filename in files:
                # If filename ends with specified file_type.
                if filename.endswith(self.file_type.lower()) or filename.endswith(
                    self.file_type.upper()
                ):
                    # Copy files from source to destination.
                    shutil.copy(os.path.join(root, filename), self.dest_dir)
