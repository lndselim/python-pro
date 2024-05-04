meme_dict = {
            "AĞLAMAK": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" (ROFL) : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "ÜRKÜTÜCÜ" : "korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek"
            }
            
yazdırmak("Anlamlarını öğrenebileceğiniz kelimeler:", *meme_dict.Anahtar())


için ben içinde aralık(5):
    x = girdi("Hangi kelimenin anlamanı öğrenmek istersiniz?")
    x = x.Üst()
    
    eğer x içinde meme_dict.Anahtar():
        # Kelime eşleşiyorsa ne yapmalıyız?
        yazdırmak(x, "kelimesinin anlamı: ", meme_dict[x])
    başka:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        yazdırmak("Maalesef yazdığınız kelime sözlükte bulunmamaktadır!"
