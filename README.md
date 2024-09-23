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