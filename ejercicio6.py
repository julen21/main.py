import statistics as st
data = list()
for indice in range(3):
    data.append(float(input("siguiente dato?: ")))

dato = st.mean(data)
print("media:", dato)

dato2 = st.median(data)
print("mediana:", dato2)

dato3 = st.variance(data)
print("varianza:", dato3)

