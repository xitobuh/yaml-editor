import yaml
from PySide6.QtWidgets import (
    QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QScrollArea, QMessageBox, QFileDialog, QHBoxLayout
)
from PySide6.QtCore import Qt

class YamlEditor(QWidget):
    def __init__(self, data, schema):
        super().__init__()
        self.data = data
        self.schema = schema
        self.widgets_mapping = {}
        self.init_ui()

    def init_ui(self, parent_key=None, indent=0):
        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        for key, value in self.schema.items():
            horizontal_box = QHBoxLayout()

            indent_label = QLabel(' ' * (indent * 2) + key)
            horizontal_box.addWidget(indent_label)

            full_key = f"{parent_key}.{key}" if parent_key else key

            widget = self.create_widget_for_value(value, full_key)
            horizontal_box.addWidget(widget)
            horizontal_box.setStretch(1, 1)

            scroll_layout.addLayout(horizontal_box)
            self.widgets_mapping[full_key] = widget

        scroll_area.setWidget(scroll_widget)
        layout.addWidget(scroll_area)

        if indent == 0:
            save_button = QPushButton('Save')
            save_button.clicked.connect(self.save_yaml)
            layout.addWidget(save_button)

            save_as_button = QPushButton('Save As')
            save_as_button.clicked.connect(self.save_as_yaml)
            layout.addWidget(save_as_button)

        self.setLayout(layout)

    def create_widget_for_value(self, value, full_key):
        widget = QLineEdit()
        widget.setText(str(self.data.get(full_key, '')))
        widget.editingFinished.connect(lambda w=widget, k=full_key: self.validate_input(w, k))
        return widget

    def validate_input(self, widget, full_key):
        current_text = widget.text()
        expected_type = self.schema.get(full_key)

        try:
            if expected_type:
                self.update_data_from_text(current_text, full_key)
                widget.setStyleSheet('')
                widget.setToolTip('')
        except Exception as e:
            widget.setStyleSheet('background-color: rgba(255, 0, 0, 0.2);')
            error_message = f"Validation error for '{full_key}': {e}"
            widget.setToolTip(error_message)
            print(e)

    def update_data_from_text(self, text, full_key):
        """Update self.data based on the text input."""
        yaml_data = yaml.safe_load(text)
        if yaml_data is not None:
            keys = full_key.split('.')
            current_data = self.data
            for key in keys[:-1]:
                if not isinstance(key, str):
                    key = str(key)
                current_data = current_data.setdefault(key, {})
            
            last_key = keys[-1]
            if not isinstance(last_key, str):
                last_key = str(last_key)

            current_data[last_key] = yaml_data

    def save_yaml(self):
        yaml_str = yaml.dump(self.data)
        with open('output.yaml', 'w') as f:
            f.write(yaml_str)

    def save_as_yaml(self):
        file_path, _ = QFileDialog.getSaveFileName(None, "Save YAML File As", "", "YAML Files (*.yaml *.yml)")
        if file_path:
            yaml_str = yaml.dump(self.data)
            with open(file_path, 'w') as f:
                f.write(yaml_str)
