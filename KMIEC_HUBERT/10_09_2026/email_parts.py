# Operator / wykonuje standardowe dzielenie zmiennoprzecinkowe (np. 10 / 4 daje wynik 2.5).
# Operator // to dzielenie calkowite, ktore odrzuca ułamek i zaokragla w dol (np. 10 // 4 daje wynik 2).

skrzynka_mail = input("Wprowadz adres e-mail: ")

login_user, _, domena_serwera = skrzynka_mail.partition("@")

print("Przed @:", login_user)
print("Po @:", domena_serwera)
