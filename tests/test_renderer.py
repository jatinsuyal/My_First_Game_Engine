import unittest
from src.core.Renderer import Renderer

class TestRenderer(unittest.TestCase):
    def setUp(self):
        self.renderer = Renderer()

    def test_initialization(self):
        self.assertIsNotNone(self.renderer)
        self.assertTrue(hasattr(self.renderer, 'render'))

    def test_render_function(self):
        result = self.renderer.render()
        self.assertTrue(result, "Render function did not return True")

if __name__ == '__main__':
    unittest.main()