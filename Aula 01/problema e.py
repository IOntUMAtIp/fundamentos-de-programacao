total = int(input())

anos = total / 365
meses = (total / 30) % 12
dias = (total % 365) % 30
print('%d ano(s)' % anos)
print('%d mes(es)' % meses)
print('%d dia(s)' % dias)
