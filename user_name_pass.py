import hashlib

username_pass = {}

def signup(username, password):
    global username_pass
    password_hash = hashlib.sha256(str(password).encode()).hexdigest()
    username_hash = hashlib.sha256(str(username).encode()).hexdigest()
    username_pass[username_hash] = password_hash
    return None

def login(username, password):
    global username_pass
    username_hash = hashlib.sha256(str(username).encode()).hexdigest()
    password_hash = hashlib.sha256(str(password).encode()).hexdigest()

    if username_pass.get(username_hash) == password_hash:
        print("logged in")
    else:
        print("Incorrect username password")



signup("leena", "akshatpass")
signup("akshat", "leenapass")


login("akshat", "leenapass")