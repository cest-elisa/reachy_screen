#!/usr/bin/env python3

import pyglet
from pyglet.window import mouse, key

import screen_app.msg

import rclpy


def show_app(node):
    """Create the window."""
    AppWindow(node)

    # Enter main event loop.
    pyglet.app.run()


class AppWindow(pyglet.window.Window):
    """A simple application to monitor mouse & keyboard events via ROS 2."""

    def __init__(self, node, width=1920, height=1080, screen_index=-1):
        self.last_pressed_pos = None
        self.last_dragged_pos = None
        self.last_released_pos = None

        self._init_graphics(width, height)

        self.name = 'Screen Testing Application'

        self.node = node

        self._init_ros()

        # Initialising pyglet window.
        self.node.get_logger().info('Creating the window.')
        super().__init__(width, height, self.name, resizable=True)

        display = pyglet.canvas.get_display()
        screens = display.get_screens()

        self.node.get_logger().info('Found {} screens:'.format(len(screens)))
        for screen in screens:
            self.node.get_logger().info('\t{}'.format(screen))

        active_screen = screens[screen_index]
        self.set_location(active_screen.x, active_screen.y)

        self.node.get_logger().info(
            'Moved to screen at index {}'.format(screen_index))
        self.node.get_logger().info('Ready!')

    # GUI methods.

    def on_draw(self):
        self.clear()
        pyglet.gl.glClearColor(1, 1, 1, 1)
        self.graphics.batch.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        self._publish_mouse_motion(x, y, dx, dy)

    def on_mouse_press(self, x, y, button, modifiers):
        self._publish_mouse_press(x, y, button)

        self.node.get_logger().info(
            'Mouse pressed at x:{}, y:{}'.format(x, y))

        self.last_pressed_pos = (x, y)
        self.pressed_label.text = self._make_pressed_text()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self._publish_mouse_drag(x, y, buttons, dx=dx, dy=dy)

        self.node.get_logger().info(
            'Mouse dragged at x:{}, y:{}'.format(x, y))

        self.last_dragged_pos = (x, y)
        self.dragged_label.text = self._make_dragged_text()

    def on_mouse_release(self, x, y, button, modifiers):
        self._publish_mouse_release(x, y, button)

        self.node.get_logger().info(
            'Mouse released at x:{}, y:{}'.format(x, y))

        self.last_released_pos = (x, y)
        self.released_label.text = self._make_released_text()

    def on_key_press(self, symbol, modifiers):
        self._publish_key_press(symbol, modifiers)

        self.node.get_logger().info(
            make_key_info_text(symbol, modifiers, 'pressed'))

        if symbol == key.ESCAPE:
            self.on_close()

    def on_key_release(self, symbol, modifiers):
        self._publish_key_release(symbol, modifiers)

        self.node.get_logger().info(
            make_key_info_text(symbol, modifiers, 'released'))

        if symbol == key.ESCAPE:
            self.on_close()

    def on_close(self):
        self.node.get_logger().info("Closing application window.")
        self.node.destroy_node()
        self.close()
        rclpy.shutdown()

    # def on_resize(self, width, height):
    #     self.node.get_logger().info(
    #         'The window was resized to {}x{}'.format(width, height))

    # Custom public methods.

    def on_context_lost(self, **kwargs):
        node.get_logger().info('context lost')

    # Private methods.

    def _init_graphics(self, width, height, image_container=None, batch=None):
        graphics = Graphics(width, height, batch=batch)
        batch = graphics.batch

        # Create objects like labels and add to the batch.

        # A generic title table.
        pyglet.text.Label(
            'Screen Testing Application', x=width//2, y=height-150,
            font_size=64, anchor_x='center', anchor_y='center',
            font_name='Sans', color=(0, 0, 0, 255), batch=batch)

        # An info label that shows the last pressed pos.
        pad = 50
        self.pressed_label = pyglet.text.Label(
            self._make_pressed_text(), x=width//2, y=height//2+pad,
            font_size=54, anchor_x='center', anchor_y='center',
            font_name='monospace', color=(0, 0, 0, 255), batch=batch)
        self.dragged_label = pyglet.text.Label(
            self._make_dragged_text(), x=width//2, y=height//2-pad,
            font_size=54, anchor_x='center', anchor_y='center',
            font_name='monospace', color=(0, 0, 0, 255), batch=batch)
        self.released_label = pyglet.text.Label(
            self._make_dragged_text(), x=width//2, y=height//2-3*pad,
            font_size=54, anchor_x='center', anchor_y='center',
            font_name='monospace', color=(0, 0, 0, 255), batch=batch)

        self.graphics = graphics

    def _make_pressed_text(self):
        """Construct a text for a press event."""
        return make_mouse_info_text(self.last_pressed_pos, 'pressed')

    def _make_dragged_text(self):
        """Construct a text for a drag event."""
        return make_mouse_info_text(self.last_dragged_pos, 'dragged')

    def _make_released_text(self):
        """Construct a text for a release event."""
        return make_mouse_info_text(self.last_released_pos, 'released')

    # ROS methods.

    def _init_ros(self):
        # Initialize the publishers.
        # Mouse events.
        self.mouse_motion_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~/mouse_motion', 10)
        self.mouse_press_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~/mouse_press', 10)
        self.mouse_drag_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~/mouse_drag', 10)
        self.mouse_release_pub = self.node.create_publisher(
            screen_app.msg.Mouse, '~/mouse_release', 10)
        # Keyboard events.
        self.key_press_pub = self.node.create_publisher(
            screen_app.msg.Key, '~/key_press', 10)
        self.key_release_pub = self.node.create_publisher(
            screen_app.msg.Key, '~/key_release', 10)

        # Initialise messages.
        self.mouse_message = screen_app.msg.Mouse()
        self.key_message = screen_app.msg.Key()

    def _make_mouse_message(self, x, y, buttons=mouse.LEFT, dx=0, dy=0):
        self.mouse_message.header.frame_id = self.name
        self.mouse_message.header.stamp = self.node.get_clock().now().to_msg()
        self.mouse_message.x = x
        self.mouse_message.y = y
        self.mouse_message.dx = dx
        self.mouse_message.dy = dy
        self.mouse_message.left = bool(buttons & mouse.LEFT)
        self.mouse_message.right = bool(buttons & mouse.RIGHT)

    def _make_key_message(self, symbol, modifiers):
        self.key_message.header.frame_id = self.name
        self.key_message.header.stamp = self.node.get_clock().now().to_msg()
        self.key_message.symbol = str(symbol)
        self.key_message.modifiers = str(modifiers)

    def _publish_mouse_motion(self, x, y, dx, dy):
        self._make_mouse_message(x, y, dx=dx, dy=dy)
        self.mouse_motion_pub.publish(self.mouse_message)

    def _publish_mouse_press(self, x, y, button):
        self._make_mouse_message(x, y, button)
        self.mouse_press_pub.publish(self.mouse_message)

    def _publish_mouse_drag(self, x, y, buttons, dx, dy):
        self._make_mouse_message(x, y, buttons, dx=dx, dy=dy)
        self.mouse_drag_pub.publish(self.mouse_message)

    def _publish_mouse_release(self, x, y, button):
        self._make_mouse_message(x, y, button)
        self.mouse_release_pub.publish(self.mouse_message)

    def _publish_key_press(self, symbol, modifiers):
        self._make_key_message(symbol, modifiers)
        self.key_press_pub.publish(self.key_message)

    def _publish_key_release(self, symbol, modifiers):
        self._make_key_message(symbol, modifiers)
        self.key_release_pub.publish(self.key_message)


def make_mouse_info_text(pos, action_text):
    """Construct the text to inform about a mouse position change event."""
    if pos is None:
        s = 'Not {} yet.'.format(action_text)
    else:
        s = 'Last {} x: {:4d}, y:{:4d}'.format(
            action_text, pos[0], pos[1])
    return s


def make_key_info_text(symbol, modifiers, action_text):
    """Construct the text to inform about a key event."""
    s = 'Key {} {}'.format(key.symbol_string(symbol), action_text)
    mod_s = key.modifiers_string(modifiers)
    if len(mod_s) > 0:
        s = s + ' with modifiers {}'.format(mod_s)
    return s


class Graphics(object):
    """A class to maintain collection of objects to draw & the window size."""

    def __init__(self, width=1920, height=1080, batch=None):
        self.width = width
        self.height = height

        if batch is None:
            self.batch = pyglet.graphics.Batch()
        else:
            self.batch = batch


def main(args=None):
    # Initialise the ROS node.
    rclpy.init(args=args)
    node = rclpy.create_node('screen_app')

    node.get_logger().info("Starting the node node...")

    # Initialise the human/app window.
    show_app(node)

    # No need to spin as pyglet has its event loop.
    # rclpy.spin(node)


if __name__ == '__main__':
    main()
