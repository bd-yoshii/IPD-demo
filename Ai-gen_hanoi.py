def hanoi(n, source, target, auxiliary):
    """
    ハノイの塔を解く関数
    :param n: 移動する円盤の数
    :param source: 元の棒 (出発点)
    :param target: 目的の棒 (移動先)
    :param auxiliary: 補助の棒 (中継点)
    """
    if n == 1:
        print(f"円盤 1 を {source} から {target} に移動")
        return
    # n-1個の円盤を補助棒に移動
    hanoi(n - 1, source, auxiliary, target)
    # 残りの1個を目的棒に移動
    print(f"円盤 {n} を {source} から {target} に移動")
    # 補助棒の円盤を目的棒に移動
    hanoi(n - 1, auxiliary, target, source)

# 使用例
n = int(input("円盤の数を入力してください: "))
hanoi(n, "A", "C", "B")