""" Initialize the PYTHONPATH properly to pick up the libs """

import os
import sys

this_dir = os.path.abspath(os.path.dirname(__file__))
src_dir = os.path.join(this_dir, os.pardir, "src")
sys.path.append(this_dir)
sys.path.append(src_dir)
