# =====================================================================
# Universidad Nacional Abierta y a Distancia (UNAD)
# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA
# 
# Problema Seleccionado: Problema 4 (Videoteca Digital)
# Enfoque: Estructurado / Modular
# =====================================================================

# R1: DATOS INICIALES - Almacenamiento en matriz (Mínimo 7 registros)
videoteca = [
    ["Inception", 2010, 8.8, "Ciencia Ficción"],
    ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
    ["Parasite", 2019, 8.6, "Drama"],
    ["Dune: Part Two", 2024, 8.9, "Ciencia Ficción"],
    ["The Matrix", 1999, 8.7, "Ciencia Ficción"],
    ["Spider-Man: Into the Spider-Verse", 2018, 8.4, "Animación"],
    ["Oppenheimer", 2023, 8.5, "Biografía"]
]


# R3 y R4: MÓDULO - Función para evaluar y contar según la lógica de negocio
def contar_tulos_destacados(matriz_videos, umbral_calificacion, anio_limite):
    """
    Recorre la matriz de películas y cuenta cuántos títulos cumplen 
    simultáneamente con el umbral de calificación y el año límite establecido.
    """
    conteo_coincidencias = 0
    
    # Ciclo estructurado para recorrer cada fila (película) de la matriz
    for pelicula in matriz_videos:
        # Extracción indexada de los campos requeridos
        anio_lanzamiento = pelicula[1]
        calificacion = pelicula[2]
        
        # Lógica de Negocio: Operador lógico Y (and) para evaluar ambas condiciones
        if calificacion >= umbral_calificacion and anio_lanzamiento >= anio_limite:
            conteo_coincidencias += 1  # Incremento del acumulador
            
    return conteo_coincidencias


# R2 y R5: FUNCIÓN PRINCIPAL / CONTROLADOR DE INTERFAZ
def main():
    print("=================================================")
    print("      AUDITORÍA DE VIDEOTECA DIGITAL (UNAD)      ")
    print("=================================================")
    
    # R2: Captura y validación de entradas por teclado
    try:
        umbral_usuario = float(input("Ingrese el umbral de calificación mínima (ej. 8.5): "))
        anio_usuario = int(input("Ingrese el año límite de lanzamiento (ej. 2015): "))
        
        # Procesamiento: Llamada al módulo con los argumentos configurados
        total_cumple = contar_tulos_destacados(videoteca, umbral_usuario, anio_usuario)
        
        # R5: Salida del conteo final esperado
        print("\n-------------------------------------------------")
        print("               INFORME GENERADO                  ")
        print("-------------------------------------------------")
        print(f"Total de títulos populares y recientes encontrados: {total_cumple}")
        print(f"(Criterio: Calificación >= {umbral_usuario} e Inclusión >= {anio_usuario})")
        print("-------------------------------------------------")
        
    except ValueError:
        # Control preventivo de errores de digitación
        print("\n[Error de Entrada]: Asegúrese de ingresar valores numéricos válidos.")


# Inicio controlado de la ejecución estructurada
if __name__ == "__main__":
    main()