class Node():
    lt_table = {}

    def __init__(self, id):
        self.id = id
        self.adj = []

    def __lt__(self, other):
        def lt():
            S = []
            S.append(self)

            while S:
                v = S.pop()
                for a in v.adj:
                    if other == a:
                        return True
                    else:
                        S.append(a)
            return False
        """
        if (self.id, other.id) in Node.lt_table:
            return Node.lt_table[(self.id, other.id)]
        else:
            result = lt()
            Node.lt_table[(self.id, other.id)] = result
            return result
        """
        return lt()

    def __gt__(self, other):
        return not self < other and self is not other

    def __repr__(self):
        return "Node({},{})".format(
            self.id,
            [v.id for v in self.adj])


def read_edges(ne, V):
    for _ in range(ne):
        s, t = [int(x) for x in input().split()]
        V[s].adj.append(V[t])


def swap(V, x, y):
    tmp = V[x]
    V[x] = V[y]
    V[y] = tmp


def sort(V):
    #print([v.id for v in V])
    for i in range(len(V)):
        for j in reversed(range(i, len(V) - 1)):
            if V[j] > V[j+1]:
                swap(V, j, j + 1)
                #print("  ", [v.id for v in V])
        #print([v.id for v in V])


def main():
    nv, ne = [int(x) for x in input().split()]
    V = [Node(id) for id in range(nv)]
    read_edges(ne, V)
    sort(V)
    [print(v.id) for v in V]


if __name__ == '__main__':
    main()
