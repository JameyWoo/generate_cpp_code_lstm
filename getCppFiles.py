'''
获取并整合我自己写的cpp代码(考虑将每个cpp文件独立出来)
划分出代码列表, 以及全部的其他ascii字符
# ! 后期看结果可以考虑将所有的非ascii字符剃掉
'''
import os


def getCppData():
    cpp_dir = 'D:\MYS\My-C++'  # cpp文件的目录

    cnt, yes_cnt, data = 0, 0, []
    chars = set()

    for root, dirs, files in os.walk(cpp_dir, topdown=False):
        for name in files:
            if name[-4:] == '.cpp':
                file = os.path.join(root, name)
                cnt += 1
                try:
                    with open(file, 'rb') as file:
                        tmp = file.read()
                        str_tmp = str(tmp, encoding="gbk")
                        data.append(str_tmp)  # gbk能包含我的绝大多数的cpp文件编码
                        for i in str_tmp:
                            if not (i <= 'z' and i >= 'a' or (i <= 'Z' and i >= 'A') or 
                                (i <= '9' and i >= '0')) and ord(i) < 128:
                                chars.add(i)

                        yes_cnt += 1
                except:
                    pass
    return data, list(chars)


if __name__ == '__main__':
    data, chars = getCppData()
    print(data[1314])
    print(chars)
