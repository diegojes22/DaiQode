# Generador de Tarjetas WiFi (QR)
`Un proyecto de tiempo libre 😉`

Proyecto básico en Python para generar automáticamente:

- Redes WiFi (SSID aleatorios con un prefijo configurable).
- Contraseñas aleatorias seguras (longitud 10–14 caracteres).
- Códigos QR compatibles con el estándar WiFi (formato `WIFI:T:...;S:...;P:...;;`).
- Tarjetas (imágenes PNG) listas para entregar a un cliente, con QR, SSID, contraseña, icono central y logo inferior.

Ideal para instaladores de routers que desean entregar una tarjeta visual al usuario final o para preparar material de prueba/demostración.

---

## 🗂 Estructura del proyecto

```
main.py                # Script principal: genera 10 redes y produce QR + tarjetas
qrWifi.py              # Clases QrWiFi y WiFiCard (lógica de QR y render de tarjeta)
pathAdmin.py           # Utilidades de rutas del proyecto
otherData/
	myvars.py            # Variables de configuración (rutas de icono, logo, fuente, prefijo SSID)
README.md
```

Carpetas esperadas (crearlas si no existen antes de ejecutar):
```
qr/    # Aquí se guardan los QR individuales (solo el código)
out/   # Aquí se guardan las tarjetas completas (QR + texto + logo)
```

---

## 🚀 Características principales

- Prefijo configurable para SSID (`my_main_wifi_keyword`).
- Inserción de icono centrado dentro del código QR.
- Generación de tarjeta 400x200 px con bordes, colores y tipografía personalizada.
- Logo opcional en la parte inferior derecha.
- Manejo básico de errores al cargar icono, logo y fuente (usa fuente por defecto si falla).

---

## 🧩 Dependencias

Requiere Python 3.10+ (recomendado) y las siguientes librerías:

```
pip install qrcode[pil] Pillow
```

Opcional: crear un entorno virtual antes.

```
python -m venv .venv
./.venv/Scripts/Activate.ps1   # PowerShell en Windows
pip install --upgrade pip
pip install qrcode[pil] Pillow
```

---

## ⚙️ Configuración (otherData/myvars.py)

```python
my_logo = "C:/ruta/a/logo.png"
my_font = "C:/ruta/a/fuente.ttf"
my_wifi_icon = "C:/ruta/a/icono_wifi.png"
my_main_wifi_keyword = "DaiNet"
```

Recomendaciones:
- Puedes cambiar rutas absolutas por relativas (por ejemplo, colocar recursos en una carpeta `assets/`).
- Asegúrate de que la fuente soporte caracteres que planees usar.

---

## ▶️ Uso rápido

1. Clona o copia el proyecto.
2. Crea (si no existen) las carpetas `qr/` y `out/` en la raíz del proyecto.
3. Ajusta `otherData/myvars.py` con tus rutas reales.
4. Instala dependencias.
5. Ejecuta:
	 ```
	 python main.py
	 ```
6. Revisa las imágenes generadas en `qr/` y `out/`.

El script genera por defecto 10 redes distintas (puedes cambiar el rango en `main.py`).

---

## 🧪 Ejemplo de uso de las clases

```python
from qrWifi import QrWiFi, WiFiCard

wifi = QrWiFi("MiRedDemo", "MiPass1234")
wifi.set_icon("assets/wifi.png")

card = WiFiCard(wifi)
card.set_font("assets/PlusJakartaSans.ttf")
card.set_bottom_logo("assets/logo.png")
card.draw().save("out/mi_tarjeta.png")
```

---

## 🖼 Formato del QR generado

Se usa la cadena estándar:
```
WIFI:T:WPA2;S:<SSID>;P:<PASSWORD>;;
```
Si necesitas redes abiertas, inicializa `QrWiFi` con `security = "nopass"` y deja la contraseña vacía.

---

## 🔐 Nota sobre seguridad

Este proyecto genera contraseñas aleatorias sencillas para demostración. Para entornos reales:
- Usa un generador más robusto (más longitud y más diversidad de caracteres).
- No publiques contraseñas reales en repositorios.
- Considera parametrizar el número de redes y longitud de la contraseña mediante argumentos CLI.

---

## 💡 Posibles mejoras futuras

- Creación automática de carpetas `qr/` y `out/` si no existen.
- Interfaz CLI (argparse) para definir cantidad, prefijo y longitud de contraseña.
- Exportar a PDF múltiple con todas las tarjetas.
- Temas de diseño (colores, tamaños y layouts configurables).
- Validación y normalización de rutas (uso de `pathlib`).

---

## ✅ Checklist rápido antes de ejecutar

- [ ] Dependencias instaladas.
- [ ] Rutas en `myvars.py` válidas.
- [ ] Carpetas `qr/` y `out/` creadas.
- [ ] Fuente / icono / logo accesibles.

---

## 📄 Licencia

GNU GPL 3.0

---

## 🙋‍♂️ Contribuciones

Puedes adaptar este código a tus necesidades. Si planeas ampliarlo, separar la lógica en módulos (por ejemplo, `utils/`, `models/`, `cli/`) facilitará el mantenimiento.

---