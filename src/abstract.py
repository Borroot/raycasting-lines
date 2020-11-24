def maps(value, l1, r1, l2, r2):  # map value in range [l1,r1] to [l2,r2]
    inverse = False
    if l2 > r2:
        tmp = l2
        l2 = r2
        r2 = tmp
        inverse = True

    lspan, rspan = r1 - l1, r2 - l2
    value = (value - l1) / lspan
    value = value * rspan
    return l2 + value if not inverse else r2 - value
