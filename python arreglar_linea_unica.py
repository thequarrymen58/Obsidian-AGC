import os
import re

CONTENT_DIR = r"./content"

def corregir_formulas_linea(texto):
    # 1. Normalizar saltos de línea de Windows (\r\n a \n)
    texto = texto.replace('\r\n', '\n')
    
    # 2. Función para desglosar la fórmula en 3 líneas independientes
    def reformatear(match):
        contenido = match.group(1).strip()
        if contenido:
            return f"$$\n{contenido}\n$$"
        return match.group(0)

    # 3. Detectar $$ fórmula $$ que estén en una sola línea
    texto = re.sub(r'\$\$([^\n\r]+?)\$\$', reformatear, texto)
    return texto

def procesar_vault():
    archivos_modificados = 0
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    contenido_original = f.read()
                
                contenido_nuevo = corregir_formulas_linea(contenido_original)
                
                if contenido_nuevo != contenido_original:
                    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
                        f.write(contenido_nuevo)
                    archivos_modificados += 1
                    print(f"Corregido: {file}")
                    
    print(f"\n¡Proceso terminado! Se actualizaron {archivos_modificados} archivos.")

if __name__ == "__main__":
    procesar_vault()