from mock_data import catalog

#CODES
def print_catalog_total():
   total = 0
 
   for prod in catalog:
      # print(prod["Price"])
      total = total + prod["Price"]



   print("The total of the catalog is: " + str(total))
   print(f"The total of the catalog is: {total} USD")


print_catalog_total()






#CLASS EXERCIESES

def say_hello():
   print("Hello there!")

def print_the_sum(a,b):
   print(a+b)

def print_the_division(a,b):
   # if the denominator is zero, print an error "asdasdasd"
   # else divide and print the result
   
   if b== 0:
      print("Error: division by zero not allowed")
   else: 
      print(a/b)


def print_the_cheaper(num1,num2):
   #validate whether the variables are numbers or not
   if type(num1) not in [int, float]:
      print("Error: num1 is not valid")
      return
   
   if type(num2) not in [int, float]:
      print("Error: num2 is not valid")
      return
    
   if num1 > num2:
      print(num2)
   elif num1 == num2:
      print("The numbers are same")
   
   else:
      print (num1)



def print_all_numbers():
   nums = [47,29,50,46,40,42,63,56,38,54,52,21]
   #create a for loop and print each number from the array
   for a in nums:
      print(a)

def print_the_sum():
   nums= [47,29,50,46,40,42,63,56,38,54,52,21]
   total = 0
   for n in nums:
      total += n
   print(total)

def print_the_sum_greater_than_40():
   nums= [47,29,50,46,40,42,63,56,38,54,52,21]
   total = 0
   
   for n in nums:
      if n > 40:
         total= total+n
   print(total)


def Print_how_many_numbers_lower_or_equal_to_50():
   nums= [47,29,50,46,40,42,63,56,38,54,52,21]
   counter = 0
   for n in nums:
      if n <= 50:
         counter = counter+1
   print(counter)





# say_hello()
# print_the_division(10,3)
# print_the_division(10,0)
# print_the_cheaper(34, 10)#34
# print_the_cheaper(3,100)#3
# print_the_cheaper(3,3)#They are same
# print_the_cheaper('a',100)
# print_the_cheaper(50,'b')
# print_all_numbers()
# print_the_sum()
# print_the_sum_greater_than_40()
# Print_how_many_numbers_lower_or_equal_to_50()




