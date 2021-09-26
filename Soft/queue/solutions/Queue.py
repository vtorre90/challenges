# enqueue(item) - adds an item to the queue
# dequeue() - removes an item from the queue (FIFO)
# peek() - returns the next item in the queue without removing it
# isEmpty() - tests to see whether the queue is empty
# size() - returns the number of items in the queue

#array declaration
fruit_list = ['banana', 'apple', 'plumb', 'grapes', 'peach']
nr_list = [4, 6, 5, 1, 9]


#adds an item to the queue
print('ADDING ITEM TO THE LIST')
extra_fruit = 'apricot'
fruit_list.append(extra_fruit)
print(fruit_list)

#removes an item from the queue (FIFO) 
print ('REMOVING ITEM FROM THE LIST')
nr_list.remove(5)
del fruit_list [-2]
print(nr_list)
print(fruit_list)

#returns the next item in the queue without removing it

#tests to see whether the queue is empty

empty_string = ''

print ('CHECKING IF STRINGS ARE EMPTY')
if (len(fruit_list))==0:
    print ('The fruit string is empty')
else :
    print ('The fruit string is not empty:' .join(fruit_list))

if (len(empty_string))==0:
    print('The empty string is empty')
else:
    print('The empty string is not empty')


#returns the number of items in the queue
print ('CHECKING THE SIZE OF ARRAY')
print(len(fruit_list))


