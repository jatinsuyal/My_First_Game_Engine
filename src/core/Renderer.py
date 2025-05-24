class Renderer:
    """
    A basic Renderer class for handling rendering logic in the game engine.
    """

    def __init__(self):
        # Initialize any rendering parameters (e.g., screen, FPS, etc.)
        self.rendering_enabled = True
        self.render_count = 0

    def render(self):
        """
        A render function to handle drawing objects to the screen.
        """
        if self.rendering_enabled:
            # Placeholder for rendering logic
            self.render_count += 1
            print(f"Rendering frame {self.render_count}")
            return True
        else:
            print("Rendering is disabled.")
            return False

    def toggle_rendering(self):
        """
        Enables or disables rendering.
        """
        self.rendering_enabled = not self.rendering_enabled
        state = "enabled" if self.rendering_enabled else "disabled"
        print(f"Rendering has been {state}.")