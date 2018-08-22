# 写入到一个文件中
def add_desc(path, file_list):
    file_str = ','.join(file_list)
    with open(path + '/desc.log', 'w') as desc:
        desc.write(file_str)


file_name = '/Users/icearl/data/test/file_dic'

add_desc(file_name, ['file_1.py', 'file_2.py'])


# 读取文件并比较缓存是不是全的
import os
def check_cache(path):
    exist_file_list = os.listdir(path)
    try:
        with open(path + '/desc.log', 'r') as desc:
            line = desc.readline()
            needed_file_list = line.split(',')
    except IOError:
        needed_file_list = []
    for i in needed_file_list:
        if i in exist_file_list:
            continue
        else:
            return False
    return True

path = '/Users/icearl/data/test/file_dic'

print(check_cache(path))