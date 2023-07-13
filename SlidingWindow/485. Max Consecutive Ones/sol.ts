function findMaxConsecutiveOnes(nums: number[]): number {
  let left = 0;
  let right = 0;

  let best = 0;

  while (right < nums.length) {
    if (nums[right] === 0) {
      left = right + 1;
    }
    best = Math.max(right - left + 1, best);
    right++;
  }
  /* return best; */
}
