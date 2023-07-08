function maxProfit(prices: number[]): number {
  let l = 0;
  let r = l + 1;
  let res = 0;
  let runningTotal = 0;
  let lowestNum = prices[l];
  while (r < prices.length) {
    const left = prices[l];
    const right = prices[r];
    const total = right - left;
    if (total > runningTotal) {
      runningTotal = total;
    }
    if (lowestNum > prices[r]) {
      lowestNum = prices[r];
      l = r;
    }
    r++;
  }
  return runningTotal;
}
