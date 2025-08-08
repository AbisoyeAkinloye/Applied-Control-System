function [o] = ObjectiveFunction(x)
    assignin("base", 'X', x);
    open("pid_pso.slx");
    sim("pid_pso.slx");

    o = sum(E1.*E1);
end
    