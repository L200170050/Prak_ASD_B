def terima(x):
    voc = 0
    alfavoc = "aiueoAIUEO"
    for i in x.lower():
        if i in alfavoc:
            voc += 1
    sisa = len(x)
    print("(" + str(sisa) + ", " + str(voc) + ")")
