# -*- coding: utf-8 -*-
"""Question 11_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1La9yDVzAIJtwaqWV_4F80Nt5n1radxOu
"""

def search(name, n1):
  for i in range(len(name)):
    if name[i]==n1:
      return True
    i+=1
    


def sorting(arr):
  n=len(arr)
  print("Array before sorting: ",arr)
  for i in range(n):
    for j in range(n-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  print("Array after sorting: ",arr)


name =('neha', 'surbhi', 'sachin', 'gaurar', 'renu', 'anisha')
arr =['neha', 'surbhi', 'sachin', 'gaurar', 'renu', 'anisha']
print("Menu \n  1.Searching \n  2.Sorting")
choice=int(input("Enter your choice"))

if choice==1:
  n1='surbhi'
  if search(name, n1):
    print("Found")
  else:
    print("Not Found")
elif choice==2:
  sorting(arr)
else:
  print("Wrong choice")