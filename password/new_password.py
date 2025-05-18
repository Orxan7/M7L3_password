import random, string

def generate_password(length=12):
    letters, digits, symbols = string.ascii_letters, string.digits, string.punctuation
    pns = ["LLDDSSLLDDSS", "LDLSLDLSLDLS", "LLLDDDSSSLLL", "LDSLDSLDSLDS", "LLDDSDLLDDSD"]
    pn = random.choice(pns)
    pn += ''.join(random.choices(letters + digits + symbols, k=max(0, length - len(pn))))
    pn = pn[:length]
    pc = [random.choice(letters) if c == 'L' else random.choice(digits) if c == 'D' else random.choice(symbols) if c == 'S' else c for c in pn]
    random.shuffle(pc)
    return ''.join(pc)

print(generate_password(12))
