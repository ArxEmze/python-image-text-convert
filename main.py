# Kütüphaneler Bölümü
import cv2  #Görüntü işleme fonksiyonlarını sağlar.
import pytesseract  #Tesseract OCR (Optik Karakter Tanıma)
import os  #Dosya ve dizin işleme için kullanılıyor.

# Tesseract'in kurulu olduğu yolu belirtiyoruz.
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# Görüntüyü metine dönüştüren fonksiyon.
def image_to_text(image_path, lang='eng'):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Görüntü dosyası bulunamadı: {image_path}")
    
    # Görüntüyü yükle
    image = cv2.imread(image_path)
    
    if image is None:
        raise ValueError(f"Görüntü dosyası yüklenemedi: {image_path}")

    # Görüntüyü gri tonlamaya çevir
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # İsteğe bağlı: Görüntüyü bulanıklaştırma
    gray_image = cv2.medianBlur(gray_image, 3)
    
    # İsteğe bağlı: Görüntüye eşikleme uygulama
    _, gray_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Tesseract ile metin tanıma
    text = pytesseract.image_to_string(gray_image, lang=lang)
    
    return text

if __name__ == "__main__":
    
    # Kullanıcıdan görüntü dosyasının yolunu al
    image_path = input("Lütfen görüntü dosyasının yolunu girin: ")

    # Kullanıcıdan kullanmak istediği dili al
    lang = input("Lütfen dil kodunu girin (varsayılan: 'eng' - İngilizce): ")
    
    # Varsayılan dil kodunu 'eng' olarak ayarla
    if not lang:
        lang = 'eng'
    
    try:
        text = image_to_text(image_path, lang=lang)
        print("Görüntüden elde edilen metin:")
        print(text)
    except Exception as e:
        print(f"Hata: {e}")
