from PIL import Image

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
sample_size = 700
print(f"\nContoh {sample_size} piksel pertama:")


count = 0  # Untuk menghitung jumlah piksel yang sudah diambil
for y in range(height):
    for x in range(width):
        if count <= sample_size:  # Hanya ambil piksel sampai mencapai 'sample_size'
            r, g, b = img.getpixel((x, y))
            # Menghapus prefix '0b' dan menambahkan leading zero
            r_byte = bin(r)[2:].zfill(8)
            g_byte = bin(g)[2:].zfill(8)
            b_byte = bin(b)[2:].zfill(8)
            print(
                f"Pixel di ({x},{y}): \nR={r}, G={g}, B={b} \nR Byte: {r_byte}, G Byte: {g_byte}, B Byte: {b_byte}\n"
            )

            count += 1
        else:
            break  # Keluar dari loop jika sudah mencapai sample_size
    if count >= sample_size:
        break