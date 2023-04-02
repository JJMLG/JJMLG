function solution(common) {
  const last = common.length - 1
  if (common[1] - common[0] === common[2] - common[1]) {
      return common[last] + common[1] - common[0]
  }
  return common[last] * (common[1] / common[0])
}