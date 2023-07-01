/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

/**
 Do not return anything, modify head in-place instead.
 */
function reorderList(head: ListNode | null): void {
  // find middle
  // reverse the part after middle
  // remove the cycle from the middle
  // merge the first side with the second reversed side;

  let slow = findMiddle(head); //
  let head2 = reverse(slow.next); //
  slow.next = null; // to prevent cycle after reversing

  merge(head, head2); //
}

function findMiddle(head: ListNode | null): ListNode | null {
  let slow = head; //
  let fast = head; //

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast?.next?.next;
  }
  return slow;
}
function reverse(head: ListNode | null): ListNode | null {
  let previous = null;
  let current = head;

  while (current) {
    let next = current.next;
    current.next = previous;
    previous = current;
    current = next;
  }
  return previous;
}

function merge(headA: ListNode | null, headB: ListNode | null) {
  while (headB) {
    let next = headA.next;
    headA.next = headB;
    headA = headB;
    headB = next;
  }
}
