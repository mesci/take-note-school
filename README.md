# Not Alma Uygulaması

Basit bir Python not alma uygulaması. Bu uygulama ile kullanıcılar not ekleyebilir, düzenleyebilir, silebilir ve notlarını listeleyebilir. Notlar bir `.txt` dosyasında saklanır.

## Özellikler
- **Giriş Yapma:** Kullanıcı adı ve şifre ile giriş.
- **Not Ekleme:** Yeni bir not oluşturma.
- **Not Düzenleme:** Mevcut notların başlık ve içeriğini güncelleme.
- **Not Silme:** İstenilen notu silme.
- **Not Listeleme:** Tüm notları görüntüleme.

## Kurulum
1. Bu repoyu klonlayın:
   ```bash
   git clone https://github.com/mesci/take-note-school.git
   ```
2. Proje dizinine gidin:
   ```bash
   cd take-note-school
   ```
3. Uygulamayı çalıştırın:
   ```bash
   python main.py
   ```

## Kullanım
1. Uygulamayı başlattığınızda, kullanıcı adı ve şifre ile giriş yapmanız istenecektir.
   - Varsayılan kullanıcı adı: `admin`
   - Varsayılan şifre: `sifre123`

2. Giriş yaptıktan sonra menüden bir işlem seçebilirsiniz:
   - **1:** Yeni not eklemek için.
   - **2:** Mevcut bir notu düzenlemek için.
   - **3:** Bir notu silmek için.
   - **4:** Tüm notları listelemek için.
   - **5:** Uygulamadan çıkmak için.

## Notların Saklanması
Tüm notlar `notes.txt` dosyasında aşağıdaki formatta saklanır:
```
ID|Başlık|İçerik
```
## Yusuf Mescioğlu - 220202071
