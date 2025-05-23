import unittest
from src.entities.Button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        self.button = Button(label="Click Me")

    def test_button_has_label(self):
        self.assertEqual(self.button.label, "Click Me")

    def test_button_click(self):
        self.button.click()
        self.assertTrue(self.button.was_clicked)

if __name__ == '__main__':
    unittest.main()