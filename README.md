# AtCoder Codes
## Reference
https://kenkoooo.com/atcoder/?user=yasunari&kind=user

## RE（Runtime Error）の原因
- ゼロ徐算  
- 配列の範囲外アクセス  

徐算を書く時はゼロ徐算する可能性を考える。  
配列を書く時は（list[i +/- j]のような時は特に）範囲外アクセスの可能性を考える。

## 桁DP
桁DPの問題はだいたい制約がクソでかいことが多いので解法の当てがつきやすく、わかりやすい。  
満たす条件により分類することで分類されたものを同一視する。  
(ex) N以下の自然数のうち各桁の数の総和がDであるような数の個数  
pattern1:  
- 今まで何桁見てきたか  
  1134***, 1242***, ...: どれも残り4桁&桁和9  

pattern2:  
- 今見ている桁の自由度  
  210***, 211***, ...: 4桁目の自由度は0-9  
  214***: 4桁目の自由度は0-5  
  215***, ...: 4桁目の自由度はなし  

http://luzhiled.hatenablog.com/entry/2017/12/03/124453

## Pythonにおける知見
### 実行時間制限とOrder
- O(1e5)/sec: 余裕を持って間に合う  
- O(1e6)/sec: おそらく間に合う  
- O(1e7)/sec: 非常にシンプルな処理でない限り難しい

## zfill
右寄せゼロ埋め: `string.zfill(size)`

### indexの所得方法
例えば`list_a`の最大値を取るインデックスを取得したい時  
```python
max_index = list_a.index(max(list_a))
```
とすると速い。

### ABC119: Digital Gifts
```python
money, currency = map(str, input().split())
```
入力を上記のようにすると、BTCの計算において`sum_money += 380000 * float(money)`が謎の文字列または`inf`を返してしまう。  
```python
money, currency = input().split()
```
しかしながら入力を上記のようにすると`sum_money += 380000 * float(money)`でもきちんと動くようになる。  
どちらも`type(money) = str`であり違いがよく分からない。
