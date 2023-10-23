from customtkinter import *
from dataclasses import dataclass
from modules import CopyFiles
from modules.frames.copy_widgets.get_dir_details import get_dir_details


def deepcopy():
    """
    Gets details from user dialog to bulk copy files of a specified file type.
    """
    dir_details = get_dir_details()
    all_files_in_src = CopyFiles(
        source_dir=dir_details["src_path"],
        dest_dir=dir_details["dst_path"],
        file_type=dir_details["file_type"],
    )
    all_files_in_src.copy_recursively()


def bulkcopy():
    """
    Gets details from user dialog to bulk copy files of a specified file type.
    """
    dir_details = get_dir_details()
    all_files_in_src = CopyFiles(
        source_dir=dir_details["src_path"],
        dest_dir=dir_details["dst_path"],
        file_type=dir_details["file_type"],
    )
    all_files_in_src.copy()


@dataclass
class CopyWidgets:
    """
    Widget for copying files of a specified file_type.
    """

    master_app: CTk

    def frame(self):
        """
        Sets UI details for the CopyWidget frame.
        """
        frame = CTkFrame(master=self.master_app, fg_color="#4EAC7D")
        frame.grid(row=2, column=1)

        CTkLabel(
            master=frame,
            text=f"Bulk copy\nspecified file types",
            font=("Arial Bold", 20),
            justify="left",
        ).pack(expand=True, pady=(30, 15))

        CTkButton(master=frame, text=f"Copy files\nrecursively", command=deepcopy).pack(
            expand=True, fill="both", pady=(30, 15), padx=30
        )

        CTkButton(master=frame, text="Bulk copy files", command=bulkcopy).pack(
            expand=True, fill="both", pady=(30, 15), padx=30
        )
