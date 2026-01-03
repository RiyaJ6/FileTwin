import hashlib
from difflib import SequenceMatcher

def hash_lib(fileName1, fileName2):
  h1 = hashlib.sha256()
  h2 = hashlib.sha256()
  with open(fileName1, "rb") as file:
    chunk = 0
    while chunk != b'':
      chunk = file.read(1024)
      h1.update(chunk)
  with open(fileName2, "rb") as file:
    chunk = 0
    while chunk != b'':
      chunk = file.read(1024)
      h2.update(chunk)
    return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_lib("fileName1", "fileName2")
if (msg1 != msg2):
  print("The files are not identical")
else:
  print("The files are identical")
