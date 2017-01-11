from abc import ABCMeta, abstractmethod
from netCDF4 import Dataset

"""
Interface enforcing a method to produce a netcdf variable object
"""
class nc_writable(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_nc_variable(self, nc_handle):
        """
        Abstract method to write a netCDF Variable to the nc_handle
        """
        pass