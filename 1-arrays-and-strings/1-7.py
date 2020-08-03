# Rotate Matrix: rotate an NxN matrix by 90 deg
# TODO: do this in place

from array import *

def rotate_matrix(m: [[]]) -> [[]]: # Not sure if it's possible to enforce 2D int array
  if (len(m) <= 1):
    return m
  new = [[0]*len(m)]*len(m)
  print('1 ====')
  for i, r in enumerate(m): # for each row
    for j, c in enumerate(r): # for each cell
      new[j][len(m) - 1 - i] = c
      print(j,len(m) - 1 - i, new[j][len(m) - 1 - i])
  print('2 ====')
  for i, r in enumerate(new): # for each row
    for j, c in enumerate(r): # for each cell
      print(i,j,new[i][j])
  return new

def check(m: [[]], n: [[]]) -> bool:
  for i, r in enumerate(m): # for each row
    for j, c in enumerate(r): # for each cell
      if (m[i][j] != n[i][j]):
        print(i,j, m[i][j], n[i][j])
        return False
  return True

assert check(rotate_matrix([[]]), [[]]) == True
assert check(rotate_matrix([[0,1,2],[3,4,5],[6,7,8]]), [[6,3,0],[7,4,1],[8,5,2]]) == True 
