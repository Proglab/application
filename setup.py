from cx_Freeze import setup, Executable
import application
import os

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = []

application_file = "app.py"

setup(
    name="application",
    version=application.__version__,
    description="Une application",
    options={"build_exe": {
            'packages': ["os", "sys"],
            'excludes': [],
            'include_files': include_files,
            'include_msvcr': True,
        }
    },
    data_files=include_files,
    executables=[Executable(application_file, base="Win32GUI")]
)
