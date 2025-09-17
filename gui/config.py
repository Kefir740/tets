from pathlib import Path


config = {
    "window_width": '900',
    "window_height": '600',
    "project_folder":  Path(__file__).resolve().parent.parent,
    "fullscreen": False,
}

config["kv_files_folder"] = config["project_folder"] / "gui/screens/kv_files"
