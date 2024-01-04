import os
import dotenv as env

env.load_dotenv()


class Rename:
    def __init__(self):
        self.folder_path = env.get("SOURCE_DESTINY")

    def replace_spaces(self):
        # Check if the folder path exists
        if not os.path.exists(self.folder_path):
            print(f'The path "{self.folder_path}" does not exist.')
            return

        # Traverse files in the folder
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)

            # Check if it's a file
            if os.path.isfile(file_path):
                new_filename = filename.replace(
                    " ", ""
                )  # Remove spaces from the file name

                # Check if the file name needs to be changed
                if new_filename != filename:
                    new_file_path = os.path.join(self.folder_path, new_filename)
                    os.rename(file_path, new_file_path)
                    print(
                        f'The file "{filename}" has been renamed to "{new_filename}".'
                    )
