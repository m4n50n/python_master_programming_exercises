def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    sec1 += hr1 * 60 * 60
    sec1 += min1 * 60

    sec2 += hr2 * 60 * 60
    sec2 += min2 * 60

    return sec2 - sec1

print(two_timestamp(1,1,1,2,2,2))
