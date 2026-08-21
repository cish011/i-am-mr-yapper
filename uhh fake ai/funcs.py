import time, random, string







def sleep(seconds) -> None:
    time.sleep(seconds)

def breeding():
    ...

def generate_string(length) -> str:
    temp = ""
    for i in range(0, length):
        temp += random.choice(string.ascii_lowercase)
    return temp

def main() -> None:
    while (True):
        sleep(0.1)
        print(generate_string(10))