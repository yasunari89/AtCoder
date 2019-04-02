# Pythonにおける知見
## Digital Gifts
```
money, currency = map(str, input().split())
```
入力を上記のようにすると、BTCの計算において`sum_money += 380000 * float(money)`が謎の文字列または`inf`を返してしまう。  
```
money, currency = input().split()
```
しかしながら入力を上記のようにすると`sum_money += 380000 * float(money)`でもきちんと動くようになる。  
どちらも`type(money) = str`であり違いがよく分からない。
