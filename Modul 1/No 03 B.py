def terima_kasih(x):
    kon = 0
    alfaKon = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for i in x.lower():
        if i in alfaKon:
            kon += 1
    sisa = len(x)
    print("(" + str(sisa) + ", " + str(kon) + ")")
