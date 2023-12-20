for i in range(0, 10):
  print(i)
print("These are new local changes")

def say_something(number: int, word: str) -> str:
  word = word.capitalize()
  return word * number