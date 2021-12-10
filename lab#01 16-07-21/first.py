print("Bismillah hirrahman iraheem");
# ===============linera searching programme============
# a = [44,56,77,334,54,22,24,45,31,21]
# v = int(input("enter your digit"))
# i = 0
# f = "n"
# N = len(a)
# while (i < N):
#     if( v == a[i]):
#             print ("found at position " , i)
#             f = "y"
#     i = i + 1   

# if(f == "n"):
#      print("Not found");  

# ============================sorting-method==================

a = [89,33,45,67,87,97,45,62,56,76];
v = int(input("enter your digit"))
j = 0;
N = len(a)
while (j < N):
  s = a[j];
  p = 1
  i = j + 1
while (i < N):
     if(a[i] < s):
         print("found")
      