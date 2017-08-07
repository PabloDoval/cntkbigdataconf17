# Workshop CNTK DotnetMalaga 2017

## Configuración inicial

1. Instala primero la versión de Anaconda para tu sistema operativo

    * Descargar [aquí](https://repo.continuum.io/archive/Anaconda3-4.1.1-Windows-x86_64.exe) para Windows.

    * Descargar [aquí](https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh) para Linux.

    * Actualmente CNTK no tiene soporte para MacOs, habría que montar un Docker.

2. Ejecuta el script dentro de scripts
    * environment.bat (si estás en windows)
    * . ./environment.sh (si estás en Linux)

3. Selecciona el nombre que quieres para el entorno virtual (una vez acabe el script tendrás activo el entorno).

4. Ejecuta python main.py para comprobar que cntk se ha instalado correctamente. Dicho programa nos mostrará la version de cntk y las cpu's y gpu's disponibles en nuestra máquina.
