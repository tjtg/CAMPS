#!/usr/bin/env python
import os
import sys
file_dir = os.path.dirname(os.path.realpath(__file__))
relative_path = '/..'
path = os.path.abspath(file_dir + relative_path)
sys.path.insert(0, path)
import wet_bulb


def test_wet_bulb_setup():
    """  """
    pass

def test_wet_bulb():
    """  """
    pass



if __name__ == "__main__":

    test_wet_bulb_setup()
    test_wet_bulb()