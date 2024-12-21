import numpy as np
from PIL import Image, ImageDraw

# Stałe
g = 6.67430e-11  # Stała grawitacyjna (m^3 kg^-1 s^-2)
M = 5.972e24      # Masa planety (kg)

# Rozmiar obrazu (piksele)
width, height = 800, 800  # Szerokość i wysokość obrazu w pikselach
center_x, center_y = width // 2, height // 2  # Środek obrazu

# Warunki początkowe w pikselach
x0, y0 = center_x + 100, center_y  # Początkowa pozycja w pikselach
vx0, vy0 = 0.0, 1.0  # Początkowa prędkość w pikselach na krok

# Parametry symulacji
dt = 1  # Krok czasowy (s)

# Funkcja obliczająca przyspieszenie grawitacyjne
def acceleration(x, y):
    r = np.sqrt(x**2 + y**2)
    ax = -g * M * x / r**3
    ay = -g * M * y / r**3
    return ax, ay

# Tworzenie obrazu
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Rysowanie obiektu centralnego
draw.ellipse([
    (center_x - 5, center_y - 5),
    (center_x + 5, center_y + 5)
], fill="red")

# Inicjalizacja położenia i prędkości w pikselach
x, y = x0, y0
vx, vy = vx0, vy0

# Symulacja numeryczna (krok po kroku w pikselach)
for _ in range(5000):  # Liczba kroków symulacji
    # Oblicz przyspieszenie w jednostkach pikseli
    ax, ay = acceleration((x - center_x), (y - center_y))
    ax *= 1e-6  # Skalowanie przyspieszenia do pikseli
    ay *= 1e-6

    # Aktualizuj prędkość
    vx += ax * dt
    vy += ay * dt

    # Oblicz nowe położenie z maksymalnym przesunięciem o 1 piksel
    dx = np.clip(vx, -1, 1)
    dy = np.clip(vy, -1, 1)
    new_x = x + dx
    new_y = y + dy

    # Rysuj trajektorię
    draw.line([(x, y), (new_x, new_y)], fill="blue", width=1)

    # Zaktualizuj pozycję
    x, y = new_x, new_y

# Zapis do pliku i wyświetlenie
output_file = "orbita.png"
image.save(output_file)
image.show()
