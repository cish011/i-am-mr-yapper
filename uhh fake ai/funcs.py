import time, random, string, breed

strings = breed.strings





def sleep(seconds) -> None:
    time.sleep(seconds)

def breeding() -> None:
    breed_pool = []
    offspring = []
    for i in range(0,int(len(strings)/2)):
        breed_pool.append(strings.pop(0))
        breed_pool.append(strings.pop(0))
        offspring.append(breed_pool[0][:int(len(breed_pool[0])/2)] + breed_pool[1][int(len(breed_pool[1])/2):len(breed_pool[1])])
        offspring.append(breed_pool[0][int(len(breed_pool[0])/2):len(breed_pool[0])])
        ...


def generate_string(length) -> None:
    for i in range(0,20):
        temp = ""
        for i in range(0, length//2*2):
            temp += random.choice(string.ascii_lowercase)
        strings.append(temp)
    

