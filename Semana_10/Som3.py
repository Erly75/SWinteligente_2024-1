import numpy as np
import matplotlib.pyplot as plt

def minimoNodo(data, t, pesos, m_rows, m_cols):
  result = (0,0)
  distanciaMinima = 1.0e20
  for i in range(m_rows):
    for j in range(m_cols):
      ed = euc_dist(pesos[i][j], data[t])
      if ed < distanciaMinima:
        distanciaMinima = ed
        result = (i, j)
  return result

def euc_dist(v1, v2):
  return np.linalg.norm(v1 - v2) 

def manhattan_dist(r1, c1, r2, c2):
  return np.abs(r1-r2) + np.abs(c1-c2)

def most_common(lst, n):
  if len(lst) == 0: return -1
  counts = np.zeros(shape=n, dtype=np.int)
  for i in range(len(lst)):
    counts[lst[i]] += 1
  return np.argmax(counts)

def SOM():
  np.random.seed(1)
  diminsion = 4
  Rows = 30; Cols = 30
  rangoMax = Rows + Cols
  factorAprendizaje = 0.5
  iteraciones = 10000
  archivo = "irisData.txt"
  dataEntrenamiento = np.loadtxt(archivo, delimiter=",", usecols=range(0,4),dtype=np.float64)
  salida = np.loadtxt(archivo, delimiter=",", usecols=[4],dtype=np.int)

  #SOM
  pesos = np.random.randn(Rows, Cols,diminsion)
  for s in range(iteraciones):
    alfa = 1.0 - ((s * 1.0) / iteraciones)
    alfaActual = alfa * factorAprendizaje
    rangoActual = (int)(alfa * rangoMax)

    t = np.random.randint(len(dataEntrenamiento))
    (bmu_row, bmu_col) = minimoNodo(dataEntrenamiento, t, pesos, Rows, Cols)

    for i in range(Rows):
      for j in range(Cols):
        if manhattan_dist(bmu_row, bmu_col, i, j) < rangoActual:
          pesos[i][j] = pesos[i][j] + alfaActual * (dataEntrenamiento[t] - pesos[i][j])

  #VISUALIZACIÓN
  print("Visualización")
  mapa = np.empty(shape=(Rows,Cols), dtype=object)
  for i in range(Rows):
    for j in range(Cols):
      mapa[i][j] = []

  for t in range(len(dataEntrenamiento)):
    (m_row, m_col) = minimoNodo(dataEntrenamiento, t, pesos, Rows, Cols)
    mapa[m_row][m_col].append(salida[t])

  label_pesos = np.zeros(shape=(Rows,Cols), dtype=np.int)
  for i in range(Rows):
    for j in range(Cols):
      label_pesos[i][j] = most_common(mapa[i][j], 20)
 
  plt.imshow(label_pesos)
  plt.colorbar()
  plt.show()

# ==================================================================

if __name__=="__main__":
  SOM()
