print('{0:b}'.format(10))


def get_bin(x):
    res = format(abs(x), 'b')
    if x < 0:
        return '1' + res.zfill(11) if len(res) < 13 else None
    return res.zfill(12) if len(res) < 13 else None


print(get_bin(-10), get_bin(10), sep='\n')
