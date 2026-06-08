- Extractor de Metadatos (OSINT) - Red Team

Este script es una herramienta de Inteligencia de Fuentes Abiertas (OSINT) desarrollada en Python.
Permite extraer información oculta (metadatos) de imágenes (.jpg, .jpeg, .png, .webp) y documentos (.pdf), incluyendo coordenadas GPS, fechas de creación, dispositivo y autores.

- Requisitos Previos
Para ejecutar esta herramienta, necesitas tener instalado Python 3.x.X en tu sistema y tambien las siguientes librerías:
pip install Pillow
pip install pypdf

- Instalación y Uso:
Descarga el script o el rar en tu máquina.
Extrae el contenido o abre una termianl, cmd o powershell, y navega hasta la carpeta del proyecto.
Ejecuta el script usando la sintaxis correcta y el nombre *COMPLETO* del archivo que deseas analizar.

Sintaxis:
python extractor_osint.py (nombre_del_archivo)

Ejemplos de ejecución:
python extractor_osint.py vacaciones.jpg
python extractor_osint.py reporte_financiero.pdf
python extractor_osint.py IMG-20260XXXX-XX-XX.jpeg

(Se han agregado algunas imágenes y pdf para probar el uso del script)

Consideraciones de Seguridad
Esta es una herramienta de auditoría defensiva/ofensiva local.
Porfavor asegurarse de ejecutarla únicamente contra archivos propios o en entornos autorizados y controlados.
