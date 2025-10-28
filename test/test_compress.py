import unittest
from pathlib import Path
import zipfile
import tempfile
from src.compress import compress_folder_to_zip

class TestCompressFolder(unittest.TestCase):
    
    def test_folder_compression(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)
            subfolder = temp_dir_path / "test_folder"
            subfolder.mkdir()

            file1 = subfolder / "file1.txt"
            file1.write_text("Hello")
            file2 = subfolder / "file2.txt"
            file2.write_text("World")

            zip_path = compress_folder_to_zip(subfolder)

            self.assertTrue(zip_path.exists(), "Zip file was not created")

            with zipfile.ZipFile(zip_path, 'r') as zipf:
                zip_files = zipf.namelist()
                self.assertIn("file1.txt", zip_files)
                self.assertIn("file2.txt", zip_files)

                with zipf.open("file1.txt") as f:
                    self.assertEqual(f.read().decode(), "Hello")
                with zipf.open("file2.txt") as f:
                    self.assertEqual(f.read().decode(), "World")

if __name__ == "main":
    unittest.main()
