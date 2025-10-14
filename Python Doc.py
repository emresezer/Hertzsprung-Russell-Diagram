import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

luminosity = [1,25.4,120000,0.0017,17] 
temperature = [5778,9940,3500,3000,25000] 
sizes = [10,17.1,85,1.4,17]

colors = ['red', 'orange', 'yellow', 'white', 'turquoise', 'blue', 'navy']
custom_cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)
plt.figure(figsize=(8, 6))
scatter = plt.scatter(temperature, luminosity, c=temperature, cmap=custom_cmap, s=sizes, edgecolors='k')
plt.gca().invert_xaxis()  

plt.title("Hertzsprung-Russell Diyagramı")
plt.xlabel("Yüzey Sıcaklığı (K)")
plt.ylabel("Parlaklık (Güneş Birimi)")
plt.colorbar(scatter, label="Sıcaklık (K)") 
plt.yscale("log")  
plt.show()
