from collections import deque


def main():
    process_num, max_q_time = map(int, input().split())
    r_schedule_lst = deque([])
    for i in range(0, process_num):
        r_schedule_lst.append(list(input().split()))

    current_process = []
    elapsed_time = 0
    res = []
    while r_schedule_lst:
        cur_process = list(r_schedule_lst.popleft())
        cur_process_name = cur_process[0]
        cur_process_time = int(cur_process[1])

        remaining_time = cur_process_time - max_q_time
        if remaining_time > 0:
            elapsed_time += max_q_time
            r_schedule_lst.append([cur_process_name, remaining_time])
        else:
            elapsed_time += cur_process_time
            res.append([cur_process_name, elapsed_time])

    for n, t in res:
        print(n, t)


if __name__ == '__main__':
    main()
