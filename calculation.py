# 整数のみを要素に持つリストの総和を返す関数calculation_sumを実装
numbers = [34,12,59,4]

def calculation_sum(numbers):
    total =0

    for number in numbers:
        total += number

    return total

if __name__ == '__main__':

    total = calculation_sum(numbers)

    print(total)
