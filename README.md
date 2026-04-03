# Discord Voice Manager

![April 2026 Integrity Ready](https://img.shields.io/badge/Discord--API-April%202026%20Ready-blue?style=for-the-badge)
![UI](https://img.shields.io/badge/UI-PyQt6%20AMOLED-000000?style=for-the-badge)

**Discord Voice Manager**, birden fazla hesabı aynı anda ses kanallarında yönetmenizi sağlayan, Nisan 2026 güvenlik protokollerine (Integrity Patch) tam uyumlu, modern ve yüksek performanslı bir yönetim panelidir.

## 🚀 Öne Çıkan Özellikler

- **Modern PyQt6 Arayüzü:** Akıcı, hızlı ve kararlı masaüstü deneyimi.
- **Dinamik Tema Desteği:**
  - **AMOLED Siyah:** OLED ekranlar için saf siyah (#000000) tasarım.
  - **Full White:** Temiz ve aydınlık çalışma alanı.
- **Nisan 2026 Güvenlik Yaması:**
  - `Build 522553` senkronizasyonu.
  - `X-Discord-Fingerprint` otomatik experiment fetching.
  - API v10 protokol desteği.
- **Gelişmiş Toplu Kontroller (Bulk Controls):**
  - Tek tıkla Join / Stop.
  - Toplu Susturma (Mute) ve Sağırlaştırma (Deafen).
  - Toplu Kamera (Video) ve Yayın (Go Live) açma/kapama.
  - **Yeni:** Mute & Deafen (Tam Sessizlik) kombinasyonu.
- **Bireysel Hesap Yönetimi:** Her hesabı ayrı ayrı kontrol edebilme, durum takibi ve kanal değişimi.

## 🛠️ Kurulum

1. Python 3.10+ kurulu olduğundan emin olun.
2. Bağımlılıkları yüklemek için:
   ```bash
   pip install -r requirements.txt
   ```
3. `tokens.txt` dosyasına Discord tokenlarınızı her satıra bir tane gelecek şekilde ekleyin.
4. Uygulamayı başlatın (Siyah terminal penceresi istemiyorsanız `main.pyw` dosyasını çalıştırın):
   ```bash
   python main.pyw
   ```

## 📋 Kullanım

- **Dashboard:** Sunucu ve Kanal ID bilgilerini girerek tüm botları aynı anda kanala sokabilir veya toplu komutlar verebilirsiniz.
- **Accounts:** Botların canlı durumlarını (Connected/Disconnected) görebilir, mikrofon/kulaklıklarını kilit butonuyla anında kapatıp açabilirsiniz.
- **Settings:** Sol alttaki "Appearance Mode" üzerinden favori temanızı seçebilirsiniz.

## ⚠️ Önemli Notlar

- Sunucuya katılım (Join) işlemleri için hesaplarınızın telefon veya e-posta onaylı olması önerilir.
- Nisan 2026 güncellemeleri sayesinde "Uygulamanı Güncelle" hatası %99 oranında giderilmiştir.

---
**Developed by Efe Kırbaş**
