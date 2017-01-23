import json


class ApkData:

    def __init__(self, app_name = "", download_url = "", package_name = ""):
        self.app_name = app_name
        self.download_url = download_url
        self.package_name = package_name


def as_payload(dct):
    return ApkData(dct['app_name'], dct['download_url'], dct['package_name'])