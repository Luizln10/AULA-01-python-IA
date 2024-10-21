for numero in range(2, 20):
  for i in range(2, numero):
    if numero % i == 0:
      break
  else:
    print(f"{numero} é um número primo")