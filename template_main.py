import sys
import importlib

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/ass_link_cornea'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    modules = [
        "ass_link_cornea",
        "cornea_by_char"
    ]

    from utils import *
    unload_packages(silent=True, packages=modules)

    for module in modules:
        importlib.import_module(module)

    from ass_link_cornea import *

    ass_link_cornea.run()