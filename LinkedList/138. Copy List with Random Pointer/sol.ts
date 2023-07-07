function generateParenthesis(n: number): string[] {
  const stack: string[] = [];
  const res = [];
  const backtrack = (closeP: number, openP: number) => {
    if (stack.length === n * 2) res.push(stack.join(''));
    console.log(closeP, openP);
    if (openP <= n) {
      stack.push('(');
      backtrack(closeP, openP + 1);
      stack.pop();
    }
    if (closeP < openP) {
      stack.push(')');
      backtrack(closeP + 1, openP);
      stack.pop();
    }
  };
  backtrack(1, 1);
  return res;
}

generateParenthesis(2);
