import unittest
import os
from stegno import hide_message_in_image, reveal_message_from_image

class TestSteganography(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setting up before any test cases run: define the path for the test image.
        cls.test_image_path = os.path.join(os.path.dirname(__file__), 'tests', 'test_image.png')
        cls.test_message = "This is a secret message"

    def setUp(self):
        # Ensure the test environment is clean before each test
        self.output_path = os.path.splitext(self.__class__.test_image_path)[0] + "_secret.png"
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_hide_and_reveal_message(self):
        # Test hiding the message in the image
        # output_path = hide_message_in_image(self.__class__.test_image_path, self.__class__.test_message)
        # self.assertIsNotNone(output_path, "The message embedding function failed to return the path to the modified image.")

        # Test revealing the message from the image
        # revealed_message = reveal_message_from_image(output_path)
        # self.assertEqual(self.__class__.test_message, revealed_message, "The revealed message does not match the original message.")
        pass
    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

if __name__ == "__main__":
    unittest.main()
    