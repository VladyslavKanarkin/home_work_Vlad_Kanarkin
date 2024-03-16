amount = float(input("Enter amount:"))
uah_usd = amount / 40.50
usd_uah = amount * 40.50
uah_eur = amount / 44.40
eur_uah = amount * 44.40
print(f"UAH --> USD: {uah_usd}. \n"
      f"USD --> UAH: {usd_uah}. \n"
      f"UAH --> EUR: {uah_eur}. \n"
      f"EUR --> UAH: {eur_uah}.")
