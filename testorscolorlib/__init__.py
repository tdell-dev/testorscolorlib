import argparse
import json
import os


class TestorsColorLib(object):

    def __init__(self, filename):
        if filename is None:
            raise RuntimeError("Filename not set")
        elif not os.path.isfile(filename):
            print("Filename does not exist. Generating new dict.")
            self.filename = filename
            self.base_db = {}
            self.base_db['colors'] = []

        else:
            self.filename = filename
            with open(self.filename, 'r') as rfile:
                self.base_db = json.load(rfile)

    def __str__(self):
        return str(self.base_db)

    def write_file(self):
        with open(self.filename, 'w') as wfile:
            json.dump(self.base_db, wfile)


    def add_entry(self, color_name, testors_code, size_in_oz, hex_val, ctype):
        for color_entry in self.base_db['colors']:
            if testors_code == color_entry['tcode']:
                print("Found another entry for this color code. Incrementing num entries")
                color_entry['num_entries'] +=1
            else:
                temp_dict = {}
                temp_dict['name'] = name_val
                temp_dict['size'] = size_in_oz
                temp_dict['hex'] = hex_val
                temp_dict['tcode'] = testors_code
                temp_dict['num_entries'] = 1
                self.base_db['colors'].append(temp_dict)


    def modify_entry(self, unique_attr_name, unique_attr_val, attribute, value):
        found = 0
        for entry in self.base_db['colors']:
            if entry[str(unique_attr_name)] == unique_attr_val:
                entry[str(attribute)] = value
                found = 1
        if found == 0:
            print("No entry was found with the given unique identifier pair {}, {}".format(unique_attr_name, unique_attr_val))
