# 4つの数字に四則演算を使って10を作る式を求める
# 数字を permutation で列挙、記号を product で重複ありで列挙して
# eval で計算式を実行する

import itertools

def find_expression(numbers):
    operators = ['+', '-', '*', '//']
    for num_permutation in itertools.permutations(numbers):
        for op_permutation in itertools.product(operators, repeat=3):
            expression = f"{num_permutation[0]}{op_permutation[0]}{num_permutation[1]}{op_permutation[1]}{num_permutation[2]}{op_permutation[2]}{num_permutation[3]}"
            try:
                if eval(expression) == 10:
                    return expression
            except ZeroDivisionError:
                continue
    return "No valid expression found."

numbers = [1, 3, 3, 7]
result = find_expression(numbers)
print(result)

numbers = [3, 4, 7, 8]
result = find_expression(numbers)
print(result)

