import json


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


print(json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex))
