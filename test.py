import re
def same(item, target):
  #print(item, target)
  return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, list):
  #print(pattern)
  return [word for word in words
                 if re.match(pattern, word) and word not in seen.keys() and
                    word if not list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
    #print(list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])

  for (match, item) in list:
    if match >= len(target) - 1 and match == len(target) - 1:
        if match < len(target):
          path.append(item)
        #use another list instead of path
        return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

def initInput():
  temp = True
  while temp is True:
    initial = input("Enter dictionary name: ")
    try:
      file = open(initial)
      temp = False
      return file
    except FileNotFoundError:
      print("Not a file. Input a correct file")


file = initInput()
lines = file.readlines()
start = input("Enter start word:")
words = []
for line in lines:
  word = line.rstrip()
  if len(word) == len(start):
    words.append(word)
target = input("Enter target word:")

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

