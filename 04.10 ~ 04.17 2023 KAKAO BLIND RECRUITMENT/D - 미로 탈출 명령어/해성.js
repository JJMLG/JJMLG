function solution(n, m, x, y, r, c, k) {
  const dir = [
    [1, 0, "d"],
    [0, -1, "l"],
    [0, 1, "r"],
    [-1, 0, "u"],
  ];
  let path = "";

  if (
    (Math.abs(x - r) + Math.abs(y - c)) % 2 !== k % 2 ||
    k < Math.abs(x - r) + Math.abs(y - c)
  ) {
    return "impossible";
  }

  while (k > 0) {
    for (let i = 0; i < 4; i++) {
      const nx = x + dir[i][0];
      const ny = y + dir[i][1];

      if (nx < 1 || ny < 1 || nx > n || ny > m) continue;

      const curDist = Math.abs(nx - r) + Math.abs(ny - c);
      if (curDist < k) {
        path += dir[i][2];
        x = nx;
        y = ny;
        k--;
        break;
      }
    }
  }

  return path;
}

// function solution(n, m, x, y, r, c, k) {
//   const maps = Array.from({ length: n }, () =>
//     Array.from({ length: m }, () => ".")
//   );
//   maps[x - 1][y - 1] = "S";
//   maps[r - 1][c - 1] = "E";

//   const dir = [
//     [1, 0],
//     [0, -1],
//     [0, 1],
//     [-1, 0],
//   ];
//   const charDir = "dlru";

//   const que = [{ nx: x - 1, ny: y - 1, cnt: 0, path: "" }];
//   let ans = "impossible";
//   const visited = Array.from({ length: n }, () =>
//     Array.from({ length: m }, () => new Set())
//   );

//   visited[x - 1][y - 1].add(0);

//   const bfs = () => {
//     while (que.length) {
//       const { nx, ny, cnt, path } = que.shift();

//       if (cnt > k) continue;

//       for (let idx = 0; idx < 4; idx++) {
//         const dx = nx + dir[idx][0];
//         const dy = ny + dir[idx][1];
//         const newCnt = cnt + 1;

//         if (dx < 0 || dy < 0 || dx >= n || dy >= m) continue;

//         if (visited[dx][dy].has(newCnt)) {
//           continue;
//         }
//         visited[dx][dy].add(newCnt);

//         const newPath = path + charDir[idx];

//         if (maps[dx][dy] === "E" && newCnt === k) {
//           if (ans === "impossible" || newPath < ans) {
//             ans = newPath;
//             return;
//           }
//         }
//         que.push({ nx: dx, ny: dy, cnt: newCnt, path: newPath });
//       }
//     }
//   };

//   bfs();
//   return ans;
// }

// function solution(n, m, x, y, r, c, k) {
//   const maps = Array.from({ length: n }, () =>
//     Array.from({ length: m }, () => ".")
//   );
//   maps[x - 1][y - 1] = "S";
//   maps[r - 1][c - 1] = "E";

//   const dir = [
//     [-1, 0],
//     [0, -1],
//     [0, 1],
//     [1, 0],
//   ];
//   const charDir = "ulrd";

//   let ans = "impossible";
//   const memo = Array.from({ length: n }, () =>
//     Array.from({ length: m }, () => Array(k + 1).fill(null))
//   );

//   const dfs = (nx, ny, cnt) => {
//     if (cnt > k) return "impossible";
//     if (nx === r - 1 && ny === c - 1 && cnt === k) return "";

//     if (memo[nx][ny][cnt] !== null) return memo[nx][ny][cnt];

//     let result = "impossible";
//     for (let idx = 0; idx < 4; idx++) {
//       const dx = nx + dir[idx][0];
//       const dy = ny + dir[idx][1];

//       if (dx >= 0 && dy >= 0 && dx < n && dy < m) {
//         const path = dfs(dx, dy, cnt + 1);
//         if (path !== "impossible") {
//           const newPath = charDir[idx] + path;
//           if (result === "impossible" || newPath < result) {
//             result = newPath;
//           }
//         }
//       }
//     }

//     memo[nx][ny][cnt] = result;
//     return result;
//   };

//   ans = dfs(x - 1, y - 1, 0);
//   return ans;
// }
