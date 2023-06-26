function topKFrequent(nums: number[], k: number): number[] {
  // hash map to store freq
  const map = new Map<number, number>();

  nums.forEach((num) => {
    map.set(num, map.get(num) + 1 || 1);
  });

  const entries = [...map.entries()];

  return entries
    .sort((a, b) => b[1] - a[1])
    .map((v) => v[0])
    .slice(0, k);
}
