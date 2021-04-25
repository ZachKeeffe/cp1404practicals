from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

BUTTON_LIST = ["Yes", "No", "Maybe", "Can't Say"]


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.button_list = BUTTON_LIST

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for entry in self.button_list:
            temp_label = Label(text=entry)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetsApp().run()
