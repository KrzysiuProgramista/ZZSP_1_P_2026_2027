email = input("enter your email adres: ")

username, domain = email.split("@")
print(f"username before @: {username}")

print(f"domain after @: {domain}")
