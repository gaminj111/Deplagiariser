import time

with open("initial.txt") as f:
    initial1 = f.read()
    transfer1 = initial1.replace("a", "а")
    transfer2 = transfer1.replace("c", "с")
    transfer3 = transfer2.replace("h", "h")
    transfer4 = transfer3.replace("e", "е")
    time.sleep(0.5)
    transfer5 = transfer4.replace("i", "і")
    transfer6 = transfer5.replace("j", "ј")
    transfer7 = transfer6.replace("o", "ο")
    transfer8 = transfer7.replace("p", "р")
    time.sleep(0.5)
    transfer9 = transfer8.replace("x", "х")
    transfer10 = transfer9.replace("y", "y")
    transfer11 = transfer10.replace("o", "ο")
    transfer12 = transfer11.replace("p", "р")
    time.sleep(0.5)

with open("after.txt", "w", encoding="utf-8") as g:
    g.write(transfer12)