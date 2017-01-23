import json


class PackageData:

    def __init__(self, name="", package_name="", lib_list=[]):
        self.name = name
        self.package_name = package_name
        self.lib_list = lib_list


class MyEncode(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def as_payload(dct):
    return PackageData(dct['name'], dct['package_name'], dct['lib_list'])
