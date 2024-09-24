# Shippy
Ecommerce Shippy, giving you an experience to throw away your money.
<details open>
<summary> Tugas 2 </summary>
## Tugas 2
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

</details>


## Tugas 3
#### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery adalah proses pengiriman data antar komponen sistem. Implementasi yang efisien sangat penting agar komponen-komponen dalam sistem dapat saling berbagi data dengan lancar. Banyak fitur dalam pengembangan software yang bergantung pada proses ini, karena data delivery memastikan komunikasi yang tepat waktu, sinkronisasi sistem, serta pengalaman pengguna yang optimal. 

#### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik dibandingkan XML karena memiliki sintaks yang lebih sederhana dan lebih mudah dibaca. JSON menggunakan struktur list, sementara XML menggunakan tag pembuka dan penutup untuk objek-objeknya. Selain itu, JSON lebih cepat dan efisien dalam pemrosesan data dibandingkan XML karena hanya melakukan parsing saja untuk mengambil datanya. JSON juga lebih mudah diintegrasikan dengan API modern dan framework berbasis web. Hal ini menjelaskan mengapa JSON lebih populer dibandingkan XML, karena memberikan kemudahan dan performa yang lebih baik dalam menyimpan dan bertukar data.

#### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django berfungsi untuk memastikan bahwa data yang dimasukkan ke dalam form memenuhi semua kriteria validasi yang telah ditetapkan. Method ini memeriksa apakah setiap field sesuai seperti formatnya dan nilai yang diperlukan. Method ini akan mengembalikan True jika persyaratan tadi dipenuhi dan sebaliknya False jika ada kesalahan. Dengan menggunakan is_valid(), kita dapat memastikan bahwa hanya data yang valid yang diproses atau disimpan nantinya.

#### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token berfungsi untuk melindungi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang memanfaatkan autentikasi pengguna untuk melakukan tindakan berbahaya. Serangan ini dimulai ketika pengguna login ke suatu situs web dan informasi autentikasi disimpan dalam cookie. Penyerang kemudian mengirimkan link berbahaya melalui email atau chat. Jika pengguna mengklik link tersebut tanpa adanya proteksi CSRF, penyerang dapat melakukan tindakan yang merugikan karena pengguna sudah terautentikasi oleh cookie. Namun, dengan adanya CSRF token, server akan memverifikasi token yang dikirim bersama permintaan. Jika tidak ada CSRF token atau tokennya tidak valid, server akan menolak permintaan tersebut dengan memberikan error 403, sehingga serangan dapat dicegah.
#### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect merupakan subclass dari HttpResponse yang digunakan untuk melakukan redirect ke URL lain. Ketika suatu fungsi dalam views mengembalikan HttpResponseRedirect, Django akan merespons dengan kode status seperti 302 (Found, jika URL valid), yang merupakan pengalihan sementara, serta menambahkan header Location yang berisi URL tujuan yang akan dikunjungi oleh client setelah melakukan request.

Redirect adalah fungsi shortcut yang disediakan oleh Django untuk mengembalikan HttpResponseRedirect. Berbeda dengan HttpResponseRedirect yang hanya menerima URL, redirect dapat mencari URL yang sesuai di urls.py, sehingga sangat berguna dalam aplikasi yang kompleks di mana rute URL dapat dikelola lebih fleksibel.

Contoh:
```python
# Menggunakan HttpResponseRedirect, perlu memakai reverse untuk mencari URL yang sesuai
response = HttpResponseRedirect(reverse("main:show_main"))

# Menggunakan redirect, langsung dapat cuy
response = redirect("main:show_main")
```

#### 2. Jelaskan cara kerja penghubungan model Product dengan User!

Pertama-tama, kita memodifikasi model dari ProductEntry dengan menambahkan atribut User, yang diimpor dari:

```python
from django.contrib.auth.models import User
```

Pada model ProductEntry, kita menambahkan:
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Sintaks tersebut berfungsi untuk menghubungkan model ProductEntry dengan pengguna (user) melalui ForeignKey. Ini dikenal sebagai Total Relation, artinya setiap entri produk terkait dengan satu pengguna. Jika pengguna yang terkait dihapus, maka semua entri produk yang berhubungan dengan pengguna tersebut juga akan ikut terhapus karena kita menggunakan on_delete=models.CASCADE.

Setelah itu, pada bagian views.py, kita menghubungkan model ini di dalam fungsi make_entry_product. Di sini, kita membuat instance dari ProductForm, kemudian kita memvalidasi form menggunakan form.is_valid(), dan mengecek apakah request yang masuk menggunakan metode POST.

Jika valid, kita membuat instance dari ProductEntry melalui form dengan menggunakan form.save(commit=False), sehingga data form belum langsung disimpan ke database, memberi kita kesempatan untuk menambahkan informasi tambahan. Kemudian kita menghubungkan entri produk ini dengan pengguna yang sedang login menggunakan product_entry.user = request.user.

Setelah menghubungkan entri dengan pengguna, kita memanggil product_entry.save() untuk menyimpan entri produk ke dalam database. Dengan langkah-langkah ini, setiap produk yang dibuat akan otomatis terhubung dengan pengguna yang membuatnya.

```python
def make_entry_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)  # Membuat instance tanpa menyimpan ke database
        product_entry.user = request.user  # Menghubungkan entri produk dengan pengguna yang sedang login
        product_entry.save()  # Menyimpan entri produk ke database
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```
 
#### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Authentication adalah proses mengidentifikasi pengguna saat mereka mencoba untuk login ke aplikasi. Di Django, saat pengguna melakukan login, sistem authentication akan mencocokkan kredensial yang dimasukkan dalam form login dengan data yang ada di database, atau memverifikasi session token untuk memastikan bahwa pengguna tersebut adalah sah. Untuk implementasi authentication, Django menyediakan fungsi login() untuk memulai sesi pengguna, UserCreationForm untuk membuat pengguna baru, dan AuthenticationForm untuk autentikasi pengguna dengan kredensial yang diberikan.

Sementara itu, Authorization adalah proses yang menentukan hak akses atau izin yang dimiliki oleh pengguna setelah mereka berhasil melewati proses authentication. Authorization mengontrol apa yang dapat dilakukan pengguna dalam aplikasi, seperti mengakses halaman tertentu atau melakukan tindakan spesifik. Di Django, authorization diimplementasikan menggunakan decorators seperti @login_required, yang memastikan hanya pengguna yang telah login yang dapat mengakses view tertentu, dan @permission_required, yang memeriksa apakah pengguna memiliki izin tertentu.

#### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan memanfaatkan cookies. Cookie adalah penyimpanan data sementara di sisi klien yang digunakan untuk menyimpan session ID dan informasi autentikasi. Dengan menyimpan session ID dalam cookie, Django dapat mengidentifikasi pengguna dan menjaga agar sesi tetap aktif sepanjang waktu, sehingga pengguna tidak perlu login berulang kali setiap kali mereka mengunjungi aplikasi. Ini memudahkan pengalaman pengguna dan memastikan konsistensi selama sesi aktif.

Cookies juga berguna untuk menyimpan data sementara, mengingat bahwa HTTP bersifat stateless, yang berarti setiap permintaan HTTP independen dan tidak menyimpan informasi tentang permintaan sebelumnya. Dengan menggunakan cookies, aplikasi web dapat menyimpan informasi penting seperti preferensi pengguna atau status autentikasi, sehingga dapat mempertahankan keadaan dan memberikan pengalaman yang lebih baik kepada pengguna.

Namun Cookies tidak selalu aman digunakan karena dapat digunakan dalam CSRF attack. Dimana penyerang memanfaatkan user yang sudah terautentikasi yang tersimpan di cookies

#### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Pertama saya membuat fungsi user_login, user_register, dan user_logout pada views.py. Disini saya mengimport beberapa library yang diperlukan salah satunya adalah django.contrib.auth. 
- Kedua, saya mengimplementasikan fungsi user_register untuk menangani pendaftaran pengguna baru. Di dalam fungsi ini, saya membuat instansi UserCreationForm() yang akan ditampilkan di template jika permintaan (request) bukan metode POST. Namun, jika permintaan adalah POST, maka UserCreationForm akan diisi dengan data yang dikirim dalam request.POST untuk membuat pengguna baru. Setelah itu, form akan divalidasi; jika valid, pengguna baru akan disimpan ke dalam database. Setelah pendaftaran berhasil, pengguna akan diberikan pesan sukses dan diarahkan ke halaman login. Jika terjadi kesalahan saat pendaftaran, pesan error akan ditampilkan. Berikut adalah implementasi kodenya:

```python
def user_register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        else :
            messages.error(request, 'Error creating your account')
    context = {'form':form}
    return render(request, 'register.html', context)
```

Setelah itu saya mengimplementasikan ini kedalam urls.py (membuat path) dan membuat html page khusus untuk register.

- Ketiga, saya mengimplementasikan fungsi user_login yang berfungsi untuk melakukan autentikasi pada pengguna yang sudah teregistrasi. Dalam fungsi ini, kita menggunakan AuthenticationForm untuk menangani data autentikasi. Jika permintaan (request) adalah POST, kita membuat instansi AuthenticationForm dengan data dari request.POST. Jika permintaan bukan POST, kita membuat instansi AuthenticationForm kosong untuk menampilkan form login yang kosong.

Jika form autentikasi valid, kita mengambil pengguna yang terkait dengan form tersebut menggunakan form.get_user() dan kemudian melakukan login dengan memanggil fungsi login() dari django.contrib.auth. Setelah pengguna berhasil login, kita mengatur cookie untuk menyimpan informasi waktu login terakhir dan mengarahkan pengguna ke URL yang ditentukan (dalam hal ini, show_main) menggunakan HttpResponseRedirect. Berikut adalah implementasi kodenya:
``` python
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)   
```

Kita juga menyimpan informasi login ini dalam cookies yang di set pada response. Kemudian user akan di alihkan sementara ke show_main url. Setelah itu sama seperti sebelunmnya, mengimplementasikan ini kedalam urls.py (membuat path) dan membuat html page.

- Keempat, saya membuat fungsi logout yang hanya berisi fungsi logout yang sudah disediakan dari django.contrib.auth. Kemudian kita redirect ke login page dan tidak lupa kita delete cookie nya. Berikut adalah implementasi kodenya:

```python
def user_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

- Saya juga menambahkan requirement yang dibutuhkan untuk show_main agar user yang tidak terlogin tidak dapat mengakses show_main apabila tidak melakukan login. Saya juga menambahkan cookies dalam context agar user dapat terautentikasi setiap saat.

```python
@login_required(login_url='main:login')
def show_main(request):
    product_entry = ProductEntry.objects.all()
    context = {
        'username' : request.user,
        'products' : product_entry,
        'last_login': request.COOKIES['last_login'] if "last_login" in request.COOKIES else None,
    }
    return render(request, "main.html", context)
```

- Terakhir saya menghubungkan product dengan user dengan cara menambahkan atribut user pada model. 
```python
class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField() 
    description = models.TextField()
```

Kemudian kita menambahkan atribut ini pada make_entry_product
```python
def make_entry_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```