'''
分隔所有的原子单位, 并转化为以0开始的整数, 生成int_text
'''
from getCppFiles import getCppData
import os
from collections import Counter


def offlineData():
    cppData, chars = getCppData()
    test_text = cppData[0]
    newData = []
    cnt = 0

    for i in range(len(cppData)):
        new_one = ''
        for j in range(len(cppData[i])):
            # print(cppData[i][j], end='')
            if cppData[i][j] in chars and cppData[i][j] != ' ':
                new_one += ' ' + cppData[i][j] + ' '
            else:
                new_one += cppData[i][j]
        newData.append(new_one)
        with open('./assets/cppData' + str(cnt) + '.cd', 'w+', encoding='utf-8') as file:
            file.write(new_one)
        cnt += 1

    # print(newData[0])


def splitData():
    '''
    返回根据频率映射好的char2int, int2char
    '''
    files = os.listdir('./assets')
    cppData = []
    for each in files:
        with open('./assets/' + each, 'r', encoding='utf-8') as file:
            cppData.append(file.read().split())
    # print(cppData[0])
    chars = Counter()
    for each in cppData:
        for char in each:
            chars[char] += 1
    int2char, char2int = {}, {}
    cnt = 0
    count = 0
    for item in chars.most_common():
        char2int[item[0]] = count
        int2char[count] = item[0]
        count += 1
        # if item[1] == 9:
        #     print(item)
    # print(cnt)
    # print(len(chars.most_common()))
    # print(char2int)
    int_text = []
    for each in cppData:
        text = []
        for any in each:
            text.append(char2int[any])
        int_text.append(text)

    return char2int, int2char, int_text


if __name__ == '__main__':
    char2int, int2char, int_text = splitData()
    print(int_text[0])
