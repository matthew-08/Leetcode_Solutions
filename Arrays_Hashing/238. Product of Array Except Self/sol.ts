function productExceptSelf(nums: number[]): number[] {
  let pre = 1;
  let preRes: number[] = [];
  for (let i = 0; i <= nums.length - 1; i++) {
    preRes.push(pre);
    pre *= nums[i];
  }

  let post = 1;
  let postRes = Array(nums.length);
  for (let j = nums.length - 1; j >= 0; j--) {
    postRes[j] = post;
    post *= nums[j];
  }
  return postRes.map((v, i) => (v *= preRes[i]));
}
