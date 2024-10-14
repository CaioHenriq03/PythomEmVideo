def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r["maior"] = max(n)
    r['menor'] = min(n)
    r["média"] = sum(n)/len(n)


resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)