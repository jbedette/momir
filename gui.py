from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import momir


class IntegerImageApp(App):
    def build(self):
        # Root layout
        root = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # Left-side layout for the integer, buttons, and submit button
        left_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.4, 1))
        self.integer_label = Label(text="1", font_size=40, halign="center", valign="middle")
        self.integer_label.bind(size=self.integer_label.setter('text_size'))
        
        increment_button = Button(text="Increment", size_hint=(1, 0.2), font_size=24)
        increment_button.bind(on_press=self.increment_integer)
        
        decrement_button = Button(text="Decrement", size_hint=(1, 0.2), font_size=24)
        decrement_button.bind(on_press=self.decrement_integer)

        submit_button = Button(text="Submit", size_hint=(1, 0.2), font_size=24)
        submit_button.bind(on_press=self.on_submit)

        # Add widgets to left layout
        left_layout.add_widget(self.integer_label)
        left_layout.add_widget(increment_button)
        left_layout.add_widget(decrement_button)
        left_layout.add_widget(submit_button)

        # Right-side layout for the image
        right_layout = BoxLayout(size_hint=(0.6, 1))
        self.image = Image(source="sample.jpg")  # Initial sample image
        right_layout.add_widget(self.image)

        # Add both layouts to the root layout
        root.add_widget(left_layout)
        root.add_widget(right_layout)

        return root

    def increment_integer(self, instance):
        current_value = int(self.integer_label.text)
        if current_value < 16:  # Limit to 16
            current_value += 1
            self.integer_label.text = str(current_value)

    def decrement_integer(self, instance):
        current_value = int(self.integer_label.text)
        if current_value > 1:  # Limit to 1
            current_value -= 1
            self.integer_label.text = str(current_value)

    def on_submit(self, instance):
        # Get the current integer as a string
        current_value = self.integer_label.text
        # Call the external function to get a new image path
        new_image_path = self.handle_submission(current_value)
        # Update the image on the right side
        self.image.source = new_image_path
        self.image.reload()  # Refresh the image widget

    def handle_submission(self, value):
        # Example function to handle submission and return an image path
        print(f"Submitted value: {value}")
        # Replace this logic with your custom logic to return the appropriate image
        # For this example, images are named '1.jpg', '2.jpg', etc.
        return momir.gui_momir(value)


if __name__ == "__main__":
    IntegerImageApp().run()
