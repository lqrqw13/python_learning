import os
from multiprocessing import Manager, Pool

#多进程拷贝文件
#Pool如果需要使用Queue，必须先导入Manager，然后实例化Manager,即Manager().Queue()



#读取文件内容，再写入内容
def copy_files(name, folder_name, new_folder_name, queue):
    
    with open(folder_name+ '/'+name, 'rb') as f:
        fr = f.read()
    with open(new_folder_name+'/'+ name, 'wb') as f:
        fw = f.write(fr)
    queue.put(name)


def main():
    #输入需要复制的文件夹名
    folder_name = input('输入需要复制的文件夹名')
    new_folder_name = folder_name + "_复件"
    os.mkdir(new_folder_name)
    #拿到文件夹下的文件名
    file_names = os.listdir(folder_name)
    pool = Pool(5)
    queue = Manager.Queue()
    for name in file_names:
        pool.apply_async(copy_files, (name, folder_name, new_folder_name,queue,))

    all_num = len(file_names)
    num = 0
    while True:
        queue.get()
        num += 1
        progress = num/all_num*100
        print('\rcopy的进度是{:.2f}%'.format(progress), end = '')
        if num == all_num:
            break

if __name__ == '__main__':
    main()
