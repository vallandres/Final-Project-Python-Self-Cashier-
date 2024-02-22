# Final Project Python: Self-Cashier



## Background Masalah
Andi pemilik Supermarket besar. Ia memiliki rencana untuk melakukan perbaikan proses bisnis dengan membuat sistem kasir yang self-service di supermarket miliknya agar customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. Ini juga untuk memudahkan customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.

Setelah melakukan riset, Andi ternyata membutuhkan Programmer untuk membuatkan fitur-fitur tersebut agar sistem kasir self service di supermarket itu bisa berjalan dengan lancar.

## Objektif
Membuat sebuah program kasir self-service menggunakan Python.

## Tools
Python

## Requirements 
- Membuat Class Transaction
- Membuat add item.
- Dapat melakukan update nama item.
- Dapat melakukan update jumlah item.
- Dapat melakukan update harga item.
- Dapat melakukan delete item.
- Dapat melakukan reset transaksi.
- Dapat melakukan cek order.
- Menghitung total harga.

## Flowchart  
 <p>
<img align="center" src="https://drive.google.com/uc?export=view&id=1riHeht2ysGpinXsLrpwUgVhjVLUWPSN_" alt="Flowchart" width="300" />
</p>

## Fungsi 
1.  Class: Transaction
    - Dibuat suatu class yang diberi nama Transaction yang digunakan sebagai  wadah untuk menghimpun data dan fungsi yang kemudian menghasilkan objek.
2.  Method: __init__
    - Dibuat ini digunakan untuk menyimpan data item belanjaan ke dalam bentuk dictionary.
3.  Method: add_item
    - Method ini digunakan untuk menambahkan data belanjaan. Dengan tiga parameter yaitu nama, jumlah dan harga.
4.  Method: update_item_name
    - Method ini digunakan untuk mengganti nama item belanjaan jika terjadi  kesalahan dalam memasukkan nama item.
5.  Method: update_item_qty
    - Method ini digunakan untuk mengubah jumlah item dari suatu item belanjaan.
6.  Method: update_item_price
    - Method ini digunakan untuk untuk mengubah suatu harga dari item belanjaan.
7.  Method: delete_item
    - Method ini berguna untuk menghapus salah satu item belanjaan.
8.  Method: reset_transaction
    - Method ini berguna untuk menghapus seluruh item pada data belanjaan.
9.  Method: check_order
    - Method ini digunakan untuk mengecek daftar barang belanjaan yang sudah input, memastikan bahwa itemnya sudah sesuai yang diinginkan.
10. Method: total_price
    - Method digunakan untuk menghitung harga total dari semua item belanjaan yang sudah diinput.

## Test Case

### Test 1

Customer ingin menambahkan dua item baru menggunakan method add_item (). Item yang ditambahkan adalah sebagai berikut:

Nama Item: Ayam Goreng, Qty: 2, Harga: 20000

Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

*Output:*

 <p>
<img align="center" src="https://drive.google.com/uc?export=view&id=1_Eubf51Qyqm0_vGhe6EN27upFZAS5lFR" alt="Flowchart" width="500" />
</p>


### Test 2

Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan,maka Customer menggunakan method de lete_item() untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi.

**Output**

<p>
<img align="center" src="https://drive.google.com/uc?export=view&id=1f7YdK4ZajYDxV0n_lHCQEVF_Ttyt2mns" alt="Flowchart" width="500" />
</p>

### Test 3

Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan!

Daripada menghapusnya satu - satu, maka Customer cukup menggunakan method reset transaction() untuk menghapus semua item yang sudah ditambahkan.

**Output**

<p>
<img align="center" src="https://drive.google.com/uc?export=view&id=13ApxAuZCT3gcQJwRdoTvkbh0o-0-vq5I" alt="Flowchart" width="500" />
</p>


### Test 4

Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total price (). Sebelum mengeluarkan output total belanja akan menampilkan item - item yang dibeli.

**Output**

<p>
<img align="center" src="https://drive.google.com/uc?export=view&id=13_ftpoI7irBgr_m-L_pbWQItxSYSN05z" alt="Flowchart" width="500" />
</p>


## Kesimpulan

Program ini sudah berjalan dengan baik, tetapi diperlukan pengembangan berkelanjutan untuk peningkatan program agar meberikan kesan baik kepada pengguna.






