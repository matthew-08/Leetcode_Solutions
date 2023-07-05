/**
 * Definition for Node.
 * class Node {
 *     val: number
 *     next: Node | null
 *     random: Node | null
 *     constructor(val?: number, next?: Node, random?: Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */

function copyRandomList(head: Node | null): Node | null {
  const arr: Node[] = [];

  let curr = head;
  while (curr) {
    arr.push(curr);
    curr = curr.next;
  }
  const map = new Map<Node, Node>();
  const getNode = (node: Node) => {
    if (map.has(node)) {
      return map.get(node) as Node;
    } else {
      const newNode = new Node(node.val);
      map.set(node, newNode);
      return newNode;
    }
  };
  let dummy = new Node();
  let curr2 = dummy;
  for (let i = 0; i < arr.length; i++) {
    const oldNode = arr[i];
    const newNode = getNode(oldNode);
    newNode.random = oldNode.random ? getNode(oldNode.random) : null;
    newNode.next = oldNode.next ? getNode(oldNode.next) : null;
    curr2.next = newNode;
    curr2 = newNode;
  }

  return dummy.next;
}
