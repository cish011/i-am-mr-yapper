class strings_i_guess:
    strings = []
    @staticmethod
    def make(name): 
        strings_i_guess.strings.append(name)

print(strings_i_guess.strings)
strings_i_guess.make("heksjflksdfkj")
print(strings_i_guess.strings)
