import unittest
from pathlib import Path

from extraction import extract_images_from_pdf

BASE_PATH = Path(__file__).resolve().parent
output_directory = BASE_PATH / "output"
input_directory = BASE_PATH / "input"
class MyTestCase(unittest.TestCase):
    def test_something(self):
        images=extract_images_from_pdf(str(input_directory),str(output_directory))
        expected=['000edd72-8c4b-4447-93b9-cc398b3d1fc0_page0_index0.png', '000edd72-8c4b-4447-93b9-cc398b3d1fc0_page1_index0.png', '000edd72-8c4b-4447-93b9-cc398b3d1fc0_page2_index0.png', '000edd72-8c4b-4447-93b9-cc398b3d1fc0_page3_index0.png']
        self.assertEqual(expected, images)  # add assertion here

if __name__ == '__main__':
    unittest.main()
