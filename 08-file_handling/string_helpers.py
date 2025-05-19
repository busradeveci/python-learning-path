def change_case(orig_string: str) -> str:
    """Değiştirilen büyük/küçük harflerle yeni bir string döndürür."""
    return orig_string.swapcase()  # Büyük harfleri küçük, küçük harfleri büyük yapar

def split_in_half(orig_string: str) -> tuple:
    """String'i ikiye böler ve sonuçları bir tuple olarak döndürür."""
    mid_index = len(orig_string) // 2  # Orta indeks
    if len(orig_string) % 2 == 0:
        return orig_string[:mid_index], orig_string[mid_index:]  # Eşit uzunlukta iki parça
    else:
        return orig_string[:mid_index], orig_string[mid_index:]  # İlk parça daha kısa

def remove_special_characters(orig_string: str) -> str:
    """Özel karakterleri kaldırarak yeni bir string döndürür."""
    return ''.join(char for char in orig_string if char.isalnum() or char.isspace())  # Harf, rakam ve boşlukları tutar 