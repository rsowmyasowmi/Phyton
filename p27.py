str='b123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\nNot numeric')
print()
