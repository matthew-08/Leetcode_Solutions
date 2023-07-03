function maxArea(height: number[]): number {
  let l = 0;
  let r = height.length - 1;

  let runningBest = 0; // edge case ?
  while (l < r) {
    const area = Math.min(height[l], height[r]) * (r - l);
    if (area > runningBest) {
      runningBest = area;
    }
    if (height[l] <= height[r]) {
      l++;
    } else {
      r--;
    }
  }
  return runningBest;
}
