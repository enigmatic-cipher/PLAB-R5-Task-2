"""
Given two input lists as input. Create a new list containing all elements from both the input lists except multiples of 2 and 3.
Print this new list along with its size.
Input-> [1,2], [3,4,5]
Output-> New list size:2 
1 
5
"""

list_1= [1,2]
list_2= [3,4,5]
length_1= len(list_1)
lenght_2= len(list_2)
new_list = []
for i in range(0,length_1):
  e = list_1[i]
  if (e%2!=0 and e%3!=0):
    new_list.append(e)
for j in range(0,lenght_2):
  e_1 = list_2[j]
  if (e_1%2!=0 and e_1%3!=0):
    new_list.append(e_1)
lenght_3 = len(new_list)
print(f"New List Size:{lenght_3}")
print(new_list)