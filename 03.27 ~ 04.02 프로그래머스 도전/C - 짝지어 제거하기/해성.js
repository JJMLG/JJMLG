function solution(s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (stack.length > 0 && stack[stack.length - 1] == s[i]) {
      stack.pop();
    } else {
      stack.push(s[i]);
    }
  }
  return stack.length > 0 ? 0 : 1;
}
