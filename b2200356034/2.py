def email(your_email):
    if "@" in your_email and "." in your_email:
        return True
    else:
        return False

your_email = "b2200356034@cs.hacettepe.edu.tr"

if email(your_email):
    print(your_email, "is a valid email")
else:
    print(your_email, "is not a valid email")
