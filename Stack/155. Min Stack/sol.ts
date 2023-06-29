function dailyTemperatures(temperatures: number[]): number[] {
  const stack: [number, number][] = [];
  //[temp, index]
  const result = Array(temperatures.length).fill(0);

  for (let i = temperatures.length - 1; i <= 0; i--) {
    if (!stack.length) {
      result[i] = 0;
    } else {
      let val = stack.pop();
      while (stack.length > 1 && val < temperatures[i]) {
        val = stack.pop();
      }
      if (stack.length === 1) {
        result[i] = 0;
      } else {
        result[i] === temperatures[1] - val[1];
      }
      stack.push(val);
    }
    stack.push([temperatures[i], i]);
  }
  console.log(result);
}

dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]);
