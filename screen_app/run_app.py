import pyglet
from pyglet.window import mouse, key

import screen_app.msg

import rclpy



def show_app(node):
    """TODO"""
    AppWindow(node)

    # Enter main event loop.
    pyglet.app.run()


class AppWindow(pyglet.window.Window):
    def __init__(self, node, width=1920, height=1080, screen_index=-1):
        self._init_graphics(width, height)

        # Set a variable to check if the SHIFT key is pressed.
        self._is_shift = False
        self._is_alt = False
        self._is_a = False

        self.name = 'App'

        self.node = node

        self._init_ros()
        # rospy.on_shutdown(self.on_close)

        # Initialising pyglet window.
        self.node.get_logger().info('Creating the window')
        style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS
        super().__init__(width, height, self.name, style=style)

        display = pyglet.canvas.get_display()
        screens = display.get_screens()
        active_screen = screens[screen_index]
        self.set_location(active_screen.x, active_screen.y)

        self.node.get_logger().info('Ready!')

    # GUI methods.

    def on_draw(self):
        self.clear()
        self.graphics.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self.publish_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        self.publish_mouse_press(x, y, button)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.publish_mouse_drag(x, y, buttons, dx=dx, dy=dy)

    def on_mouse_release(self, x, y, button, modifiers):
        self.publish_mouse_release(x, y, button)

    def on_key_press(self, symbol, modifiers):
        self.publish_key_press(symbol, modifiers)

        if symbol == key.LSHIFT or symbol == key.RSHIFT:
            self._is_shift = True
        if symbol == key.LALT or symbol == key.RALT:
            self._is_alt = True
        if symbol == key.A:
            self._is_a = True

        # # Execute other things.
        # if symbol == key.ESCAPE: # and modifiers & key.MOD_CTRL:
        #     rospy.signal_shutdown('App window is closed by ESCAPE.')

  
    def on_key_release(self, symbol, modifiers):
        self.publish_key_release(symbol, modifiers)
        if symbol == key.LSHIFT or symbol == key.RSHIFT:
            self._is_shift = False
        if symbol == key.LALT or symbol == key.RALT:
            self._is_alt = False
        if symbol == key.A:
            self._is_a = False

    def on_close(self):
        self.node.get_logger().info("Closing application window.")
        self.close()

    # Custom public methods.

    def on_context_lost(self, **kwargs):
        pass
        # node.get_logger().info('context lost')

    def update(self):
        pyglet.clock.schedule_once(self.update_callback, 0)

    def update_callback(self, dt):
        self.on_update()

    def on_update(self):
        pass


    # Private methods.

    def _init_graphics(self, width, height, image_container=None, batch=None):
        graphics = Graphics(width, height, batch=batch)
        batch = graphics.batch

        # Create objects like labels and add to the batch.
        
        self.graphics = graphics

    # ROS methods.

    def _init_ros(self):
        # Initialize the publishers.
        self.mouse_press_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~mouse_press', queue_size=10)

        self.mouse_drag_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~mouse_drag', queue_size=10)

        self.mouse_release_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~mouse_release', queue_size=10)

        self.mouse_motion_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~mouse_motion', queue_size=10)
        self.key_press_pub = self.node.create_publisher(
            screen_app.msg.Key, '~key_press', queue_size=10)

        self.key_release_pub = self.node.create_publisher(
            screen_app.msg.Key, '~key_release', queue_size=10)

        # Initialise messages.
        self.mouse_message = screen_app.msg.Mouse()
        self.key_message = screen_app.msg.Key()

    def make_mouse_message(self, x, y, buttons=mouse.LEFT, dx=0, dy=0):
        self.mouse_message.header.frame_id = self.name
        self.mouse_message.header.stamp = self.node.get_clock().now()
        self.mouse_message.header.seq += 1
        self.mouse_message.x = x
        self.mouse_message.y = y
        self.mouse_message.dx = dx
        self.mouse_message.dy = dy
        self.mouse_message.left = bool(buttons & mouse.LEFT)
        self.mouse_message.right = bool(buttons & mouse.RIGHT)

    def make_key_message(self, symbol, modifiers):
        self.key_message.header.frame_id = self.name
        self.key_message.header.stamp = self.node.get_clock().now()
        self.key_message.header.seq += 1
        self.key_message.symbol = str(symbol)
        self.key_message.modifiers = str(modifiers)

    def publish_button_press(self, name, state):
        message = make_button_message(self.name, name, state)
        self.button_press_pub.publish(message)

    def publish_mouse_motion(self, x, y, dx, dy):
        self.make_mouse_message(x, y, dx=dx, dy=dy)
        self.mouse_motion_pub.publish(self.mouse_message)

    def publish_mouse_press(self, x, y, button):
        self.make_mouse_message(x, y, button)
        self.mouse_press_pub.publish(self.mouse_message)

    def publish_mouse_release(self, x, y, button):
        self.make_mouse_message(x, y, button)
        self.mouse_release_pub.publish(self.mouse_message)

    def publish_mouse_drag(self, x, y, buttons, dx, dy):
        self.make_mouse_message(x, y, buttons, dx=dx, dy=dy)
        self.mouse_drag_pub.publish(self.mouse_message)

    def publish_key_press(self, symbol, modifiers):
        self.make_key_message(symbol, modifiers)
        self.key_press_pub.publish(self.key_message)

    def publish_key_release(self, symbol, modifiers):
        self.make_key_message(symbol, modifiers)
        self.key_release_pub.publish(self.key_message)




class Graphics(object):
    """docstring for Graphics"""

    def __init__(self, width=1920, height=1080, batch=None):
        self.width = width
        self.height = height

        if batch is None:
            self.batch = pyglet.graphics.Batch()
        else:
            self.batch = batch


def main(args=None):
    # Initialise the scenario's ROS node.
    #rospy.init_node('screen_app', anonymous=False)
    rclpy.init(args=args)
    node = rclpy.create_node('screen_app', anonymous=False)


    node.get_logger().info("Starting a screen application node...")

    # Initialise the human/app window.
    show_app(node)

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()

    # rospy.spin()


if __name__ == '__main__':
    main()
