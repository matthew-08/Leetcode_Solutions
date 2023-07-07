function longestSubarray(nums: number[]): number {
  let left = 0;
  let right = 0;

  let best = 0;
  let deletedZero = false;

  while (right < nums.length) {
    if (nums[right] === 0) {
      if (deletedZero) {
        while (deletedZero) {
          if (nums[left] === 0) {
            deletedZero = false;
          }
          left++;
        }
      }
      deletedZero = true;
    }
    best = Math.max(right - left, best);
    right++;
  }
  return best;
}
