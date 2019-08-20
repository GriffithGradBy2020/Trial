import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  list.reverse()
  for (match, item) in list:
    if match >= len(target) -1:
        path.append(item)
        return True
    seen[item] = True

  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()


def fileInput():
  fileIsReal = False
  while fileIsReal is False:
    initial = input("Enter dictionary name: ")
    try:
      file = open(initial)
      fileIsReal = True
      return file
    except FileNotFoundError:
      print("Not a file. Input a correct file")


def valueInput():
  inputCorrect = False
  while inputCorrect is False:
    start = input("Enter start word:")
    target = input("Enter target word:")
    #print((len(start) == len(target)))
    if (len(start) == len(target)) is False:
      print("Needs same length words")
    if start.isalpha() == False or target.isalpha() == False and (len(start) == len(target)) is True:
      print("needs alphabetical letters")
    else:
      inputCorrect = True

  return start , target


file = fileInput()
lines = file.readlines()
start, target = valueInput()
words = []
for line in lines:
  word = line.rstrip()
  if len(word) == len(start):
    words.append(word)


path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")