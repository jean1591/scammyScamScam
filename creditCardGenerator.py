#!/usr/bin/env python

# author: garbu

from random import randint

card_types = ["visa16", "mastercard", "discover"]

def generate_card(type):  
  t = type.lower()
  if t not in card_types:
      print( "Unknown type: '%s'" % type)
      print( "Please pick one of these supported types: %s" % card_types)
      return
  
  initial, rem = prefill(t)
  so_far = initial + [randint(1,9) for x in range(rem - 1)]
  return "".join(map(str,finalize(so_far)))

def prefill(t):
  # typical number of digits in credit card
  def_length = 16
      
  if t == card_types[0]:
    # master card start with 5 and is 16 digits long
    return [5, randint(1,5)], def_length - 2
      
  elif t == card_types[1]:
    # discover card starts with 6011 and is 16 digits long
    return [6, 0, 1, 1], def_length - 4
      
  else:
    # this section probably not even needed here
    return [], def_length

def finalize(nums):
  check_sum = 0
  check_offset = (len(nums) + 1) % 2
  
  for i, n in enumerate(nums):
      if (i + check_offset) % 2 == 0:
          n_ = n*2
          check_sum += n_ -9 if n_ > 9 else n_
      else:
          check_sum += n
  return nums + [10 - (check_sum % 10) ]

""" # run - check
print(generate_card("discover"))
print(generate_card("mastercard"))
print(generate_card("visa16")) """