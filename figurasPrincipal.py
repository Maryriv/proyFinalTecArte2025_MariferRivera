
import pandas as pd
from funciones import triangulo, rectangulo, circulo
dataFile = pd.read_csv("figuras.csv", sep='\s+', engine='python')

print("Procesando Figuras ...\n")

areas = []

for index, row in dataFile.iterrows():
    figura = row['FIGURA']
    medida1 = row['MEDIDA1']
    medida2 = row['MEDIDA2']
    
    print(f"Fila {index}: FIGURA={figura}, Medida1={medida1}, Medida2={medida2}")
    
    if figura == 'c':  # Círculo
        area = circulo(medida1)
    elif figura == 't':  # Triángulo
        area = triangulo(medida1, medida2)
    elif figura == 'r':  # Rectángulo
        area = rectangulo(medida1, medida2)
    else:
        print(f"  Figura desconocida: {figura}")
        continue
    
    areas.append(area)
    print(f"  Área: {area:.2f}\n")

print("=" * 50)
print(f"Total de figuras procesadas: {len(areas)}")
print(f"Área total: {sum(areas):.2f}")
