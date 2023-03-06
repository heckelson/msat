import os


class FileCollection:
    def __init__(self, starting_dir: str):
        self.file_list = self.__collect_filenames_in_dir(starting_dir)

    def __iter__(self):
        self.__n = 0
        return self

    def __next__(self):
        if self.__n < len(self.file_list):
            next_elem = self.file_list[self.__n]
            self.__n += 1
            return next_elem
        else:
            raise StopIteration

    @staticmethod
    def from_filename_list(filename_list: list[str]) -> "FileCollection":
        collection = FileCollection('.')
        collection.file_list = filename_list
        return collection

    @staticmethod
    def __collect_filenames_in_dir(start_dir: str) -> list[str]:
        """
        This function returns all filenames starting from a directory
        if given a directory, or just a list with 1 element
        if given a file.

        This function is taken and modified from my MRE course.
        Copyright Alexander Hecke 2022.
        """

        if not os.path.exists(start_dir):
            raise ValueError("The start directory does not exist!")

        if os.path.isdir(start_dir):
            # gather files down the file tree
            file_collection = []
            for path, _, files in os.walk(start_dir):
                for file in files:
                    file_collection.append(f"{path}{os.sep}{file}")

            # replace double // with single / for consistency
            file_collection = [filename.replace(f'{os.sep}{os.sep}', f'{os.sep}')
                               for filename in file_collection]

        else:
            # else we just put the filename into an array of size 1
            file_collection = [start_dir]

        return file_collection

    def keep_relevant_files(self,
                            override_file_endings:
                            tuple[str] = None) -> "FileCollection":
        """
        Filters filenames according to their file endings.
        One can optionally pass a tuple of file endings to override the default endings,
        which are (jpeg, jpg, png)

        """

        if override_file_endings is None:
            override_file_endings = ('jpeg', 'jpg', 'png')

        # this works only with tuples!
        filtered_files = list(filter(
            lambda file: file.lower().endswith(override_file_endings), self.file_list))

        # return a new object
        new_collection = FileCollection.from_filename_list(filtered_files)
        return new_collection

    def __repr__(self):
        return str(self.file_list)
