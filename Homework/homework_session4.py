print("=== Factorial Calculator===")

num = int(input("\nEnter a number: "))
result = 1
print(f"\nCalculating {num}!: ")
for i in range(num ,1, -1):
    prev_result = result
    result = result * i
    # final_result= result* (i)
    print(f"{prev_result} x {i} = {result}")


print(f"\nFinal Result: {num}! = {result} ")
   
