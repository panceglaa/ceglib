

def findlinewithword(file, word):
    with open(file) as f2:
      for line in f2.readlines():
        if word in line:
          return line
      f2.close()


def findnumbiggerthan(num, numlist):
  for num2 in numlist:
    if num2 > num:
      return num2


def fileexists(file):
  
  # checks if file exists without module
  try:
    with open(file) as f2:
      f2.close()
  except (OSError, ValueError):
    return False
  return True

