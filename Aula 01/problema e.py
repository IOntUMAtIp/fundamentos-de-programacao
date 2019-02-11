total = int(input())

anos = int(total / 365)
meses = int((total / 30) / 12)
dias = int((total % 365) % 30)
print('%d ano(s)' % anos)
print('%d mes(es)' % meses)
print('%d dia(s)' % dias)

