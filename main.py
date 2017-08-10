import cntk

if __name__ == '__main__':
    print('CNTK version:',cntk.__version__)
    all_devices = cntk.device.all_devices()
    if all_devices[0].type() == cntk.device.DeviceKind.GPU:
        print('You can use the GPU of your computer!!!')
        cntk.device.try_set_default_device(cntk.device.gpu(0))
    else:
        print('Sorry, your computer only has a slow CPU')
        cntk.device.try_set_default_device(cntk.device.cpu())