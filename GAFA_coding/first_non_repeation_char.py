# return char of first non-repeation char
def return_first_non_repeation_str(string: str) -> str:

    # 例外：string.len() <= 1 のときは確実にユニーク
    if len(string) <= 1:
        return string

    # {str: int}
    # step1: 与えられた文字列に含まれている文字を集計する
    count_map = {}
    for s in string:
        if s in count_map:
            count_map[s] += 1
        else:
            count_map[s] = 1

    # step2: マップの中で集計結果が１の最初のkeyを見つけてreturn
    for k, v in count_map.item():
        if v == 1:
            return k

    return None


if __name__ == "__main__":
    res = return_first_non_repeation_str("a")
    print(res)
