#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Fincanında Gelecek Gören Yapay Zeka
Tamamen bilimsel, %100 doğru, asla yanılmaz.
"""

import random
import time

def fincani_oku():
    print("\n🍵 Fincanınız inceleniyor... Lütfen 3 saniye bekleyin.")
    time.sleep(3)
    
    sekiller = [
        "bir kedi", "ters dönmüş kedi", "çok sinirli kedi",
        "uçan balık", "yürüyen balık", "felsefe yapan balık",
        "para", "çok para", "hiç para", "borç para",
        "kalp", "kırık kalp", "kalp atışı yapmayan kalp",
        "yol", "çıkmaz yol", "asla bitmeyen yol",
        "kuş", "ters uçan kuş", "uçmayı unutmuş kuş"
    ]
    
    yorumlar = [
        "Yakında büyük bir sürpriz sizi bekliyor. Muhtemelen market kuyruğu.",
        "Aşk hayatınızda yeni bir sayfa açılacak. Sayfa numarası 404.",
        "Para geleceği görüyorum. Ama başkasının parası.",
        "Kariyerinizde büyük bir adım atacaksınız. Adımın boyu 3 cm.",
        "Sağlık konusunda dikkatli olun. Özellikle çay kaşığına dikkat.",
        "Gelecekte çok mutlu olacaksınız. Ama şimdi değil, çok sonra. Belki 2087'de.",
        "Bir yolculuk sizi bekliyor. Muhtemelen otobüs durağına.",
        "Fincanınız diyor ki: 'Daha çok kahve iç.'",
        "Kaderiniz şu anda başka bir fincanda. Bu fincan yedek."
    ]
    
    sekil = random.choice(sekiller)
    yorum = random.choice(yorumlar)
    
    print(f"\n🔮 Fincanınızda {sekil} görüldü!")
    print(f"💬 Yorum: {yorum}")
    print("\nNot: Bu fal %100 doğrudur. Yanılırsa fincanın suçu.")

if __name__ == "__main__":
    print("=" * 50)
    print("   KAHVE FINCANINDA GELECEK GÖREN YAPAY ZEKA v1.0")
    print("=" * 50)
    fincani_oku()
    print("\n✨ Fal tamamlandı. Başka bir fincan için programı tekrar çalıştırın.")
