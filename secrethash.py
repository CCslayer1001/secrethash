def sesli_harf_mi(harf):
    sesli_harfler = "aeiouAEIOU"
    return harf in sesli_harfler

def ters_siradaki_harf(harf):
    if harf.isalpha():
        alfabe = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        index = alfabe.index(harf)
        return alfabe[::-1][index]
    else:
        return harf

def encrypt(metin):
    sifrelenmis_metin = ""
    for harf in metin:
        if harf == ' ':
            sifrelenmis_metin += ' '
        elif sesli_harf_mi(harf):
            sifrelenmis_metin += "1" + ters_siradaki_harf(harf)
        else:
            sifrelenmis_metin += "0" + ters_siradaki_harf(harf)

    return sifrelenmis_metin

metin = ''''''

def decrypt(sifrelenmis_metin):
    orijinal_metin = ""
    i = 0
    while i < len(sifrelenmis_metin):
        if i + 1 < len(sifrelenmis_metin):
            if sifrelenmis_metin[i] == "1":
                orijinal_metin += ters_siradaki_harf(sifrelenmis_metin[i + 1])
                i += 2
            elif sifrelenmis_metin[i] == "0":
                orijinal_metin += ters_siradaki_harf(sifrelenmis_metin[i + 1])
                i += 2
            elif sifrelenmis_metin[i] == ' ':
                orijinal_metin += ' '
                i += 1
            elif sifrelenmis_metin[i] == '//':
                orijinal_metin += '\n'
                i += 1
            else:
                orijinal_metin += sifrelenmis_metin[i]
                i += 1
        else:
            orijinal_metin += sifrelenmis_metin[i]
            i += 1
    
    return orijinal_metin

sifrelenmis_metin = rf'''
'''
