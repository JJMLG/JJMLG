const [N, ...INPUT] = require("fs")
  .readFileSync("./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.trim());

const nextPermutation = (el) => {
  let word = el.split("");

  let i = word.length - 1;
  let j = word.length - 1;

  // 뒤에서부터 오름차순이 끊기는 인덱스 찾기
  while (i > 0 && word[i - 1] >= word[i]) i--;

  //이미 뒤에서부터 오름차순이 끝까지 되므로 제일 뒤 문자이므로 리턴
  if (!i) return el;

  // 뒤에서부터 바꿔야할 인덱스(i-1) 값보다 큰 값 인덱스 j 찾기
  while (word[i - 1] >= word[j]) j--;

  // 스왑하고
  [word[j], word[i - 1]] = [word[i - 1], word[j]];

  //그 뒤는 어차피 오름차순이면 바로 그담 순서
  let front = word.slice(0, i).join("");
  let rear = word
    .slice(i)
    .sort((a, b) => a.charCodeAt() - b.charCodeAt())
    .join("");
  word = front + rear;

  return word;
};

INPUT.map((el) => {
  console.log(nextPermutation(el));
});
