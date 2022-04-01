#this is a python program to find the GCD of two numbers
def gcd():
  n1 = int(input("Enter First Number :"))
  n2 = int(input("Enter Second number :"))
  x = n1
  y = n2
  while(n2!=0):
    t= n2
    n2 = n1 % n2
    n1 = t
  gcd = n1
  print("GCD of {0} and   {1} = {2}".format(x,y,gcd))

#class GCD:
    #def __init__(self):
      #  self.GCD = []
    #def __call__(self, n):
      #for i in range (1, n + 1):
        # if n % i == y:
           # self.GCD.append(i)
      #return self.GCD
      
#GCD_of = GCD() 
#def testdata():
  #gcd(12)
  #gcd(100)
#def testinput():
  #while True:
      #n = int(input("What number do you want the GCD of"))
      #try:
            #n = int(n)
            #if n <= 0:
                #raise ValueError
           # print("GCD of {0} is: ".format(n))
           # print(GCD_of(n))
      #except ValueError:
            #print(f'Positive integer number is expected, got "{n}" Try again.')

#if __name__ == "__main__":
   # testinput()
#if __name__ == "__main__":
   # testdata()