import time, random, string, breed

strings = breed.strings





def sleep(seconds) -> None:
    time.sleep(seconds)

def breeding():
    ...

def generate_string(length) -> None:
    for i in range(0,20):
        temp = ""
        for i in range(0, length):
            temp += random.choice(string.ascii_lowercase)
        strings.append(temp)
    

