def sum_up_to_n(n):
    """
    1からNまでの合計を計算する関数
    :param n: 整数
    :return: 1からNまでの合計
    """
    if n < 1:
        return 0
    return sum(range(1, n + 1))

# 使用例
N = int(input("Nを入力してください: "))
print(f"1から{N}までの合計は: {sum_up_to_n(N)}")