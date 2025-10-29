import unittest
import tempfile
import shutil
from pathlib import Path

from src.compress_subfolders import compress_subfolders  # adjust this import if needed

class TestCompressSubfolders(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = Path(tempfile.mkdtemp())

        # Create subfolders inside it
        (self.test_dir / "folder1").mkdir()
        (self.test_dir / "folder2").mkdir()

        # Add some files inside each subfolder
        for folder in ["folder1", "folder2"]:
            file_path = self.test_dir / folder / "file.txt"
            file_path.write_text("test data")

    def tearDown(self):
        # Clean up after each test
        shutil.rmtree(self.test_dir)

    def test_creates_zip_for_each_subfolder(self):
        compress_subfolders(self.test_dir)

        # Expect zip files for each subfolder
        zip1 = self.test_dir / "folder1.zip"
        zip2 = self.test_dir / "folder2.zip"

        self.assertTrue(zip1.exists(), "folder1.zip should be created")
        self.assertTrue(zip2.exists(), "folder2.zip should be created")

    def test_nonexistent_directory(self):
        fake_dir = self.test_dir / "does_not_exist"
        result = compress_subfolders(fake_dir)

        # It shouldn't crash or create any zips
        zips = list(self.test_dir.glob("*.zip"))
