from customtkinter import *
from dataclasses import dataclass
from modules.file_tools.MoveFiles import MoveFiles
from modules.frames.copy_widgets.get_dir_details import get_dir_details


def deepmove():
    """
    Gets details from user dialog to bulk move files of a specified file type.
    """
    dir_details = get_dir_details()
    all_files_in_src = MoveFiles(
        source_dir=dir_details["src_path"],
        dest_dir=dir_details["dst_path"],
        file_type=dir_details["file_type"],
    )
    all_files_in_src.move_recursively()


def bulkmove():
    """
    Gets details from user dialog to bulk move files of a specified file type.
    """
    dir_details = get_dir_details()
    all_files_in_src = MoveFiles(
        source_dir=dir_details["src_path"],
        dest_dir=dir_details["dst_path"],
        file_type=dir_details["file_type"],
    )
    all_files_in_src.move()


@dataclass
class MoveWidgets:
    """
    Widget for moving files of a specified file_type.
    """

    master_app: CTk

    def frame(self):
        """
        Sets UI details for the MoveWidget frame.
        """
        frame = CTkFrame(master=self.master_app, fg_color="#606190")
        frame.grid(row=0, column=1, padx=50, pady=50)

        CTkLabel(
            master=frame,
            text=f"Bulk move\nspecified file types",
            font=("Arial Bold", 20),
            justify="left",
        ).pack(expand=True, pady=(30, 15))

        CTkButton(master=frame, text=f"Move files\nrecursively", command=deepmove).pack(
            expand=True, fill="both", pady=(30, 15), padx=30
        )

        CTkButton(master=frame, text="Bulk move files", command=bulkmove).pack(
            expand=True, fill="both", pady=(30, 15), padx=30
        )
