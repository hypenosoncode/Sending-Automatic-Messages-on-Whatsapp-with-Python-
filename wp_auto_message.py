import pywhatkit as kit # Pywhatkit kütüphanesi kullanılmıştır.

try : # Dene
    kit.sendwhatmsg("+905xxxxxxxxx","Mesajınızı buraya yazın.",saat,dakika) # Dakika yazılırken başına 0 eklerseniz kod hata verecektir. Başına 0 yazmadan direkt dakikayı yazabilirsiniz.
    print("Mesaj başarılı bir şekilde gönderildi.") # Mesaj gönderme işlemi başarılı olursa bu mesajı alırsınız.
except : # Eğer olmazsa
    print("Mesaj gönderilirken bir hata meydana geldi!") # Mesaj gönderme işlemi başarısız olursa bu mesajı alırsınız.