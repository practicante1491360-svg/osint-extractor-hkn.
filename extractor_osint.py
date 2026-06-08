import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from pypdf import PdfReader

def convertiragrados(coordenadas, referencia):
    grados = float(coordenadas[0])
    minutos = float(coordenadas[1])
    segundos = float(coordenadas[2])
    
    decimal = grados + (minutos / 60) + (segundos / (60*60))
    if referencia in ['S', 'W']:
        decimal = -decimal
    return decimal

##############################MÓDULO IMAGEN
def meta_imagen(ruta_imagen):
    print(f"\n[*] Información de: {ruta_imagen}")
    try:
        imagen = Image.open(ruta_imagen)
        datos = imagen._getexif()

        if not datos:
            print("  [-] No se encontraron metadatos en esta imagen.")
            return

        fecha_creacion = "Desconocida"
        telefono = "Desconocida"
        ubicacion = {}

        for tag_id, valor in datos.items():
            nombre_tag = TAGS.get(tag_id, tag_id)
            if nombre_tag == "DateTimeOriginal":
                fecha_creacion = valor
            elif nombre_tag == "Model":
                telefono = valor
            elif nombre_tag == "GPSInfo":
                for gps_tag_id in valor:
                    nombre_gps_tag = GPSTAGS.get(gps_tag_id, gps_tag_id)
                    ubicacion[nombre_gps_tag] = valor[gps_tag_id]

        print(f"  [+] Fecha de creación: {fecha_creacion}")
        print(f"  [+] Modelo de celular: {telefono}")

        if ubicacion and "GPSLatitude" in ubicacion and "GPSLongitude" in ubicacion:
            latitud = convertiragrados(ubicacion["GPSLatitude"], ubicacion["GPSLatitudeRef"])
            longitud = convertiragrados(ubicacion["GPSLongitude"], ubicacion["GPSLongitudeRef"])
            print(f"  [+] ubicación: {latitud:.4f}, {longitud:.4f} (Ubicación encontrada)")
        else:
            print("  [-] ubicación: No encontrada.")

    except Exception as e:
        print(f"  [-] Error al analizar la imagen: {e}")

########################################MÓDULO PDF
def extraer_metadatos_pdf(ruta_pdf):
    print(f"\n[*] Iniciando análisis de PDF: {ruta_pdf}")
    try:
        reader = PdfReader(ruta_pdf)
        metadatos = reader.metadata
        
        if not metadatos:
            print("  [-] No se encontraron metadatos en este PDF.")
            return
            
        print(f"  [+] Autor: {metadatos.get('/Author', 'Desconocido')}")
        print(f"  [+] Programa: {metadatos.get('/Creator', 'Desconocido')}")
        print(f"  [+] Fecha de creación: {metadatos.get('/CreationDate', 'Desconocida')}")
        print(f"  [+] Software productor: {metadatos.get('/Producer', 'Desconocido')}")
        
    except Exception as e:
        print(f"  [-] Error analizando el PDF: {e}")

#########################################LOGICA
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso correcto: python extractor_osint.py <archivo de imagen o archivo.pdf>")
    else:
        archivo = sys.argv[1]
        
        ##################3VerificaCION del Archivo
        if not os.path.exists(archivo):
            print(f"[-] Error: El archivo '{archivo}' no existe en esta carpeta.")
            sys.exit(1)
            
        #####################minimizar la extención
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()
        
        if extension in ['.jpg', '.jpeg', '.png', '.webp']:
            meta_imagen(archivo)
        elif extension == '.pdf':
            extraer_metadatos_pdf(archivo)
        else:
            print(f"[-] Formato no soportado: {extension}")
            print("[!] Esta herramienta solo soporta archivos .jpg, .jpeg, .png, .webp o .pdf")