# push(item) - Add an item to the top of the stack.
# pop() - Remove the top item from the stack.
# peek() - Returns a copy of the top item in the stack.
# isEmpty() - Return a boolean indicating whether or not the stack is empty.
# size() - Return the number of items in the stack.

fruit_list = ['banana', 'apple', 'plumb', 'grapes', 'peach']

#Add an item to the top of the stack
def push(fruit_list):
    var='watermelon'
    fruit_list.insert(0,var)
    print (fruit_list)

push(fruit_list)


#pop() - Remove the top item from the stack.

fruit_list = ['banana', 'apple', 'plumb', 'grapes', 'peach']
def removeTop(fruit_list):
    fruit_list.pop(0)
    print (fruit_list)

removeTop(fruit_list)

# peek() - Returns a copy of the top item in the stack.

def copy(fruit_list):
    print (fruit_list[0])

copy(fruit_list)



