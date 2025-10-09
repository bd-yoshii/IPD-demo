def hanoi(n, source, target, auxiliary):
    """
    ハノイの塔の再帰的な解法
    :param n: 移動するディスクの数
    :param source: 元の棒
    :param target: 目的の棒
    :param auxiliary: 補助の棒
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# 実行例
if __name__ == "__main__":
    num_disks = 3  # ディスクの数
    hanoi(num_disks, 'A', 'C', 'B')