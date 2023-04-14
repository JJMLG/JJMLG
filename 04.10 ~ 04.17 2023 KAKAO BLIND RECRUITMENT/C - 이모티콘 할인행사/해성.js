function solution(users, emoticons) {
  let result = [0, 0];

  const ratios = Array.from({ length: emoticons.length }, () => 0);
  let calc = () => {
    let signCnt = 0;
    let totalVal = 0;

    users.forEach((el) => {
      let tempsum = 0;
      for (let idx = 0; idx < ratios.length; idx++) {
        if (ratios[idx] >= el[0]) {
          tempsum += (emoticons[idx] * (100 - ratios[idx])) / 100;
        } else continue;
      }
      if (tempsum >= el[1]) {
        signCnt++;
      } else totalVal += tempsum;
    });
    return [signCnt, totalVal];
  };
  const dfs = (dep) => {
    if (dep === emoticons.length) {
      const [signCnt, totalVal] = calc();
      if (signCnt > result[0]) result = [signCnt, totalVal];
      else if (signCnt === result[0] && totalVal > result[1])
        result = [signCnt, totalVal];
      return;
    }
    for (let val = 10; val <= 40; val += 10) {
      ratios[dep] = val;
      dfs(dep + 1, val);
      ratios[dep] = 0;
    }
  };
  dfs(0);
  return result;
}
