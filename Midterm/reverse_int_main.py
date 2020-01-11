from queue_llist import Queue
from stack_list import Stack

def main ():

    # (1) Initialize the number to be reversed 
    #     and a holder for the reversed number
    
    orig_num = 1234567  # original number
    rev_num = 0         # reversed number

    # (2) Create the queue and stack for this assignment
    

    stack1 = Stack()
    queue1 = Queue()

    
    # (3) Call rev_int_rec passing in the original num and the queue
    #     There is no need to return the Queue, 
    #     as the reference was passed


    rev_int_rec(orig_num, queue1)
    

    # (4) Loop through the queue:
    #     Dequeue each digit and multiply by the correct power of 10
    #     Start with the highest power of ten, use length of queue
    #     Add these terms to get the reversed number which you
    #     should store in rev_num.

    i = len(queue1) - 1
    while i != -1:
        rev_num = (queue1.dequeue() * 10**i) + rev_num
        i = i - 1



    
    
    print("Original: ", orig_num, " Reversed: ", rev_num)

    # (5) Call rev_int_stack passing in reversed number 
    #     This is the number you built in steps 3 and 4.
    #     There is no need to return the Stack, 
    #     as the reference was passed
    

    rev_int_stack(rev_num, stack1)
    

    # (6) Loop through stack:
    #     Pop each digit and multiply by the appropriate power of 10
    #     Start with the lowest power of ten
    #     Add these terms to get the original number
    for i in range(len(stack1)):
        orig_num = (stack1.pop() * 10**i) + orig_num
    
    print("Reversed: ", rev_num, " Original: ", orig_num)
    

def rev_int_stack(num, stack):
    """ 
    Using a loop:
    Remove each last digit from num using the % operator
    Add each last digit to the stack
    With each round of the loop reduce num by dividing by 10
    Base case is when num is less than 10
    """
    for i in range(len(stack)):
        new_num = num % 10
        stack.push(new_num)
        num = num // 10



    

def rev_int_rec(num, queue):
    """ 
    Remove each last digit from num using the % operator
    Add each last digit to the queue
    With each round of recursion reduce num by dividing by 10
    Base case is when num is less than 10
    """ 

    # Base case: If num < 10
    # Enqueue last digit and return
    

    new_num = num % 10
    if num < 10:
        queue.enqueue(new_num)
        return
 
    # else Not Base case:
    # Enqueue last digit and recurse
	
    else:
        queue.enqueue(new_num)
        num = num // 10
        rev_int_rec(num, queue)
    
    
main()

