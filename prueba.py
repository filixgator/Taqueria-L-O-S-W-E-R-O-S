import matplotlib.pyplot as plt
names = ['Mulitas','Quesadillas','Tacos','Tortas','Tostadas']
values = [10, 10,20,30, 40]

plt.figure(1, figsize=(18, 5))

#Cantidad de tacos
plt.subplot(231)
plt.bar(names, values)

#Tiempo por orden
plt.subplot(232)
plt.plot(names, values)


#Promedio por orden
plt.subplot(233)
plt.scatter(names, values)

#Grafica 4
plt.subplot(234)
plt.scatter(names, values)

#Grafica 5
plt.subplot(235)
plt.scatter(names, values)
plt.suptitle('Taqueria los WERS')
plt.show()
