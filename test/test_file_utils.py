import subprocess
import unittest

from file_utils.filecollection import FileCollection
from file_utils.utils import sha256hash


class FileUtilsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.files = FileCollection(starting_dir='../media')

    def test_sha256_matches(self):
        # compare to the Linux impl of sha256
        for file in self.files:
            # format it the same way s.t. they match if the hashes match too
            my_impl = f"{sha256hash(file)}  {file}\n"
            reference = subprocess.run(["sha256sum", file], capture_output=True) \
                .stdout.decode()

            self.assertEqual(my_impl, reference)

    def test_can_filter_FileCollections(self):
        print(self.files.keep_relevant_files(('jpeg',)))


if __name__ == '__main__':
    unittest.main()
