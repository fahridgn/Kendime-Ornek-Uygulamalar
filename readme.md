# Django - HTMX - Rest FrameWork - Basit Uygulamalar

Bu proje, yalnızca kendimi geliştirmek amaçlı saçma sapan örneklerle doludur ama merak ediyorsanız elbette bakabilirsiniz. Projede django başta olmak üzere rest-framework, htmx, bootstrap ve bazı detayları işledim (aşağıda detaylar var). Bazı fazlalık dosyalar var silmek istemedim çünkü bu projenin üzerine inşa etmeye devam edeceğim ve o fazlalıklar işe yarar hale gelecek. Umarım okuyup vakit ayırdığınız zaman ziyan olmaz çünkü zaman çok kıymetli ve faydasız olduğunu düşündüğünüz an bence projeyi incelemeyi bırakın.

## Kurulum

Projeyi yerel bilgisayarınıza klonlayın:

```bash
git clone (https://github.com/fahridgn/Kendime-Ornek-Uygulamalar.git)
```

Proje klasörüne gidin:

```bash
cd [proje-adı]
```

Gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

Sitenin içinde htmx ile interaktif bir uygulama (themes) bulunmakta, burada crud işlemlerini olduğu yerde yapabilmeyi amaçladım. Bir diğer uygulama is aslında react ile önyüzünü oluşturduğum todo uygulamasının json çıktısı için kullandığım rest-framework todo uygulaması (oldukça basit bir şey, kodları incelediğinizde anlayacaksınız). Burada benim için önemli olan bir başka şey ise bütün uygulamalarımdan ve template dosyalarımdan erişebildiğim bir yapıyı keşfettim, birçok kişi bunu biliyormuş ama ben yeterince irdelendiğini düşünmüyorum bunun adı ise context_processors. Bu sayede projede tema ayarları gibi her yerden ulaşılması gereken verilere tek yönetim merkezinden erişebiliyorsunuz bkz.[backend/themes/context_processors.py].

## Veritabanı Ayarları

Eğer projeniz bir veritabanı kullanıyorsa, veritabanı ayarlarınızı buraya ekleyin.

```bash
python manage.py migrate
```

## Django Admin

Projede kullanılan Django Admin paneline erişmek için:

1. [localhost:8000/admin/](http://localhost:8000/admin/) adresine gidin.
2. [admin] ve [azsxdc1234] ile giriş yapın.

## API Endpoints

Projenin sunduğu API endpoint'lerini ve nasıl kullanılacağını açıklayın.

## Ekran Görüntüleri

Projenin bazı ekran görüntülerini ekleyin (varsa).

## Geliştirme

Projeyi geliştirmek veya özelleştirmek istiyorsanız, aşağıdaki adımları takip edin:

1. [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.
2. Kendi değişikliklerinizi yapın.
3. Değişikliklerinizi bir pull request (çekme isteği) ile gönderin.

## Lisans

Bu proje herhangi bir lisansa sahip değildir kullanımı tamamen özgür. Dilediğiniz gibi faydalanabilirsiniz.
