def infinite_numbers(start=0):  #Generators are great because the code is simpler, but it will give you the same output as complex class functions, and also saves memory space since it uses iterators.
    while True:         
        yield start  #Generators use the keyword "yield" instead of "return", which will iterate over a sequence, but does not store the entire sequence in memory (saving memory space)
        start += 1

my_gen = infinite_numbers()  #returns a *generator* object.
print(my_gen)  
print(dir(my_gen)) #call "dir" will find that it contains __iter__ and *__next__* methods and so on.

for num in infinite_numbers(1): #Technically, generators does not "execute" or print alone, but one can use a foor loop like this and print the outup of the generator.
    print(num, end=" ")
    if num > 20: #
        break  #The break point puts and end the "infinite numbers" while loop. 
        
