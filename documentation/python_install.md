# Python

Recomendadmos la versión 3.14.3t para la realización de las prácticas,
pero en todo caso debe ser la versión 3.8 o superior. Es importante que la
versión de python tenga la `t` para que podamos utilizar las caraterísticas de
hilos y concurrencia reales.

En el caso de la versión 3.14 la
[documentación oficial](https://www.python.org/downloads/windows/) recomienda la
instalación mediante la
[Windows store](https://apps.microsoft.com/detail/9nq7512cxl7t?ocid=webpdpshare)
de manera que primero instalamos la plataforma de python y luego las diferentes
versiones.

## Instalación mediante plataforma de Python

Una vez descargado el instalador de plataforma de python lo ejecutamos y
seguimos los pasos de instalación. Se abrirá una terminal donde se nos
preguntarán algunas opciones de configuración, responda que sí a todas.

<img src="./statics/python_install/python_install_init.png" width="600"/>

<img src="./statics/python_install/python_install_terminal.png" width="600"/>

Una vez finalizada la instalación, debemos instalar la versión concreta de
python que usaremos. Para esto abrimos la PowerShell de Windows y ejecutamos el
siguiente comando:

```powershell
py install 3.14.3t
```

<img src="./statics/python_install/python_install_terminal_free_threaded_version.png" width="600"/>

Esto descargará e instalará la versión de python 3.14.3t en nuestro sistema. A
partir de ahora podremo seleccionar en VScode la versión de python 3.14.3t para
ejecutar el código o crear el entorno virtual.

## Instalación directa

En ocasiones la instalción mediante la plataforma da problemas si ya existe una
versión de python instalada. En estos casos se puede realizar una instalación
directa de la versión adecuada. El instalador se puede descarga de la
[página oficial](https://www.python.org/downloads/windows/)

<img src="./statics/python_install/python_install_releases_windows.png" width="600"/>

Una vez descargado el instalador ejecutelo y asegúrese de marcar las siguientes
opciones:

- Add Python to PATH
- Use admin privileges when installing py.exe

<img src="./statics/python_install/python_install_direct_init.png" width="600"/>

A continuación seleccione `Customize installation` y seleccione las opciones que
se muestran en la imagen.

<img src="./statics/python_install/python_install_direct__optional_features.png" width="600"/>

En la siguiente pantalla es muy importante marcar la opción
`Download free-threaded binaries`. Tras esto la instalación finalizará.

<img src="./statics/python_install/python_install_direct_free_threaded_option_select.png" width="600"/>

Una vez instalado python puede verificar la instalción con el siguiente comando:

```shell
py -3.14t --version
```

## Versiones antiguas

En el caso de versiones inferiores puede seguir la siguiente guía:

El primer paso es descargar el instaladro de
[Python](https://www.python.org/downloads/) adecuado y ejecutar el archivo
descargado.

<img src="./statics/python_install/python_install_old_init.png" width="600"/>

Tras terminar la instalación, se le ofrece la opción de eliminar el tamaño
máximo de nombre de los archivos, no es necesario.

<img src="./statics/python_install/python_install_old_finish.png" width="600"/>
