import torch
from torch_sparse import SparseTensor
import scipy.sparse as sp
import time

import torch_sparse_utils as tsu


n = 1000
b = 500
a = sp.rand(n, n, density=0.5, format='csr')
a[a>0] = 1
adj = SparseTensor.from_scipy(a).type_as(torch.FloatTensor())
batch_nodes = torch.randperm(n)[:b]

num_neighbors = 50
num_proc = 10

print('Torch Sparse')
start_time = time.perf_counter()
sa = adj.sample_adj(batch_nodes, num_neighbors, replace=False)
end_time = time.perf_counter()
print('Time (s)', end_time - start_time)

print('Cython')
start_time = time.perf_counter()
sa = tsu.sample_neighbors(adj, batch_nodes, num_neighbors, num_proc, replace=False)
end_time = time.perf_counter()
print('Time (s)', end_time - start_time)