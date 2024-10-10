import random

# Kelimeleri kategorilere ayırma
nouns = [
    "aşk", "deniz", "güneş", "kalp", "hayal", "bahar", "kuş", "rüzgar", "ağaç", "yıldız",
    "gökyüzü", "toprak", "çiçek", "nehir", "gül", "dağ", "yol", "ev", "arkadaş", "dünya",
    "kitap", "kedi", "köpek", "rüya", "sevgi", "huzur", "ışık", "karanlık", "umut", "ses",
    "hayat", "zaman", "göz", "yüz", "el", "insan", "aile", "yaşam", "haber", "şehir",
    "çocuk", "bellek", "zihin", "gürültü", "su", "kumsal", "renk", "yolculuk", "film",
    "müzik", "yemek", "oyun", "hayvan", "tüy", "özlem", "dert", "hasret", "mutluluk",
    "kütüphane", "saray", "kaleler", "dükkan", "sokak", "park", "kedi", "kedi", "kedi",
    "hayvan", "yaratık", "top", "çim", "rüzgar", "yudum", "açık", "kapalı", "birlik",
    "daire", "yüzey", "kütle", "fikir", "serçe", "balık", "yıldırım", "şarkı", "düş",
    "kelime", "zaman", "birlik", "hayat", "eylem", "karar", "düşünce", "deneyim",
    "hayvan", "seçenek", "uyku", "sahne", "dağlar", "derin", "bölge", "mektup"
]

verbs = [
    "seviyor", "koşuyor", "düşünüyor", "gülüyor", "söylüyor", "uyuyor", "geliyor", "gidiyor",
    "okuyor", "yazıyor", "izliyor", "yüzüyor", "şarkı söylüyor", "gözlüyor", "düşlüyor",
    "sarılıyor", "yıkıyor", "inşa ediyor", "tutuyor", "çalışıyor", "hayal ediyor", "eğleniyor",
    "tahmin ediyor", "belirliyor", "geliştiriyor", "buluyor", "sorular soruyor", "kavrıyor",
    "yaşıyor", "hissediyor", "dinliyor", "çiziyor", "resim yapıyor", "çağırıyor",
    "paylaşıyor", "biriktiriyor", "tadıyor", "karşılaşıyor", "başarıyor", "etkileniyor",
    "kalkıyor", "kuruyor", "öğreniyor", "görüyor", "unutuyor", "fark ediyor", "düşünüyor",
    "yardım ediyor", "süreç yaşıyor", "giriyor", "çıkıyor", "yaratıyor", "özlüyor",
    "yazdırıyor", "şarkı söylüyor", "parlıyor", "konuşuyor", "katılıyor", "gelişiyor",
    "bekliyor", "hareket ediyor", "karar veriyor", "yürüyor", "çalıştırıyor",
    "katılıyor", "arzu ediyor", "hayal ediyor", "göz önüne getiriyor", "şartlar koyuyor",
    "kurtuluyor", "yetişiyor", "gerçekleştiriyor", "hatırlıyor", "destekliyor"
]

adjectives = [
    "güzel", "huzurlu", "karanlık", "büyülü", "yalnız", "umutlu", "çirkin", "tutkulu",
    "hızlı", "yavaş", "şirin", "renkli", "sakin", "heyecanlı", "üzgün", "neşeli",
    "soğuk", "sıcak", "derin", "gürültülü", "sessiz", "tatlı", "ekşi", "keskin",
    "uzun", "kısa", "geniş", "dar", "açık", "kapalı", "belirsiz", "ağır",
    "hafif", "güçlü", "zayıf", "cesur", "korkak", "zeki", "sağlam", "naif",
    "içten", "samimi", "tehlikeli", "güvenli", "yeni", "eski", "kıymetli",
    "değerli", "ilginç", "sıradan", "kapsamlı", "basit", "karışık", "büyüleyici",
    "sevimli", "hayalperest", "romantik", "duygusal", "çalışkan", "tembel",
    "şanslı", "şanssız", "hırslı", "tutkulu", "yalnız", "sosyal", "duygusal",
    "bilge", "mütevazı", "mükemmel", "şiddetli"
]

# Zarflar (Adverbs)
adverbs = [
    "hızla", "güzelce", "yavaşça", "sakin bir şekilde", "cesurca", "neşeyle",
    "yavaş yavaş", "dikkatlice", "umutla", "heyecanla", "aşkla", "kararlılıkla",
    "gizlice", "güvenli bir şekilde", "cesaretle", "merakla", "sabırla",
    "sevinçle", "uzaktan", "yakından", "doğrudan", "görerek", "duyarak",
    "gözlerimi kapatıp", "hissederek", "düşleyerek", "gerçekten", "şu anda",
    "sürekli", "geçici olarak", "birlikte", "her zaman", "çoğu zaman",
    "çokça", "azca", "hiçbir zaman", "daha fazla", "daha az", "genellikle"
]

# Şiir yapıları
structures = [
    (adjectives, nouns),  # Sıfat - İsim
    (nouns, verbs),  # İsim - Fiil
    (nouns, adverbs, verbs),  # İsim - Zarf - Fiil
    (adjectives, nouns, verbs),  # Sıfat - İsim - Fiil
    (verbs, adverbs, nouns),  # Fiil - Zarf - İsim
]


def generate_poem():
    num_lines = 5  # Dize sayısını 5 olarak ayarladık
    poem_lines = []
    for _ in range(num_lines):
        structure = random.choice(structures)  # Rastgele yapı seç
        line = []

        # Her bir yapıya göre kelime ekle
        for part in structure:
            line.append(random.choice(part))

        # Dizeyi oluştur ve uygun biçimlendirmeyi yap
        formatted_line = ' '.join(line) + '.'  # Dize sonuna nokta ekle
        poem_lines.append(formatted_line.capitalize())  # İlk harfi büyük yap

    return '\n'.join(poem_lines)


# Şiiri oluştur ve yazdır
poem = generate_poem()
print("=== Oluşturulan Şiir ===")
print(poem)