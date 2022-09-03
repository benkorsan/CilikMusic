HELP_1  =  """✅**<u>Yönetici Komutları:</u>**
**c** kanal oynatma anlamına gelir.
/pause veya /cpause - Çalan müziği duraklatın.
/resume veya /cresume- Duraklatılan müziği devam ettirin.
/mute veya /cmute- Çalan müziğin sesini kapatın.
/unmute veya /cunmute- Sesi kapatılan müziğin sesini açın.
/atla veya /cskip- Çalmakta olan müziği atla.
/stop veya /cstop- Çalan müziği durdurun.
/shuffle veya /cshuffle- Sıraya alınmış çalma listesini rastgele karıştırır.
/seek veya /cseek - İleri Müziği sürenize göre arayın
/seekback veya /cseekback - Geriye Müziği sürenize göre arayın
/restart - Sohbetiniz için botu yeniden başlatın.
✅<u>**Belirli Atlama:**</u>
/skip veya /cskip [Sayı(örnek: 3)]
    - Müziği belirtilen sıraya alınmış numaraya atlar. Örnek: /skip 3, müziği sıraya alınan üçüncü müziğe atlar ve sıradaki 1 ve 2 müziği yok sayar.
✅<u>**Döngü Oyna:**</u>
/loop veya /cloop [etkinleştir/devre dışı bırak] veya [1-10 arasındaki sayılar]
    - Etkinleştirildiğinde, bot sesli sohbette çalmakta olan müziği 1-10 kez döngüye alır. Varsayılan olarak 10 kez.
✅<u>**Yetkili Kullanıcılar:**</u>
Yetkilendirme Kullanıcıları, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.
/auth [Kullanıcı adı] - Grubun YETKİ LİSTESİ'ne bir kullanıcı ekleyin.
/unauth [Kullanıcı adı] - Bir kullanıcıyı grubun YETKİ LİSTESİ'nden kaldırın.
/authusers - Grubun YETKİ LİSTESİ'ni kontrol edin."""


HELP_2  =  """✅<u>**Çal Komutları:**</u>
Kullanılabilir Komutlar = oynat, vplay, cplay
ForcePlay Komutları = playforce, vplayforce, cplayforce
**c** kanal oynatma anlamına gelir.
**v** video oynatma anlamına gelir.
**kuvvet** kuvvet oyunu anlamına gelir.
/play veya /vplay veya /cplay - Bot, verilen sorgunuzu sesli sohbette veya Sesli sohbetlerde Canlı bağlantı akışında oynatmaya başlar.
/playforce veya /vplayforce veya /cplayforce - **Force Play**, sesli sohbette mevcut parçayı durdurur ve sırayı bozmadan/temizlemeden aranan parçayı anında çalmaya başlar.
/channelplay [Sohbet kullanıcı adı veya kimliği] veya [Devre dışı bırak] - Kanalı bir gruba bağlayın ve grubunuzdan kanalın sesli sohbetinde müzik akışı yapın.
✅**<u>Bot'un Sunucu Oynatma Listeleri:</u>**
/playlist - Sunucularda Kaydedilmiş Oynatma Listenizi Kontrol Edin.
/deleteplaylist - Çalma listenizde kayıtlı tüm müzikleri silin
/play - Kayıtlı Oynatma Listenizi Sunuculardan oynatmaya başlayın."""


HELP_3  =  """✅<u>**Bot Komutları:**</u>
/stats - En İyi 10 Parçayı Al Global İstatistikler, Botun En İyi 10 Kullanıcısı, Botta En İyi 10 Sohbet, Sohbette Oynanan En İyi 10 vb.
/sudolist - Yukki Music Bot'un Sudo Kullanıcılarını kontrol edin
/lyrics [Müzik Adı] - Web'de belirli bir Müzik için Şarkı Sözleri arar.
/song [Parça Adı] veya [YT Bağlantısı] - youtube'dan herhangi bir parçayı mp3 veya mp4 formatında indirin.
/player - Etkileşimli bir Oynatma Paneli edinin.
**c** kanal oynatma anlamına gelir.
/queue veya /cqueue- Müzik Sırası Listesini Kontrol Edin."""

HELP_4  =  """✅<u>**Ek Komutlar:**</u>
/start - Music Bot'u başlatın.
/help - Komutların ayrıntılı açıklamalarını içeren Komutlar Yardımcı Menüsü Alın.
/ping- Bot'a ping atın ve Bot'un Ram, Cpu vb. istatistiklerini kontrol edin.
✅<u>**Grup Ayarları:**</u>
/settings - Satır içi düğmelerle tam bir grubun ayarlarını alın
🔗 **Ayarlardaki Seçenekler:**
1️⃣ Sesli sohbette yayın yapmak istediğiniz **Ses Kalitesini** ayarlayabilirsiniz.
2️⃣ Sesli sohbette yayın yapmak istediğiniz **Video Kalitesini** ayarlayabilirsiniz.
3️⃣ **Yetkili Kullanıcılar**:- Yönetici komutları modunu buradan herkese veya yalnızca yöneticilere değiştirebilirsiniz. Grubunuzda bulunan herkes yönetici komutlarını kullanabilecekse (/atla,/durdur vb.)
4️⃣ **Temiz Mod:** Etkinleştirildiğinde, sohbetinizin temiz ve iyi kalmasını sağlamak için 5 dakika sonra botun mesajlarını grubunuzdan siler.
5️⃣ **Komut Temizleme** : Etkinleştirildiğinde, Bot yürütülen komutları (/oynat, /duraklat, /karıştır, /durdur vb.) hemen siler.
6️⃣ **Oyun Ayarları:**
/playmode - Grubunuzun oynatma ayarlarını ayarlayabileceğiniz düğmeler içeren eksiksiz bir oynatma ayarları paneli edinin.
<u>Oynatma modundaki seçenekler:</u>
1️⃣ **Arama Modu** [Doğrudan veya Satır İçi] - /oynatma modu verirken arama modunuzu değiştirir.
2️⃣ **Yönetici Komutları** [Herkes veya Yöneticiler] - Grubunuzda bulunan herkes, herkes yönetici komutlarını kullanabilir (/atla, /durdur vb.)
3️⃣ **Oyun Türü** [Herkes veya Yöneticiler] - Yöneticilerse, yalnızca grupta bulunan yöneticiler sesli sohbette müzik çalabilir."""

