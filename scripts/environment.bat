@echo off
set /p envname="¿Cual es el nombre de tu entorno virtual?"
call conda-env create -n %envname% --file ../anaconda_env.yml
if %errorlevel% neq 0 ( 
    echo "Hubo un error creando el entorno virtual" 
    exit /b %ERRORLEVEL%
    )
activate %envname%
