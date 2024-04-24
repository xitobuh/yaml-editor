import yaml

def load_yaml(file_path):
    """Load YAML file and return its content as a Python dictionary."""
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {file_path} file not found.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing {file_path}: {e}")

def save_yaml(file_path, data):
    """Save YAML data to a file."""
    try:
        with open(file_path, 'w') as f:
            yaml.dump(data, f)
    except Exception as e:
        raise ValueError(f"Error saving data to {file_path}: {e}")
