import platform

def pcinfo():
    info = platform.uname()
    os = info[0]
    distro = info[1]
    bits = 32
    if '64' in info[-1]:
        bits = 64
    return print(f'Operating system: {os}\nDistibution: {distro}\nBits: {bits}')

pcinfo()

