% Closed loop transfer function for Ziegler-Nichols method

G = zpk([],[0 -2 -3], 1)

rlocus(G);

%% Programming the System

Gc = pid(18, 14.0345, 5.771);   % compensator
open_loop_system = G*Gc;        % plant and the compensator
close_loop_system = feedback(open_loop_system,1); % add a unity feedback
step(close_loop_system, 15)         % add a step input