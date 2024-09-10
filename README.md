# Shippy
Ecommerce Shippy, giving you an experience to throw away your money.

#### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat github repo shippy dan melakukan clone ke dalam local directory saya
- Membuat envriontment dan membuat requirements untuk menginstall resource yang dibutuhkan
- Membuat proyek awal Django dengan startproject dan kemudian menambahkan gitignore
- Membuat aplikasi main dan melakukan beberapa penyesuaian seperti pada direktori luar bagian settings.py dengan menambahkan host yang diperbolehkan untuk pws dan local host, menambahkan main pada installed app, dan menghubungkan url aplikasi main ke urls.py
- Adapun penyesuaian yang dilakukan pada direktori aplikasi main seperti menambahkan templates (html, disini saya memakai tailwind untuk mempercantiknya), menambahkan model dan melakukan migrate, menambahakan render code dibagian view,dan terakhir menambahkan path render di urls.py.
- Terakhir tinggal di coba runserver untuk memastikan semua berjalan aman dan melakukan push di pws.

#### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![MVT Diagram](/shippy/scr/PBP.drawio.png)

#### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Git berfungsi sebagai sistem kontrol versi yang berarti ia menyimpan riwayat perubahan atau versi dari sebuah proyek. Fitur ini memudahkan programmer untuk kembali ke versi sebelumnya jika diperlukan, dan sangat berguna untuk kolaborasi tim. Dengan Git, setiap anggota tim dapat bekerja pada bagian yang berbeda dari proyek secara paralel tanpa saling mengganggu, serta dapat menggabungkan perubahan mereka dengan mudah.


#### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Menurut saya, keramahan pemula menggunakan Django merupakan poin utama. Django membawa banyak sekali fitur bawaan dibandingkan framework lainnya, sehingga programmer hanya perlu memakai fitur tersebut untuk membuat sebuah website dengan cepat. Fitur-fitur seperti ORM (Object-Relational Mapping) dan routing URL sudah disediakan secara default, yang memudahkan pemula dalam membangun aplikasi tanpa harus mengonfigurasi banyak hal dari awal.

Ditambah dengan bahasa pemrograman yang digunakan adalah Python, yang juga dipakai di DDP1 dan terkenal ramah pemula, hal ini membuat Django menjadi framework yang sangat ideal bagi mereka yang baru memulai. Python memiliki sintaks yang sederhana dan intuitif, sehingga membantu pemula fokus pada konsep pengembangan tanpa terbebani oleh kompleksitas bahasa. Selain itu, Django juga terstruktur dengan baik, menggunakan pola *Model-View-Template (MVT)*, yang membantu programmer memahami dan mengelola proyek dengan lebih mudah dan teratur.

#### 5. Mengapa model pada Django disebut sebagai ORM?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pemetaan objek Python langsung ke tabel database, sehingga kita bisa mengelola database tanpa menulis query SQL manual. ORM memudahkan pengembang untuk melakukan operasi seperti membuat, membaca, memperbarui, dan menghapus data (CRUD) langsung dengan kode Python. Django juga otomatis menangani relasi antar-tabel, sehingga pengelolaan database lebih efisien dan terstruktur.