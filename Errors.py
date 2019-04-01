from enum import Enum

class Errors(Enum):
    reverse_variables_error = "Error: 引数の順番が逆！"
    not_int_error = "Error: 引数はint型に！"
    not_zero_and_over_error = "Error: 引数は0以上！"
