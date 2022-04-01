  
class Factors:
    def __init__(self):
        self.factors = []
    def __call__(self, n):
      for i in range (1, n + 1):
        if n % i == 0:
            self.factors.append(i)
      return self.factors
      
factors_of = Factors() 
def tester():
  while True:
      n = int(input("What number do you want to find the factor of?"))
      try:
            n = int(n)
            if n <= 0:
                raise ValueError
            print("Factors of {0} is: ".format(n))
            print(factors_of(n))
      except ValueError:
            print(f'Positive integer number is expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()