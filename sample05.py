# 2つの整数の和を返す関数addを作る

def add(a: int, b: int) -> int:
    return a + b


def diff(a: int, b: int) -> int:
    return a - b


if __name__ == '__main__':
    y = add(a=3, b=4)
    print(y)  # ここで7が出力されればok

    # 2つの整数の差を返す関数を定義

    y2 = diff(a=3, b=4)
    print(y2)
