def human(n, binary):
    table = ["", "K", "M", "G"]
    inc = 1000
    if binary:
        table = ["", "Ki", "Mi", "Gi"]
        inc = 1024
    for unit in table:
        if n < inc:
            return "%3.1f %sB" % (n, unit)
        n /= inc
    return "%3.1f %sB" % (n, "Ti" if binary else "T")
