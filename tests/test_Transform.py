import unittest
from src.core.Transform import Transform

class TestTransform(unittest.TestCase):
    def setUp(self):
        self.transform = Transform()

    def test_default_position(self):
        self.assertEqual(self.transform.position, (0, 0, 0))

    def test_move(self):
        self.transform.move(1, 2, 3)
        self.assertEqual(self.transform.position, (1, 2, 3))

    def test_rotate(self):
        self.transform.rotate(90, 0, 0)
        self.assertEqual(self.transform.rotation, (90, 0, 0))

if __name__ == '__main__':
    unittest.main()