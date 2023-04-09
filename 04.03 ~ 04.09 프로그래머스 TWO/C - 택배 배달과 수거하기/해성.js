function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let d = 0;
  let p = 0;
  for (let idx = n - 1; idx >= 0; idx--) {
    let cnt = 0;
    d += deliveries[idx];
    p += pickups[idx];

    while (d >= 0 || p >= 0) {
      d -= cap;
      p -= cap;
      cnt++;
    }
    answer += (idx + 1) * 2 * cnt;
  }

  return answer;
}
