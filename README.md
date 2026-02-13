# Semana 1 — Limpieza básica y modularización (Pandas) — Cáncer de mama (PIII 2023)

## 1. Objetivo (Semana 1)
Este trabajo corresponde a la **Semana 1** del curso:  
- **Seleccionar un dataset personal**  
- Realizar **limpieza básica en Pandas**  
- **Modularizar la limpieza en funciones puras** en un archivo `.py` separado (no solo en celdas del notebook). :contentReference[oaicite:0]{index=0}  

## 2. Dataset
- **Nombre del archivo (raw):** `42.-cancer-de-mama-datos-abiertos-piii-2023.csv`
- **Tema:** registros/variables asociadas a cáncer de mama (PIII 2023)
- **Nota técnica del archivo:** el dataset está separado por `;` (no por `,`) y contiene separadores sobrantes al final, lo que puede crear columnas vacías (`Unnamed:*`) si no se limpia.

## 3. Estructura de archivos (Colab)
- `Semana1_CancerMama.ipynb` (notebook principal)
- `cleaning.py` (funciones puras de limpieza)
- `cancer_mama_piii_2023_clean.csv` (salida procesada)

## 4. Reproducibilidad en Google Colab
### 4.1. Lectura del dataset (I/O)
En Colab, el archivo raw se lee con:

```python
import pandas as pd
df_raw = pd.read_csv("/content/42.-cancer-de-mama-datos-abiertos-piii-2023.csv", sep=";", engine="python")
