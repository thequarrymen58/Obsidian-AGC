import os
import re

CONTENT_DIR = r"./content"

def corregir_entorno_align(texto):
    # Reemplazar \begin{align} por \begin{align*} (solo si no tiene ya el asterisco)
    texto = re.sub(r'\\begin\{align\}(?!\*)', r'\\begin{align*}', texto)
    texto = re.sub(r'\\end\{align\}(?!\*)', r'\\end{align*}', texto)
    
    # Reemplazar \begin{aligned} por \begin{align*} para estandarizar
    texto = re.sub(r'\\begin\{aligned\}', r'\\begin{align*}', texto)
    texto = re.sub(r'\\end\{aligned\}', r'\\end{align*}', texto)
    
    return texto

def procesar_vault():
    archivos_modificados = 0
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido_original = f.read()
                
                contenido_nuevo = corregir_entorno_align(contenido_original)
                
                if contenido_nuevo != contenido_original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(contenido_nuevo)
                    archivos_modificados += 1
                    print(f"Actualizado: {file}")
                    
    print(f"\n¡Listo! Se actualizaron los entornos en {archivos_modificados} archivos.")

if __name__ == "__main__":
    procesar_vault()