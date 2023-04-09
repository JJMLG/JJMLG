function solution(common) {
  const sol = (b, c) => {
    let sum = b;
    for (; c > 1; c--) {
      sum *= b;
    }
    return sum;
  };
  let answer = 0;
  if (common[2] - common[1] == common[1] - common[0]) {
    answer = common[0] + common.length * (common[2] - common[1]);
  } else {
    answer = common[0] * sol(common[1] / common[0], common.length);
  }
  return answer;
}
