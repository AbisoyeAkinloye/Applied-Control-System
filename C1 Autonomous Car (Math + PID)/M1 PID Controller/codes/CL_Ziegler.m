% Closed loop transfer function for Ziegler-Nichols method

G = zpk([],[0 -2 -3], 1)

rlocus(G)