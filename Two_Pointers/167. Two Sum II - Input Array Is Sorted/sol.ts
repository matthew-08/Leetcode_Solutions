function twoSum(numbers: number[], target: number): number[] {
  let l = 0;
  let r = numbers.length - 1;

  while (l < r) {
    const sum = numbers[l] + numbers[r];
    if (sum > target) {
      r--;
      continue;
    }
    if (sum < target) {
      l++;
      continue;
    }
    return [l + 1, r + 1];
  }
}
