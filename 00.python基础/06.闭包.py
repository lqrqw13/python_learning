def test(num):
   def test_in(num1):
       return(num + num1)
   return test_in

a = test(100)
print(a(200))

#def test(a,b):
#   def test_in(x):
#       print(a*x+b)
#   return test_in
#
#line1 = test(1,1)
#line1(0)
#line2 = test(10,4)
#line2(0)
#line1(0)
