from splitCppData import splitData
import torch
from torch.utils.data import TensorDataset, DataLoader
import numpy as np


def batch_data_onefile(one_text, sequence_length):
    words = np.array(one_text)
    words_x, words_y = [], []
    for i in range(0, len(words) - sequence_length):
        words_x.append(words[i: i + sequence_length])
        words_y.append(words[i + sequence_length])
    words_x, words_y = np.array(words_x), np.array(words_y)
    # print(words_x, words_y)
    return words_x, words_y


def batch_data(int_text, sequence_length, batch_size-128):
    words_x, words_y = [], []
    for each in int_text:
        wx, wy = batch_data_onefile(each, sequence_length)
        words_x.extend(wx)
        words_y.extend(wy)

    words_x, words_y = np.array(words_x), np.array(words_y)
    print(len(words_x))
    print(len(words_y))
    train_data = TensorDataset(torch.from_numpy(
        words_x), torch.from_numpy(words_y))  # 把y也放进去
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)

    return train_loader


def getTrainLoader():
    char2int, int2char, int_text = splitData()
    train_loader = batch_data(int_text, 10, 128)
    return train_loader


if __name__ == '__main__':
    train_loader = getTrainLoader()
    iter = next(iter(train_loader))
    print(iter)
    print(iter[0].shape, iter[1].shape)