'''
获取并整合我自己写的cpp代码(考虑将每个cpp文件独立出来)
'''
import os

def getCppData():
    cpp_dir = 'D:\MYS\My-C++'  # cpp文件的目录

    cnt, yes_cnt, data = 0, 0, []

    for root, dirs, files in os.walk(cpp_dir, topdown=False):
        for name in files:
            if name[-4:] == '.cpp':
                file = os.path.join(root, name)
                cnt += 1
                try:
                    with open(file, 'rb') as file:
                        tmp = file.read()
                        data.append(str(tmp, encoding = "gbk"))  # gbk能包含我的绝大多数的cpp文件编码
                        yes_cnt += 1
                except:
                    pass
    return data


if __name__ == '__main__':
    data = getCppData()
    print(data[234])