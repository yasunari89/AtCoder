# AtCoder Codes
## Reference
https://kenkoooo.com/atcoder/?user=yasunari&kind=user

## RE(Runtime Error)の原因
- ゼロ徐算  
- 配列の範囲外アクセス  
徐算を書く時はゼロ徐算する可能性を考える。
配列を書く時はlist[i +/- j]のような時は特に範囲外アクセスの可能性を考える。

## Pythonにおける知見
### Digital Gifts
```python
money, currency = map(str, input().split())
```
入力を上記のようにすると、BTCの計算において`sum_money += 380000 * float(money)`が謎の文字列または`inf`を返してしまう。  
```python
money, currency = input().split()
```
しかしながら入力を上記のようにすると`sum_money += 380000 * float(money)`でもきちんと動くようになる。  
どちらも`type(money) = str`であり違いがよく分からない。
