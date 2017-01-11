
# Add a relative path
import sys, os
file_dir = os.path.dirname(os.path.realpath(__file__))
relative_path = "/.."
path = os.path.abspath(file_dir + relative_path)
sys.path.insert(0, path)
import time
import numpy as np
import logging
import copy
from data_mgmt.Wisps_data import Wisps_data
import data_mgmt.writer as writer
from netCDF4 import Dataset
from datetime import datetime 
from datetime import timedelta
from marine_to_nc.marinereader import marinereader
import metar_to_nc.qc_main as qc
import registry.util as cfg

def main():
    """
    Main function for converting marine CSV file to WISPS netCED file
    """
    # Read Control
    control = cfg.read_marine_control()
    in_dir = control['input_directory']
    in_file = control['input_filename']
    out_dir = control['output_directory']
    out_file = control['output_filename']
    start_date = control['start_date']
    end_date = control['end_date']

    in_path = in_dir + in_file
    out_path = out_dir + out_file + '.nc'

    # Read Configuration
    marine_convert = cfg.read_marine_lookup()
    nc_vars = cfg.read_nc_variables()

    # Read file
    print "Reading marine file"
    reader = marinereader(in_path)
    if start_date:
        reader.read(start_date=start_date, end_date=end_date)
    reader.read(end_date=end_date)

    # Stack the stations to make 3d array
    multi_d = []
    for name, observations in reader.station_list.iteritems():
        reader.station_list[name] = np.array(observations)
        multi_d = multi_d + [reader.station_list[name]] 
   
    # Package data into Wisps_data object. Write data
    observations = reader.observations
    multi_d = np.array(multi_d)
    station_names = reader.station_list.keys()
    obj_list = []
    for i,observation_name in enumerate(observations):
        ob_arr = multi_d[:,:,i] 
        std_name = marine_convert[observation_name]
        try:
            std_var = nc_vars[std_name]
            ob_arr = ob_arr.astype(std_var['data_type'])
            obj = Wisps_data(std_name)
            obj.set_dimensions(tuple(std_var['dimensions']))
            obj.add_data(ob_arr)
            obj_list.append(obj)
        except KeyError:
            print observation_name, "undefined"

    writer.write(obj_list, out_path)



