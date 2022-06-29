import sqlite3
from tabulate import tabulate


connection = sqlite3.connect("produk.db")
cursor = connection.cursor()


def print_output(rows):
    headers = ["nama", "harga", "rating", "likes"]
    data = []
    for i in rows:
        data.append(list(i))
    print(tabulate(data, headers=headers, tablefmt="pretty"), end="\n\n")


def pilihan(p):
    if (p == "1"):
        rows = cursor.execute("SELECT * FROM produk",).fetchall()
        print_output(rows)
    elif (p == "2"):
        rows = cursor.execute("SELECT * FROM produk ORDER BY \
                harga ASC, \
                rating DESC, \
                likes DESC",).fetchall()
        print_output(rows)
    elif (p == "3"):
        nama = input("Nama produk: ")
        harga = input("Harga produk: ")
        rating = input("Rating produk: ")
        likes = input("Likes produk: ")
        cursor.execute("INSERT INTO produk VALUES (?, ?, ?, ?)", \
                       (nama, harga, rating, likes),)
        connection.commit()
    elif (p == "4"):
        cursor.close()
        connection.close()
        exit()


while (True):
    print("Menu: ")
    print("1. Tampilkan data produk awal")
    print("2. Tampilkan data produk yang sudah diurutkan")
    print("3. Masukkan produk baru ke database")
    print("4. Keluar")
    print("Pilihan:", end=" ")
    pil = input()
    pilihan(pil)
