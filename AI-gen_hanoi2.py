def hanoi(n, source, target, auxiliary):
    """
    ハノイの塔のアルゴリズム。
    :param n: 移動するディスクの枚数
    :param source: 移動元の棒
    :param target: 移動先の棒
    :param auxiliary: 補助の棒
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    # n-1枚を補助棒に移動
    hanoi(n - 1, source, auxiliary, target)
    # 最後のディスクを移動先棒に移動
    print(f"Move disk {n} from {source} to {target}")
    # n-1枚を補助棒から移動先棒に移動
    hanoi(n - 1, auxiliary, target, source)

# 例: 3枚のディスクで遊ぶ
number_of_disks = 3
hanoi(number_of_disks, 'A', 'C', 'B')