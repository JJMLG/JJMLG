function solution(ingredient) {
  let ans = 0
  const stack = []

  for (let i = 0; i < ingredient.length; i++) {
    // 햄버거를 만들 수 있는 경우는
    // ingredient[i]가 1일때 stack의 가장 최근이 123으로 쌓여 있는 경우만!
    if (ingredient[i] === 1 && stack.length >= 3) {
      const L = stack.length
      if (stack[L-1] === 3 && stack[L-2] === 2 && stack[L-3] === 1) {
        ans++
        stack.pop();stack.pop();stack.pop();
        continue
      }
    } // 나머지 경우에는 그냥 stack에 담으면 된다.
    stack.push(ingredient[i])
  }
  
  return ans
}
