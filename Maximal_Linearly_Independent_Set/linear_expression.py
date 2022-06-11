import numpy as np

def is_linear_expression(M, src_idxs, tgt_idx, factors_for_src):
    len_src_idxs = len(src_idxs)
    if len_src_idxs != len(factors_for_src):
        print("error")
        return False

    print("M.size:", M[:,0].size)
    v = np.zeros(M[:,0].size)
    for sid, factor in zip(src_idxs, factors_for_src):
        v += factor * M[:,sid]
        print("v:", v)

    tgt_value = M[:,tgt_idx]
    src_with_linear_expression = v

    print("tgt_value:", tgt_value)
    print("src_with_linear_expression:", src_with_linear_expression)

    if tgt_value.any() == src_with_linear_expression.any():
        return True
    else:
        return False 

M1 = np.array([[1,2,-1,0],[4,5,2,2],[1,-1,5,2],[0,-3,6,-1],[2,2,2,0]])
M2 = np.array([[1,0,3,0],[0,1,-2,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
src_idxs = (0, 1, 3)
tgt_idx = 2
factors_for_src = (3, -2, 0)

ret = is_linear_expression(M1, src_idxs, tgt_idx, factors_for_src)
print("ret:", ret)

ret = is_linear_expression(M2, src_idxs, tgt_idx, factors_for_src)
print("ret:", ret)
