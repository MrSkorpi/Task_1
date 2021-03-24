m = input("Введите фразу на английском: ")
print("a", *map(m.lower().count, "a"),
      "e", *map(m.lower().count, "o"),
      "i", *map(m.lower().count, "a"),
      "o", *map(m.lower().count, "a"),
      "u", *map(m.lower().count, "u"),
      "y", *map(m.lower().count, "y"))