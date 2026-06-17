class Solution:
   def fizzBuzz(self, n: int) -> list[str]:
       result = []
       for num in range(1, n + 1):
           if num % 15 == 0: # divisible by both 3 and 5
               result.append("FizzBuzz")
           elif num % 3 == 0: # divisible by 3
               result.append("Fizz")
           elif num % 5 == 0: # divisible by 5
               result.append("Buzz")
           else: # not divisible by 3 or 5
               result.append(str(num))
       return result