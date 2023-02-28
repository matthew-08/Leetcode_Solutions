## Explanation

The crux of this problem is using 'carry' numbers from basic elementary long addition.

It's important to note that long addition is done from right to left. Meaning that whenever we add two numbers like:
999

- 99
  We start from the end and work our way left as we add each column.

In this problem, that fact makes the reversed link list reasonable.

## 2 -> 0 -> 1

2 -> 0 -> 1

Here, the numbers they want us to add are reversed. The result we want is 102 + 102. Since we're performing simulated
long addition here, it works perfect as we can just add from the end to the beginning just as we would with long addition.
This also makes our result easy to ouput as we can simply output the numbers as we go and they'll already be in "reversed"
order.

## Solution

In the solution, we start by using a dummy node to keep track of the head of our new list that we'll return at the end.
Then, we declare a `current` variable which will serve as our pointer for the returned list.
Similary, we declare two `curr` variables which serve as pointers for the two lists we're adding.
We have a `carryNum` variable which will serve as a holder for our carried numbers.

```
        dummy = ListNode()
        curr = dummy
        curr1 = l1
        curr2 = l2
        carryNum = 0
```

Our while loop has 3 conditions: 1. While list 1 is still intact. 2. While list 2 is still intact. 3. While our carry variable still holds a number. This is intended to counteract the edge case
in which we may "finish" adding but still have some carry number left over to add in.

`while curr1 or curr2 or carryNum`
