from customtkinter import filedialog, CTkInputDialog


def get_dir_from_user() -> dict:
    """
    Handles the user dialog to get details about deleting specified file types.
    #### Returns dict of strings:
    key src_path (str): source path.
    key file_type (str): File type such as .csv, .pdf, .txt, etc.
    """
    # Ask user for the source path.
    src_path = filedialog.askdirectory(
        initialdir="D:/dev/tests", mustexist=True, title="Select what to delete"
    )

    if src_path:
        # Ask user to enter file type.
        enter_file_type = CTkInputDialog(
            text="Enter a file extension to delete:", title="Enter file extension"
        )
        # Retrieve the user's input.
        file_type = enter_file_type.get_input()
        if file_type:
            # TODO: Setup logging and pass this to logs.
            print(f"Source path: {src_path}")
            print(f"File type: {file_type}")
            return {
                "src_path": src_path,
                "file_type": file_type,
            }
