def computepay(Hours, Rate):
    if Hours <= 40:
        Pay= Hours * Rate
    else:
        Pay = 40 * Rate + (Hours - 40) * 1.5 * Rate
    return Pay

computepay(45, 10)

