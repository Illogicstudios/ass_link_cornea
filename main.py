import importlib
from common import utils

utils.unload_packages(silent=True, package="ass_link_cornea")
importlib.import_module("ass_link_cornea")
from ass_link_cornea import ass_link_cornea
ass_link_cornea.run()
