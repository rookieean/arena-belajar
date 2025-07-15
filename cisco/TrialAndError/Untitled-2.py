def faktorial(n):
  if n == 0:
    return 1  # Basis kasus: faktorial 0 adalah 1
  else:
    return n * faktorial(n-1)  # Kasus rekursif: panggil fungsi faktorial dengan n-1
faktorial(4)