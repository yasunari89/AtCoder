| 計算量       | Python         |
| ------------ | -------------- |
| O(1e5) / sec | 余裕で間に合う |
| O(1e6) / sec | 多分間に合う   |
| O(1e7) / sec | かなり厳しい   |

| 処理     | 計算量 |
| -------- | ------ |
| `pop()`  | O(1)   |
| `pop(i)` | O(n)   |

| Runtime Error              | 解決                                     |
| -------------------------- | ---------------------------------------- |
| ゼロ徐算                   |                                          |
| 配列の範囲外アクセス       |                                          |
| 再帰関数の再起制限回数超え | `sys.setrecursionlimit(10**8)`などと設定 |