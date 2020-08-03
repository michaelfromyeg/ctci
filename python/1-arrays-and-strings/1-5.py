# One Away: check if two strings are one or zero edits away
# NB: an edit is insert, remove, or replace

def one_away(a: str, b: int) -> bool:
  for c in a:
    if c in b:
      a = a.replace(c, '')
      b = b.replace(c, '')
  if len(a) <= 1 and len(b) <= 1:
    return True
  return False

assert one_away('', ' ') == True
assert one_away('pale', 'ple') == True
assert one_away('pales', 'pale') == True
assert one_away('pale', 'bale') == True
assert one_away('pale', 'bake') == False
assert one_away('pale', 'pale') == True
assert one_away('ple', 'pale') == True
assert one_away('paale', 'ple') == False

