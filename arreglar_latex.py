import os
import re

CONTENT_DIR = r"./content"

def corregir_bloques_math(texto):
    # Separar $$ iniciales si están pegados al código
    texto = re.sub(r'\$\$\s*(\\begin)', r'$$\n\1', texto)
    # Separar $$ finales si están pegados al cierre
    texto = re.sub(r'(\\end\{[^\}]+\}|\tag\{[^\}]+\})\s*\$\$', r'\1\n$$', texto)
    return texto

def procesar_vault():
    archivos_modificados = 0
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido_original = f.read()
                
                contenido_nuevo = corregir_bloques_math(contenido_original)
                
                if contenido_nuevo != contenido_original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(contenido_nuevo)
                    archivos_modificados += 1
                    print(f"Corregido: {file}")
                    
    print(f"\n¡Listo! Se separaron los delimitadores $$ en {archivos_modificados} archivos.")

if __name__ == "__main__":
    procesar_vault()