import os

def get_script_path():
    return str(os.path.dirname(os.path.abspath(__file__)))

def get_parent_project_path():
    return str(os.path.dirname(get_script_path()))

def get_appdata_roaming_path():
    # windows software edition
    if os.name == 'nt':
        # C:\Users\<user>\AppData\Roaming
        # verificar si existe
        os.makedirs(os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "DaiQode"), exist_ok=True)
        return os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "DaiQode")

    # linux software edition
    elif os.name == 'posix':
        # ~/.config/DaiQode
        os.makedirs(os.path.join(os.path.expanduser("~"), ".config", "DaiQode"), exist_ok=True)
        return os.path.join(os.path.expanduser("~"), ".config", "DaiQode")