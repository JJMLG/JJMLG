function solution(players, callings) {
  const charToIdx = new Map();
  const IdxToChar = new Map();
  players.map((el, idx) => {
    charToIdx[el] = idx;
    IdxToChar[idx] = el;
  });
  for (let i = 0; i < callings.length; i++) {
    const calledWord = callings[i];
    const idx = charToIdx[calledWord];
    const faster = IdxToChar[idx - 1];
    [charToIdx[faster], charToIdx[calledWord]] = [idx, idx - 1];
    [IdxToChar[idx], IdxToChar[idx - 1]] = [faster, calledWord];
  }
  return Object.values(IdxToChar);
}

function solution(players, callings) {
  const ranks = new Map();
  players.map((el, idx) => {
    ranks[el] = idx;
  });
  for (let i = 0; i < callings.length; i++) {
    const calledWord = callings[i];
    const idx = ranks[calledWord];
    const faster = players[idx - 1];
    [players[idx], players[idx - 1]] = [faster, calledWord];
    ranks[calledWord]--;
    ranks[faster]++;
  }
  return Object.entries(ranks)
    .sort((a, b) => {
      return a[1] - b[1];
    })
    .map((el) => el[0]);
}
