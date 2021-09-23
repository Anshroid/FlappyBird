import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Flappy Bird",
        version = "1.0",
        description = "A Python Flappy Bird Clone, with open variable access",
        options = {"build_exe": {"packages": ["os", "random"],
                                 "include_files": ["bird.py",
                                                   "pipe.py",
                                                   "scorebox.py",
                                                   "bird.png",
                                                   "background.jpg",
                                                   "pipe.png",
                                                   "icon.png",
                                                   "icon.ico",
                                                   "flappybird.otf"]},
                   "bdist_msi": {"target_name": "FlappyBird",
                                 "install_icon": "icon.ico",
                                 "add_to_path": True}},
        executables = [Executable("main.py", base=base, targetName="FlappyBird", icon="icon.ico")])
