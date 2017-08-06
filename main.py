import cntk

if __name__ == '__main__':
    print(cntk.__version__)
    print(cntk.device.all_devices())
