class Node():
    def __init__(self, v):
        self.d = 0
        self.f = 0
        self.v = v

    def __repr__(self):
        return "Node({},{},{})".format(
            self.d, self.f, self.v)


def read_node():
    n = int(input())
    adj_list = [[] for _ in range(n + 1)]

    for _ in range(n):
        id, _, *v = [int(x) for x in input().split()]
        adj_list[id] = Node(v)

    return adj_list


def depth_first_search(adj_list):
    def dfs(id):
        nonlocal adj_list, timestamp

        adj_list[id].d = timestamp
        for adj_id in adj_list[id].v:
            if adj_list[adj_id].d == 0:
                timestamp += 1
                dfs(adj_id)
        timestamp += 1
        adj_list[id].f = timestamp

    timestamp = 1
    for id in range(1, len(adj_list)):
        if adj_list[id].d == 0:
            dfs(id)
            timestamp += 1


def print_result(adj_list):
    for id in range(1, len(adj_list)):
        print(id, adj_list[id].d, adj_list[id].f)


def main():
    adj_list = read_node()
    depth_first_search(adj_list)
    print_result(adj_list)


if __name__ == '__main__':
    main()
