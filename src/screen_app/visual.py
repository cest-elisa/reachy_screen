import pyglet
from pyglet.window import mouse, key

import rospy

import screen_app.msg


def show_app():
    """TODO"""
    AppWindow()

    # Enter main event loop.
    pyglet.app.run()


class AppWindow(pyglet.window.Window):
    def __init__(self, width=1920, height=1080, screen_index=-1):
        self._init_graphics(width, height)

        # Set a variable to check if the SHIFT key is pressed.
        self._is_shift = False
        self._is_alt = False
        self._is_a = False

        self.name = 'App'

        self._init_ros()
        rospy.on_shutdown(self.on_close)

        # Initialising pyglet window.
        rospy.loginfo('Creating the window')
        style = pyglet.window.Window.WINDOW_STYLE_BORDERLESS
        super().__init__(width, height, self.name, style=style)

        display = pyglet.canvas.get_display()
        screens = display.get_screens()
        active_screen = screens[screen_index]
        self.set_location(active_screen.x, active_screen.y)

        rospy.loginfo('Ready!')

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

        # Execute other things.
        if symbol == key.ESCAPE: # and modifiers & key.MOD_CTRL:
            rospy.signal_shutdown('App window is closed by ESCAPE.')

  
    def on_key_release(self, symbol, modifiers):
        self.publish_key_release(symbol, modifiers)
        if symbol == key.LSHIFT or symbol == key.RSHIFT:
            self._is_shift = False
        if symbol == key.LALT or symbol == key.RALT:
            self._is_alt = False
        if symbol == key.A:
            self._is_a = False

    def on_text(self, text):
        self.cur_scene.on_text(text)

    def on_text_motion(self, motion):
        self.cur_scene.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        self.cur_scene.on_text_motion_select(motion)

    def on_close(self):
        rospy.loginfo("Closing application window.")
        self.close()

    # Custom public methods.

    def on_context_lost(self, **kwargs):
        rospy.logerr('context lost')

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
        self.mouse_press_pub = rospy.Publisher(
            '~mouse_press', screen_app.msg.Mouse, queue_size=10)

        self.mouse_drag_pub = rospy.Publisher(
            '~mouse_drag', screen_app.msg.Mouse, queue_size=10)

        self.mouse_release_pub = rospy.Publisher(
            '~mouse_release', screen_app.msg.Mouse, queue_size=10)

        self.mouse_motion_pub = rospy.Publisher(
            '~mouse_motion', screen_app.msg.Mouse, queue_size=10)
        self.key_press_pub = rospy.Publisher(
            '~key_press', screen_app.msg.Key, queue_size=10)

        self.key_release_pub = rospy.Publisher(
            '~key_release', screen_app.msg.Key, queue_size=10)

        # Initialise messages.
        self.mouse_message = screen_app.msg.Mouse()
        self.key_message = screen_app.msg.Key()

    def make_mouse_message(self, x, y, buttons=mouse.LEFT, dx=0, dy=0):
        self.mouse_message.header.frame_id = self.name
        self.mouse_message.header.stamp = rospy.Time.now()
        self.mouse_message.header.seq += 1
        self.mouse_message.x = x
        self.mouse_message.y = y
        self.mouse_message.dx = dx
        self.mouse_message.dy = dy
        self.mouse_message.left = bool(buttons & mouse.LEFT)
        self.mouse_message.right = bool(buttons & mouse.RIGHT)

    def make_key_message(self, symbol, modifiers):
        self.key_message.header.frame_id = self.name
        self.key_message.header.stamp = rospy.Time.now()
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