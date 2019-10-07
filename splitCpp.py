'''
分隔所有的原子单位, 并转化为以0开始的整数
'''

text = '''
#include <iostream>
using namespace std;

int main() {
    int a[3] = {1, 2, 3};
    for (auto &i: a) {
        i = 3;
    }
    for (auto i: a) {
        cout << i << endl;
    }
}
'''

