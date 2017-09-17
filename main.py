import cntk
from mnistdata.mnist_downloader import MnistDownloader
from mnistdata.ctf_reader import init_reader
from settings import MINST_DOWNLOAD_INFO


if __name__ == '__main__':
    if (cntk.__version__ != '2.1'):
        raise Exception('Invalid CNTK Version')
    all_devices = cntk.device.all_devices()
    if all_devices[0].type() == cntk.device.DeviceKind.GPU:
        print('You can use the GPU of your computer!!!')
        cntk.device.try_set_default_device(cntk.device.gpu(0))
    else:
        print('Sorry, your computer only has a slow CPU')
        cntk.device.try_set_default_device(cntk.device.cpu())

    input_dim = 784
    num_output_classes = 10

    mnist_downloader = MnistDownloader(MINST_DOWNLOAD_INFO)
    mnist_downloader.download_and_save_data()

    # Create the reader to training data set
    reader_train = init_reader(
        mnist_downloader.train_file, input_dim, num_output_classes)
