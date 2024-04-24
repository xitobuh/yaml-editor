from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QAction
from editor import YamlEditor
from utils import load_yaml

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YAML Editor")
        self.editor = None
        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("File")

        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.open_file)
        file_menu.addAction(self.open_action)

        file_menu.addSeparator()

        self.save_action = QAction("Save", self)
        self.save_action.triggered.connect(self.save_file)
        file_menu.addAction(self.save_action)

        self.save_as_action = QAction("Save As", self)
        self.save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(self.save_as_action)

        file_menu.addSeparator()

        self.exit_action = QAction("Exit", self)
        self.exit_action.triggered.connect(self.close)
        file_menu.addAction(self.exit_action)

    def open_file(self):
        schema_path, _ = QFileDialog.getOpenFileName(self, "Open Schema File", "", "YAML Files (*.yaml *.yml)")
        if not schema_path:
            return

        schema = load_yaml(schema_path)

        yaml_path, _ = QFileDialog.getOpenFileName(self, "Open YAML File", "", "YAML Files (*.yaml *.yml)")
        if not yaml_path:
            return

        data = load_yaml(yaml_path)

        self.editor = YamlEditor(data, schema)
        self.setCentralWidget(self.editor)

    def save_file(self):
        if self.editor:
            self.editor.save_yaml()

    def save_as_file(self):
        if self.editor:
            self.editor.save_as_yaml()
