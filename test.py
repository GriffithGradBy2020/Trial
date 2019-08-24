import re
def same(item, target):
  """
  Function that determines the amount of matching letters from current word to target
  :param item: item is the current word being compared
  :param target: is the desired word to be changed to
  :return: returns an integer value that is the amount of matching letters
  """
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  """
  Fucntion builds a list to match pattern
  :param pattern: The pattern in which the list is assembled
  :param words: Words from the dictionary
  :param seen: Words previously seen and to be discarded
  :param list: list of current potential words to be put in path
  :return: Returns a built list to be used to find path
  """
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(start, words, seen, target, path):
  """
  Function finds path from word to target optimally
  :param start: first word in path
  :param words: words from dictionary
  :param seen: previously tested words from dictionary
  :param target: desired outcome of path
  :param path: pathway of words from start to target
  :return: True or False adding words to seen dictionary
  """
  list = []
  compatible = []
#checks if the sum of compatible letters from item to target are over 0, removing unnecessary words
  if (sum(1 for (c, t) in zip(start, target) if c == t)) > 0:
    compatible = [i for i, x in enumerate(zip(start, target)) if all(y == x[0] for y in x)]

  for i in range(len(start)):
    if i not in compatible:
      list += build(start[:i] + "." + start[i + 1:], words, seen, list)

  if len(list) == 0:
    return False
#reversing the sorted list gives words closest to target, improving efficiency
  list = sorted([(same(w, target), w) for w in list])
  list.reverse()

#checks if the current word being tested is 1 letter away from target, meaning task completed
  for (match, item) in list:
    if match >= len(target) -1:
      if match == len(target) - 1:
        path.append(item)
        return True
    seen[item] = True

  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()


def fileInput(initial):
  """
  Function attempts to open text file
  :param initial: name of text file to be opened
  :return: variable storing text file
  """
  fileIsReal = False
  while fileIsReal is False:
    try:
      file = open(initial)
      fileIsReal = True
      return file
    except FileNotFoundError:
      print("Not a file.")
      initial = input("Enter dictionary name:\nOr enter quit to exit program: ")
      if initial=="quit":
        exit()





def startInput(start):
  """
  Function validates start input
  :param target: start word entered via input
  :return: True or False if input is valid
  """

  start.lower()

  for i in range(len(start)):
    if start[i]==" ":
      return False

  if start.isalpha() is False:
    return False
  else:
    return True



def targetInput(target):
  """
  Function validates target input
  :param target: target word entered via input
  :return: True or False if input is valid
  """
  target.lower()
  for i in range(len(target)):
    if target[i] == " ":
      return False

  if target.isalpha() is False:
    return False
  else:
    return True


def matchingInput(start,target):
  """
  Function confirms matching length of start and target
  :param start: Start word entered via input
  :param target: Target word entered via input
  :return: True or False if matching
  """
  if len(start) == len(target):
    return True
  else:
    return False



initial = input("Enter File name: ")
file = fileInput(initial)
lines = file.readlines()
initialStart = input("Enter start word:")
initialTarget = input("Enter target word:")
if startInput(initialStart)==True and targetInput(initialStart)==True and matchingInput(initialStart,initialStart)==True:
  start = initialStart
  target = initialTarget
else:
  print("Error in input.")
  exit()
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

  file.close()