HELP_5  =  """🔰**<u>SUDO KULLANICILARINI EKLE VE KALDIR :</u>**
/addsudo [Kullanıcı adı veya bir kullanıcıyı yanıtla]
/delsudo [Kullanıcı adı veya bir kullanıcıyı yanıtla]
🛃**<u>HEROKU:</u>**
/usage - Dyno Kullanımı.
🌐**<u> VARS YAPILANDIRMA:</u>**
/get_var - Heroku veya .env'den bir yapılandırma değişkeni alın.
/del_var - Heroku veya .env üzerindeki herhangi bir değişkeni silin.
/set_var [Var Adı] [Değer] - Heroku veya .env üzerinde bir Var ayarlayın veya Var'ı güncelleyin. Var ve Değerini bir boşlukla ayırın.
🤖**<u>YİD KOMUTLARI:</u>**
/reboot - Botunuzu yeniden başlatın.
/update - Bot'u güncelleyin.
/speedtest - Sunucu hızlarını kontrol edin
/bakım [etkinleştir / devre dışı bırak]
/logger [etkinleştir / devre dışı bırak] - Bot, logger grubundaki aranan sorguları günlüğe kaydeder.
/get_log [Satır Sayısı] - Heroku veya vps'den botunuzun günlüğünü alın. Her ikisi için de çalışır.
📈**<u>STATS KOMUTLARI:</u>**
/activevoice - Bottaki aktif sesli sohbetleri kontrol edin.
/activevideo - Botta etkin görüntülü aramaları kontrol edin.
/stats - Bot İstatistiklerini Kontrol Et
⚠️**<u>KARA LİSTE SOHBET İŞLEVİ:</u>**
/blacklistchat [CHAT_ID] - Music Bot'u kullanarak herhangi bir sohbeti kara listeye alın
/whitelistchat [CHAT_ID] - Music Bot'u kullanarak kara listeye alınmış herhangi bir sohbeti beyaz listeye alın
/blacklistedchat - Kara listeye alınmış tüm sohbetleri kontrol edin.
👤**<u>ENGELLENMİŞ İŞLEV:</u>**
/block [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcının bot komutlarını kullanmasını engeller.
/unblock [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un Engellenenler Listesinden çıkarın.
/blockedusers - Engellenen Kullanıcı Listelerini kontrol edin
👤**<u>GBAN İŞLEVİ:</u>**
/gban [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Botun sunduğu sohbette bir kullanıcıyı Gban ve botunuzu kullanmasını durdurun.
/ungban [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un gbanlı Listesinden çıkarın ve onun botunuzu kullanmasına izin verin
/gbannedusers - G Yasaklı Kullanıcı Listelerini Kontrol Et
🎥**<u>VİDEO ÇAĞRISI İŞLEVİ:</u>**
/set_video_limit [Sohbet Sayısı] - Bir seferde Görüntülü Aramalar için izin verilen maksimum Sohbet Sayısını ayarlayın. Varsayılan olarak 3 sohbet.
/videomode [download|m3u8] - İndirme modu etkinleştirilirse, Bot videoları M3u8 biçiminde oynatmak yerine indirir. Varsayılan olarak M3u8'e. Herhangi bir sorgu m3u8 modunda oynatılmadığında indirme modunu kullanabilirsiniz.
⚡️**<u>ÖZEL BOT İŞLEVİ:</u>**
/yetki [CHAT_ID] - Botunuzu kullanmak için bir sohbete izin verin.
/unauthorize [CHAT_ID] - Bir sohbetin botunuzu kullanmasına izin vermeyin.
/yetkili - Botunuzun izin verilen tüm sohbetlerini kontrol edin.
🌐**<u>YAYIN İŞLEVİ:</u>**
/broadcast [Mesaj veya Bir Mesaja Cevap Ver] - Herhangi bir mesajı Bot'un Sunulan Sohbetlerine yayınlayın.
<u>yayın seçenekleri:</u>
**-pin** : Bu, mesajınızı sabitler
**-pinloud** : Bu, mesajınızı yüksek sesli bildirimle sabitler
**-user** : Bu, mesajınızı botunuzu başlatan kullanıcılara yayınlayacaktır.
**-asistan** : Bu, mesajınızı botunuzun asistan hesabından yayınlayacaktır.
**-nobot** : Bu, botunuzu mesaj yayınlamamaya zorlar
**Örnek:** `/broadcast -user -assistant -pin Merhaba Testi`
"""
