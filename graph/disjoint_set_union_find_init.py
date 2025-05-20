class DisjointSet:
    def __init__(self, n) -> None:
        self.parent = list(range(n + 1))
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)

    def __str__(self) -> str:
        p_str = [" ".join(str(i)) for i in self.parent]
        r_str = [" ".join(str(i)) for i in self.rank]
        s_str = [" ".join(str(i)) for i in self.size]
        # return f"rank : {r_str}\nparent : {p_str}"
        return f"size : {s_str}\nparent : {p_str}"

    def find_ultimate_parent(self, node): # finds the ultimate parent
        # base condition: if a node's parent is the node itself then we have the ultimate parent
        if self.parent[node] == node: return node
        # if not, we keep finding the parent of the current node until we have the ultimate parent
        # return self.find(self.parent[node]) # but this takes O(log n) time, 
        # we use path compression so it takes constant time O(4*alpha) by doing:
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]
    
    def union_by_rank(self, node1, node2):
        ult_par_node1 = self.find_ultimate_parent(node1)
        ult_par_node2 = self.find_ultimate_parent(node2)

        # if node1 & node2 belong to the same component, then do nothing
        if ult_par_node1 == ult_par_node2: return

        # but if they do not belong to the same component then we need to perform a union by rank:
        # if rank(ultimate parent of node1) is less than rank(ultimate parent of node2), then make 
        # the ultimate parent of node2 as the parent of ultimate parent of node1
        if self.rank[ult_par_node1] < self.rank[ult_par_node2]: self.parent[ult_par_node1] = ult_par_node2
        elif self.rank[ult_par_node1] > self.rank[ult_par_node2]: self.parent[ult_par_node2] = ult_par_node1
        else: # keep ultimate parent of node1 as the parent
            self.parent[ult_par_node2] = ult_par_node1
            self.rank[ult_par_node1] += 1 # and increase the rank of the parent

    def union_by_size(self, node1, node2):
        ult_par_node1 = self.find_ultimate_parent(node1)
        ult_par_node2 = self.find_ultimate_parent(node2)

        if ult_par_node1 == ult_par_node2: return

        if self.size[ult_par_node1] < self.size[ult_par_node2]: 
            self.parent[ult_par_node1] = ult_par_node2
            self.size[ult_par_node2] += self.size[ult_par_node1]
            
        else: # does not matter if they're equal or greater we anyways need to increase its size 
            self.parent[ult_par_node2] = ult_par_node1
            self.size[ult_par_node1] += self.size[ult_par_node2]

# the smaller component/node to the larger so as to save time when finding rank same is true for union by rank 

# ds = DisjointSet(7)
# print(ds)
# ds.union_by_rank(1,2)
# ds.union_by_rank(2,3)
# ds.union_by_rank(4,5)
# ds.union_by_rank(6,7)
# ds.union_by_rank(5,6)
# # check if 3 and 7 belong to the same component
# print("Same") if (ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7)) else print("Not same")
# print(ds)

# ds.union_by_rank(3,7)
# # after union let's see now if they belong to the same component
# print("Same") if (ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7)) else print("Not same") 
# print(ds)
            
ds = DisjointSet(7)
print(ds)
ds.union_by_size(1,2)
ds.union_by_size(2,3)
ds.union_by_size(4,5)
ds.union_by_size(6,7)
ds.union_by_size(5,6)
# check if 3 and 7 belong to the same component
print("Same") if (ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7)) else print("Not same")
print(ds)

ds.union_by_size(3,7)
# after union let's see now if they belong to the same component
print("Same") if (ds.find_ultimate_parent(3) == ds.find_ultimate_parent(7)) else print("Not same") 
print(ds)
