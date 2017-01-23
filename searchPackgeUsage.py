import os
import json
import packageData
import sys
import operator

apk_list = json.load(open('apk_package_list_4.json', 'r'), object_hook = packageData.as_payload)
result_apk_list = []
size_info_list = []
for apk_package_data in apk_list:
    for lib in apk_package_data.lib_list:
        if sys.argv[1] in lib:
            try:
                size = os.path.getsize('apk/' + apk_package_data.package_name + '/lib/armeabi/libandfix.so')
            except:
                try:
                    size = os.path.getsize('apk/' + apk_package_data.package_name + '/lib/armeabi-v7a/libandfix.so')
                except:
                    size = 0
            result_apk_list.append(apk_package_data)
            size_info_list.append(size)
            break
apk_size_map = dict(zip(result_apk_list, size_info_list))
apk_size_map = sorted(apk_size_map.items(), key=operator.itemgetter(1))
for a in apk_size_map:
    print(a[0].name + " : " + a[0].package_name + ' : ' + str(a[1]))