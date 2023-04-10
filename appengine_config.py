# appengine_config.py
import pkg_resources
from google.appengine.ext import vendor

# Set path to your libraries folder.
path = 'lib'
# Add libraries installed in the path folder.
vendor.add(path)
# Add libraries to pkg_resources working set to find the distribution.
pkg_resources.working_set.add_entry(path)

# lib フォルダのフルパスを指定します
# import os
# path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')