class ListNode {
  val: number;
  constructor(val: number) {
    this.val = val;
  }
}

const map = new Map<ListNode, ListNode>();
const ok = new ListNode(3);
map.set(ok, new ListNode(2));
console.log(map);
