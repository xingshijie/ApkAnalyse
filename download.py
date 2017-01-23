import threading

import requests
import json
import os
from apkData import ApkData
import queue

f = open('apk_data_list.json', 'r')


def as_payload(dct):
    return ApkData(dct['app_name'], dct['download_url'], dct['package_name'])


apk_list = json.load(f, object_hook=as_payload)

q = queue.Queue()
for item in apk_list:
    q.put(item)


def download_apk():
    while True:
        download_apk_data = q.get()
        re_count = 0
        apk_filename = 'apk/' + download_apk_data.package_name + '.apk'
        if os.path.isfile(apk_filename):
            print("has download:" + apk_filename)
        else:
            while True:
                try:
                    print("start download:" + apk_filename)
                    re = requests.get(download_apk_data.download_url)
                    if re.status_code == 200:
                        with open('apk/' + download_apk_data.package_name + ".apk", 'wb') as fd:
                            for c in re.iter_content(1000):
                                fd.write(c)
                            print(fd.name)
                except Exception as e:
                    print(e)
                    re_count += 1
                    if re_count > 4:
                        print("download fail:" + apk_filename)
                    continue
                else:
                    print("download success:" + apk_filename)
                    break
        q.task_done()


for i in range(5):
    t = threading.Thread(target=download_apk)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()

q.join()
