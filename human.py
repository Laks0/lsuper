def human(n):
    for unit in ["B", "kB", "mB", "gB"]:
        if n < 1000:
            return "%3.1f %s" % (n, unit)
        n /= 1000
    return "%3.1f tB" % (n)
