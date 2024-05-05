import math

def eudistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Örnek noktalar
x1, y1 = 3,5
x2, y2 = 2,1

# Öklid mesafesini hesapla
distance = eudistance(x1, y1, x2, y2)
print("Öklid Mesafesi:", distance)