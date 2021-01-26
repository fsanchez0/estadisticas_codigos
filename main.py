from connector import DatabaseManip as Db
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


consulta = Db()
qresult = consulta.obtener_codigos()
df = pd.DataFrame(qresult)
df2 = df

def colocar_horas(x):
    x = int(x)
    x = x/60
    x = str(x)
    x+=' H'
    return x


df.to_csv(r'export_data.csv', index= False)
df['tiempo'] = df['tiempo'].apply(colocar_horas)
df.groupby('tiempo')['codigo'].nunique().plot(kind='bar', color=['coral', 'lightgreen', 'gold', 'red','teal'], edgecolor='black')
print(df.groupby(['tiempo','precio']).count())
plt.title('Venta de Códigos Segunda Quincena Enero 2021')
plt.xlabel('Tiempo')
plt.ylabel('# Códigos Vendidos')


fix, ax = plt.subplots(figsize=(10, 5))
def quitar_hora(x):
    x = str(x)
    fecha = x.split()
    return fecha[0]

df2['hora'] = df2['hora'].apply(quitar_hora)
df2.groupby(['hora']).count()['codigo'].plot(ax=ax)

plt.show()

