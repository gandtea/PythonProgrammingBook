# Chapter 4, Challenge 1
# Write a program that counts for the user. 
# Let the user enter the starting number, the ending number, and the amount by which to count.

start = int(input("What number should I count from: "))
end = int(input("What number should I count to: "))

while start != end:
    print(start)
    if start < end:
        start = start + 1
    if start > end:
        start = start - 1

print(end)
input('Finished! Press enter.')
