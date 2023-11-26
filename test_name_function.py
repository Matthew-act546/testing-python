import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testing for 'name_function.py"""
    
    def test_first_last_name(self):
        """Do names matthew fernandez works?"""
        formatted_name = get_formatted_name("matthew", "fernandez")
        self.assertEqual(formatted_name, "Matthew Fernandez")

    def test_first_last_middle_name(self):
        """Do names like matthew cabance fernandez works?"""
        formatted_name = get_formatted_name(
            "matthew", "fernandez", "cabance")
        self.assertEqual(formatted_name, "Matthew Cabance Fernandez")
if __name__ == "__main__":
    unittest.main()