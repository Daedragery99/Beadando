import regex as r
def email_ellenorzo():
    email = ""
    k = True
    while email != "0":
        email = input("Adja meg az email címét: ").lower()
        for idx in range(len(email)):
            if email[idx] == '.' and email[idx-1] == '.' or email[-1] == '.' or email[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                k = None
                break
        emails = r.match('^[a-z0-9][a-z0-9-._]+[a-z0-9]+@[a-z0-9-.]+\.[a-z]+', email)
        if email == "0":
            break
        if emails and k:
            print("Helyes email!")
        else:
            print("Helytelen email!")
            k = True


email_ellenorzo()
