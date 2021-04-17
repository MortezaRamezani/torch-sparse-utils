import torch
from torch_sparse import SparseTensor
import scipy.sparse as sp

import torch_sparse_utils as tsu


n = 10
b = 5
a = sp.rand(n, n, density=0.5, format='csr')
a[a>0] = 1
adj = SparseTensor.from_scipy(a).type_as(torch.FloatTensor())
batch_nodes = torch.randperm(n)[:b]

num_neighbors = 10
num_proc = 2

sa = tsu.sample_neighbors(adj, batch_nodes, num_neighbors, num_proc, replace=False)