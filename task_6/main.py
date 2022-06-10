def main(x):
    dict1 = {'VHDL': 0, 'CUDA': 1, 'NSIS': 2}
    dict11 = {'VHDL': 3, 'CUDA': 4, 'NSIS': 5}
    dict2 = {2017: 6, 1972: 7}
    dict3 = {'TEA': dict1[x[1]], 'TEX': dict11[x[1]]}
    dict111 = {'VHDL': dict2[x[2]], 'CUDA': 8, 'NSIS': 9}
    dict0 = {1957: dict3[x[3]], 1975: dict111[x[1]], 1964: 10}
    return dict0[x[0]]
