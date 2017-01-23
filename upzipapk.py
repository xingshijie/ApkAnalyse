import queue
import subprocess
import os
import threading

q = queue.Queue()
apk_json_dir = os.curdir + os.path.sep + 'apk'
for f in os.listdir(apk_json_dir):
    path = os.path.abspath(apk_json_dir + '/' + f)
    if os.path.isdir(path) and not os.path.exists(path + '/classes.dex'):
        q.put(path)


def apk_to_class():
    while True:
        apk_path = q.get()
        re_count = 0
        while True:
            try:
                print("start unzip:" + apk_path)
                subprocess.call(['/Users/shijie.xing/AndroidStudioProjects/dexReader/apk2class.sh', apk_path])
            except Exception as e:
                print(e)
                re_count += 1
                if re_count > 4:
                    print("unzip fail:" + apk_path)
                continue
            else:
                print("unzip success:" + apk_path)
                break
        q.task_done()


for i in range(5):
    a = 'test'
    t = threading.Thread(target=apk_to_class)
    t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
    t.start()

q.join()
