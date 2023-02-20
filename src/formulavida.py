def paleitis():
    vidal = 100
    vidap = 160
    atackl = 13
    atackp = 14
    defensal = 1
    defensap = 2
    golpes = 0

    while (vidal > 0) and (vidap > 0):
        vidal -= (atackp - defensal)
        vidap -= (atackl - defensap)
        golpes += 1
    
    print (vidap, vidal, golpes)

paleitis()