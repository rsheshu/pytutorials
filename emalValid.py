import  re

ss = '^[a-zA-Z0-9\-_]+(\.([a-zA-Z0-9\-_])+)*@[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+(\.([a-zA-Z0-9\-_])+)*'
emails = re.compile(r'^[a-zA-Z0-9\-_]+(\.([a-zA-Z0-9\-_])+)*@[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+(\.([a-zA-Z0-9\-_])+)*$')
if not emails.match("Se.h.Sesh.com"):
    print("Not matched")
else:
    print("Matched")

print(re.match(ss, "Sesh@ses.com"))
print(re.findall(ss, "Sesh@ses.com"))