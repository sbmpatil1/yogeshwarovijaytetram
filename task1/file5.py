import random

def spell_github():
  letters = ["g", "i", "t", "h", "u", "b"]
  random.shuffle(letters)
  return "".join(letters)

if __name__ == "__main__":
  print(spell_github())
