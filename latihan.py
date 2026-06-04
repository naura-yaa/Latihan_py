Menu_Makanan = [
    ['Mie Gacoan', 10000],
    ['Mie Hompimpa', 11000],
    ['Udang Keju', 10000],
    ['Es Teh', 8000],
    ['Udang Rambutan', 12000]
]

pesanan = []

# Menu
def mulai():
    print("\n - APLIKASI KASIR -")
    print("1. Menu")
    print("2. Tambah Pesanan")
    print("3. Lihat Pesanan")
    print("4. Total")
    print("5. Riwayat Pembelian")
    print("6. Keluar")

# Lihat Menu
def menu():
    print("\n - DAFTAR MENU -")
    for nama, harga in Menu_Makanan:
        print(f"- {nama}: Rp{harga:,}")

# Tambah Pesanan
def tambah_pesanan():

    nama = input("\nMasukkan nama menu: ").strip().lower()

    for menu, harga in Menu_Makanan:
        if menu.lower() == nama:
            try:
                jumlah = int(input("Jumlah: "))

                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                    return

                subtotal = harga * jumlah

                pesanan.append([menu, harga, jumlah, subtotal])

                print(f"{menu} berhasil ditambahkan!")
                return

            except ValueError:
                print("Jumlah harus berupa angka!")
                return

    print("Menu tidak ditemukan.")


def lihat_pesanan():
    print("\n- PESANAN -")

    if not pesanan:
        print("Belum ada pesanan.")
        return

    for menu, harga, jumlah, subtotal in pesanan:
        print(f"{menu} x{jumlah} = Rp{subtotal:,}")


def total():
    if not pesanan:
        print("Belum ada pesanan.")
        return

    total = sum(item[3] for item in pesanan)

    diskon = 0
    if total >= 50000:
        diskon = total * 0.1

    bayar = total - diskon

    print(f"\nTotal Harga : Rp{total:,.0f}")
    print(f"Diskon      : Rp{diskon:,.0f}")
    print(f"Total Bayar : Rp{bayar:,.0f}")


def riwayat_pembelian():
    if not pesanan:
        print("Belum ada pesanan.")
        return

    total = sum(item[3] for item in pesanan)
    diskon = total * 0.1 if total >= 50000 else 0
    bayar = total - diskon

    print("\n========================")
    print("      RIWAYAT PEMBELIAN")
    print("========================")

    for menu, harga, jumlah, subtotal in pesanan:
        print(f"{menu:<15} x{jumlah:<2} Rp{subtotal:,}")

    print("========================")
    print(f"Total Harga : Rp{total:,.0f}")
    print(f"Diskon      : Rp{diskon:,.0f}")
    print(f"Total Bayar : Rp{bayar:,.0f}")
    print("========================")

# Main Program
def main():
    while True:
        mulai()
        choice = input("Pilih menu (1-6): ")
        if choice == "1":
            menu()
        elif choice == "2":
            tambah_pesanan()
        elif choice == "3":
            lihat_pesanan()
        elif choice == "4":
            total()
        elif choice == "5":
            riwayat_pembelian()
        elif choice == "6":
            print("Terima Kasih! sudah berbelanjaaa.")
            break
        else:
            print("Pilihanlah yang sesuai.")

main()