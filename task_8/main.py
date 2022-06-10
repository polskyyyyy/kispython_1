def main(x):
    x = x.replace('do', '') \
        .replace('.do', '') \
        .replace('\n', ' ') \
        .replace('loc', '') \
        .replace('[', '') \
        .replace(']', '')
    x_parts = x.split('.end')
    x_parts_1 = [i.split('=:') for i in x_parts]
    x_parts_1.pop(-1)
    dick = {}
    # print(x_parts_1)
    for i in range(len(x_parts_1)):
        key = x_parts_1[i][1].replace(' ', '')
        value = x_parts_1[i][0].split(' . ')
        value.pop(0)
        for j in range(len(value)):
            value[j] = value[j].replace(' ', '')
        dick[key] = value
    return dick


main('''do .do loc[learin . tiri_70 . ceerer_155 . rain_932 ]=: onma_484 .end
.do loc [ tieron . telere_630 . teerri_262 . inxeus_780 ]=: biceti_414
.end .do loc [ enaraes_692 . ledi ]=:zaqure .end .do loc[ vequza_598 .
esorqu_686 . inties_701]=: tila .end end''')
