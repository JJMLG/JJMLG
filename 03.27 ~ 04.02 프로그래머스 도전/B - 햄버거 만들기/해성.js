function solution(ingredient) {
  let answer;
  let stack = [];
  for (let i = 0; i < ingredient.length; i++) {
    stack.push(ingredient[i]);
    if (stack[stack.length - 1] === 1 && stack.length >= 3) {
      let flag = 0;
      for (
        let idx = 1, j = stack.length - 1 - 3;
        j <= stack.length - 1;
        j++, idx = (idx % 3) + 1
      ) {
        if (stack[j] != idx) break;
        flag++;
      }
      if (flag === 4) {
        while (flag--) {
          stack.pop();
        }
      }
    }
  }
  answer = (ingredient.length - stack.length) / 4;
  return answer;
}
