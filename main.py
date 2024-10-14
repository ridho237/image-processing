from PIL import Image
import colorsys #modul untuk konversi warna

# Membuat variabel yang akan menerima gambar
# Menggunakan function Image.open untuk membuat image
img = Image.open('ayaka!.jpg')

# Menampilkan Gambar
img.show()


# Ngambil ukuran gambar (width, height)
width, height = img.size
total_pixels = width * height

# Cetak ukuran gambar dan total piksel buat bukti
print(f"Ukuran gambar: {width}x{height}")
print(f"Total piksel: {total_pixels}")

# Gara-Gara Ayaka-chan pikselnya banyak maka Tentukan jumlah piksel untuk ditampilkan
sample_size = 10
print(f"\nContoh {sample_size} piksel pertama:")


count = 0  # Untuk menghitung jumlah piksel yang sudah diambil
for y in range(height):
    for x in range(width):
        if count <= sample_size:  # Hanya ambil piksel sampai mencapai 'sample_size'
            r, g, b = img.getpixel((x, y))

            # Konversi ke HSL (Hue, Saturation, Lightness)
            hsl = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
            h, l, s = hsl

            # Konversi ke HSV (Hue, Saturation, Value)
            hsv = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
            h_hsv, s_hsv, v_hsv = hsv

            # Konversi ke Hexcode
            hexcode = f'#{r:02x}{g:02x}{b:02x}'

            # Menghapus prefix '0b' dan menambahkan leading zero
            r_byte = bin(r)[2:].zfill(8)
            g_byte = bin(g)[2:].zfill(8)
            b_byte = bin(b)[2:].zfill(8)

            print(f"Pixel di ({x},{y}): \nR={r}, G={g}, B={b} | Red:Byte={r_byte}, Green:Byte={g_byte}, Blue:Byte={b_byte}")
            print(f"HSL: Hue={h:.2f}, Saturation={s:.2f}, Lightness={l:.2f}")
            print(f"HSV: Hue={h_hsv:.2f}, Saturation={s_hsv:.2f}, Value={v_hsv:.2f}")
            print(f"Hexcode: {hexcode}\n")

            count += 1
        else:
            break  # Keluar dari loop jika sudah mencapai sample_size
    if count >= sample_size:
        break