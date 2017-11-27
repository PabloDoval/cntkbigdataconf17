# Workshop CNTK - Big Data Conference 2017 Lithuania

## Initial Setup

1. First of all, please do install Anaconda in your machine

    * Windows version [here](https://repo.continuum.io/archive/Anaconda3-4.1.1-Windows-x86_64.exe).

    * Linux version [here](https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh).

    * Unfortunately, CNTK does not natively support MacOs yet, so a Docker solution would be needed if you want to work on MacOs.

2. Go to the .\Scripts folder and run the script that will perform the environment setup:
    * environment.bat (if you are running Windows)
    * . ./environment.sh (for you, Linux folks)

3. Once the script finishes running, that environment will be active. The name of the environment is *cntk23-bigdataconflithuania*, in case you want to activate it manually.

4. Run the *main.py* to check that the CNTK environment and dependencies have been propertly setup. The output will show the version of the CNTK distribution, as well as the number of CPUs and GPUs available in our machine.

## Mnist Handwritten Digits Database

The initial exercises of this workshop will use the MNIST Handwritten Digits database; this publicly available dataset has become a sort of *de facto* industry standard to test the performance of certain image classification algorithms. Even though a detailed description of this data set is not intended here (more information [here](https://en.wikipedia.org/wiki/MNIST_database)), suffice to say that each image represents a handwrittend digit, from 0 to 9, as an array of 9x9 pixels.

![MNIST image sample](https://www.researchgate.net/profile/Amaury_Lendasse/publication/264273647/figure/fig1/AS:295970354024489@1447576239974/Fig-18-0-9-Sample-digits-of-MNIST-handwritten-digit-database.png)


The folder *./mnistdata* contains both the script to download the data set, as well as the classes tasked with reading and writing the images. The *mnist_downloader.py* file will download the images into the directory specified in the *settings.py* file. Then, both the training and test datasets will be serialized individually into two files in CTF format.

These files will then be easily read by CNTK using the built-in CTF deserializer.

## Authors

    Pablo Álvarez Doval - @PabloDoval
    Rodrigo Cabello - @mrcabellom
