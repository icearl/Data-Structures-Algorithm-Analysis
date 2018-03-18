class Vertex:
    """
    顶点的定义
    """

    def __init__(self, key):
        self.id = key
        # 相邻的节点的 id 和 权重 组成的字典
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """
        添加一个邻居
        :param nbr:要添加的一个相邻节点
        :param weight:权重
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        魔法方法，print([类实例])的时候调用
        :return:
        """
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        获取所有的邻居的 id 组成的 list
        :return: list类型
        """
        return self.connectedTo.keys()

    def getId(self):
        """
        获取当前节点的 id
        """
        return self.id

    def getWeight(self, nbr):
        """
        获取到某一个邻居的权重
        :param nbr:
        :return:
        """
        return self.connectedTo[nbr]

class Graph1:
    def __init__(self):
        # id:节点类 组成的字典
        self.vertList = {}
        # 节点数
        self.numVertices = 0

    def addVertex(self, key):
        """
        添加一个节点
        :param key:
        :return:
        """
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, key):
        """获取某个key对应的节点"""
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        """
        添加一条边
        :param f: 头 id
        :param t: 尾 id
        :param cost: 权重
        :return:
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """获取所有的节点 id 组成的 list"""
        return self.vertList.keys()

    def __iter__(self):
        """使节点类可迭代"""
        return iter(self.vertList.values())

class Graph2(object):
    def __init__(self,*args,**kwargs):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self,nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, key):
        if not key in self.nodes():
            self.node_neighbors[key] = []

    def add_edge(self,edge):
        u, v = edge
        if(v not in self.node_neighbors[u]) and ( u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if u != v:
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()
'''
    def depth_first_search(self, root=None):
        order = []
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)

        if root:
            dfs(root)

        for node in self.nodes():
            if not node in self.visited:
                dfs(node)

        print order
        return order

    def breadth_first_search(self,root=None):
        queue = []
        order = []
        def bfs():
            while len(queue)> 0:
                node  = queue.pop(0)

                self.visited[node] = True
                for n in self.node_neighbors[node]:
                    if (not n in self.visited) and (not n in queue):
                        queue.append(n)
                        order.append(n)

        if root:
            queue.append(root)
            order.append(root)
            bfs()

        for node in self.nodes():
            if not node in self.visited:
                queue.append(node)
                order.append(node)
                bfs()
        print order

        return order
'''


    def DFS(self, node0):
        """
        # Depth-First-Search
        深度优先算法，是一种用于遍历或搜索树或图的算法。沿着树的深度遍历树的节点，尽可能深的搜索树的分支。
        当节点v的所在边都己被探寻过，搜索将回溯到发现节点v的那条边的起始节点。
        这一过程一直进行到已发现从源节点可达的所有节点为止。如果还存在未被发现的节点，
        则选择其中一个作为源节点并重复以上过程，整个进程反复进行直到所有节点都被访问为止。属于盲目搜索。
        :param self:
        :param node0:
        :return:
        """
        # queue本质上是堆栈，用来存放需要进行遍历的数据
        # order里面存放的是具体的访问路径
        queue, order = [], []
        # 首先将初始遍历的节点放到queue中，表示将要从这个点开始遍历
        queue.append(node0)
        while queue:
            # 从queue中pop出点v，然后从v点开始遍历了，所以可以将这个点pop出，然后将其放入order中
            # 这里才是最有用的地方，pop（）表示弹出栈顶，由于下面的for循环不断的访问子节点，并将子节点压入堆栈，
            # 也就保证了每次的栈顶弹出的顺序是下面的节点
            v = queue.pop()
            order.append(v)
            # 这里开始遍历v的子节点
            for w in self.sequense[v]:
                # w既不属于queue也不属于order，意味着这个点没被访问过，所以讲起放到queue中，然后后续进行访问
                if w not in order and w not in queue:
                    queue.append(w)


    def BFS(self, node0):
        """
        Breadth-First-Search
        BFS是从根节点开始，沿着树的宽度遍历树的节点。如果所有节点均被访问，则算法中止。
        广度优先搜索的实现一般采用open-closed表。
        :param self:
        :param node0:
        :return:
        """
        # queue本质上是堆栈，用来存放需要进行遍历的数据
        # order里面存放的是具体的访问路径
        queue, order = [], []
        # 首先将初始遍历的节点放到queue中，表示将要从这个点开始遍历
        # 由于是广度优先，也就是先访问初始节点的所有的子节点，所以可以
        queue.append(node0)
        order.append(node0)
        while queue:
            # queue.pop(0)意味着是队列的方式出元素，就是先进先出，而下面的for循环将节点v的所有子节点
            # 放到queue中，所以queue.pop(0)就实现了每次访问都是先将元素的子节点访问完毕，而不是优先叶子节点
            v = queue.pop(0)
            for w in self.sequense[v]:
                if w not in order:
                    # 这里可以直接order.append(w) 因为广度优先就是先访问节点的所有下级子节点，所以可以
                    # 将self.sequense[v]的值直接全部先给到order
                    order.append(w)
                    queue.append(w)
        return order

if __name__ == '__main__':
    g = Graph()
g.add_nodes([i+1 for i in range(8)])
g.add_edge((1, 2))
g.add_edge((1, 3))
g.add_edge((2, 4))
g.add_edge((2, 5))
g.add_edge((4, 8))
g.add_edge((5, 8))
g.add_edge((3, 6))
g.add_edge((3, 7))
g.add_edge((6, 7))
print "nodes:", g.nodes()

order = g.breadth_first_search(1)
order = g.depth_first_search(1)
a = Vertex('ice')
b = Vertex('gua')
a.addNeighbor(b)
print(a)
