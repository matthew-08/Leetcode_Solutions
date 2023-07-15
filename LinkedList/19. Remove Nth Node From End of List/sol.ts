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

/* function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  let slowP = head;
  let fastP = head;

  for (let i = 0; i < n; i++) {
    fastP = fastP.next;
  }

  if (!fastP) return head.next;

  while (fastP.next) {
    slowP = slowP.next;
    fastP = fastP.next;
  }

  slowP.next = slowP.next.next;
  return head;
}
 */
