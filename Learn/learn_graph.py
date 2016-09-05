import networkx

G = networkx.Graph()   # 建立一个空的无项图
Gdi = networkx.DiGraph()  # 建立一个有向图
G.add_node(1)  # 添加一个节点1
G.add_edge(2, 3)  # 添加一条边2-3（隐含添加了两个节点2,3）
G.add_edge(3, 2)  # 对于无向图，边3-2和2-3被认为是一条边
G.add_edge(1, 2)  # 添加一条边2-3（隐含添加了两个节点2,3）
print("输出全部的节点：", G.nodes())
print("输出全部的边：", G.edges())
print("输出边的数量：", G.number_of_edges())
# G.add_edges_from([(2, 3, 3), (1, 2, 7)])
G.add_weighted_edges_from([(2, 3, 3.1), (1, 2, 7.5)])
# 添加0-1和1-2两条边，权重分别是3.0和7.5
# 读取权重数
print("边的权重：", G.get_edge_data(1, 2))

path = networkx.all_pairs_shortest_path(G)  # 调用多远最短路径算法，计算图G所有节点的最短路径

# 输出路径
print("输出节点1,3的最短路径", path[1][3])
