Due to the fact that this linked list is sorted, deleting duplicates becomes fairly easy. Duplicates will always follow previous nodes meaning that we don't need to keep track of duplicates in a dictionary or array like we normally would for duplicate-finding type problems.

In the case where we have a linked list like:
`1 => 1 => 1 => 2 => 3`

1. We don't need to worry about having any type of reference to our head node, as the nodes we're deleting will _always_ come after the head.
2. The duplicates are successive.

We'll set up a current variable to iterate through the linked list. If current.next is _not_ null and the value of current is equal to the value of the next node, we'll assign current.next equal to the node after current.next.
