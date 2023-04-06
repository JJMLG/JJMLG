function solution(cap, n, deliveries, pickups) {
  let ans = 0
  let haveToD = 0
  let haveToP = 0
  
  for (let i = n - 1; i >= 0; i--) {
    haveToD += deliveries[i]
    haveToP += pickups[i]
    while (haveToD > 0 || haveToP > 0) {
      ans += (i + 1)
      haveToD -= cap
      haveToP -= cap
    }
  }
  return ans * 2
}
