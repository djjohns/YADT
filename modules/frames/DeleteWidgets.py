from customtkinter import *
from dataclasses import dataclass
from modules.file_tools.DeleteFiles import DeleteFiles
from modules.frames.delete_widgets.get_dir_from_user import get_dir_from_user


def delete_file_types_in_src():
    """
    Gets details from user dialog to bulk move files of a specified file type.
    """
    dir_details = get_dir_from_user()
    all_files_in_src = DeleteFiles(
        source_dir=dir_details["src_path"],
        file_type=dir_details["file_type"],
    )
    all_files_in_src


@dataclass
class DeleteWidgets:
    master_app: CTk

    def frame(self):
        frame = CTkFrame(master=self.master_app, fg_color="#CD8C67")
        frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

        CTkLabel(
            master=frame,
            text=f"Bulk delete\nspecified file types",
            font=("Arial Bold", 20),
            justify="left",
        ).pack(expand=True, pady=[10, 10])
        CTkButton(
            master=frame,
            text="Bulk delete",
            command=delete_file_types_in_src,
        ).pack(expand=True, fill="both", pady=(30, 15), padx=30)
