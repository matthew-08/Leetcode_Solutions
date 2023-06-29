class MinStack {
  stack: number[];
  minStack: number[];
  constructor() {
    this.stack = [];
    this.minStack = [];
  }

  push(val: number): void {
    this.stack.push(val);
    if (
      !this.minStack.length ||
      this.minStack[this.minStack.length - 1] >= val
    ) {
      this.minStack.push(val);
    } else {
      this.minStack.push(this.getMin());
    }
  }

  pop(): void {
    this.stack.pop();
    this.minStack.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.minStack[this.minStack.length - 1];
  }
}
