clc; clear; close all;

% define the details of the table design problem
nVar = 3; % number of variables (Kp, Ki, Kd)
lb = [1 0.1 0.01]; % lower bounds (Kp, Ki, Kd)
ub = [1000 1000 1000]; % upper bounds (Kp, Ki, Kd)
fobj = @ObjectiveFunction; % objective function

% define the PSO parameters
noP = 10; % number of particles
maxIter = 5; % maximum number of iterations
wMax = 0.9; % maximum inertia weight
wMin = 0.2; % minimum inertia weight
c1 = 2; c2 = 2; % cognitive and social coefficients
vMax = (ub - lb).*0.2;
vMin = -vMax;

% Initialize the particles 
for k = 1 : noP
    Swarm.Particles(k).X = (ub-lb) .* rand(1,nVar) + lb; 
    Swarm.Particles(k).V = zeros(1, nVar); 
    Swarm.Particles(k).PBEST.X = zeros(1,nVar); 
    Swarm.Particles(k).PBEST.O = inf; 
    
    Swarm.GBEST.X = zeros(1,nVar);
    Swarm.GBEST.O = inf;
end


% Main loop
for t = 1 : maxIter
    
    % Calcualte the objective value
    for k = 1 : noP
        currentX = Swarm.Particles(k).X;
        Swarm.Particles(k).O = fobj(currentX);
        
        % Update the PBEST
        if Swarm.Particles(k).O < Swarm.Particles(k).PBEST.O 
            Swarm.Particles(k).PBEST.X = currentX;
            Swarm.Particles(k).PBEST.O = Swarm.Particles(k).O;
        end
        
        % Update the GBEST
        if Swarm.Particles(k).O < Swarm.GBEST.O
            Swarm.GBEST.X = currentX;
            Swarm.GBEST.O = Swarm.Particles(k).O;
        end
    end
    
    % Update the X and V vectors 
    w = wMax - t .* ((wMax - wMin) / maxIter);
    
    for k = 1 : noP
        Swarm.Particles(k).V = w .* Swarm.Particles(k).V + c1 .* rand(1,nVar) .* (Swarm.Particles(k).PBEST.X - Swarm.Particles(k).X) ...
                                                                                     + c2 .* rand(1,nVar) .* (Swarm.GBEST.X - Swarm.Particles(k).X);
                                                                                 
        
        % Check velocities 
        index1 = find(Swarm.Particles(k).V > vMax);
        index2 = find(Swarm.Particles(k).V < vMin);
        
        Swarm.Particles(k).V(index1) = vMax(index1);
        Swarm.Particles(k).V(index2) = vMin(index2);
        
        Swarm.Particles(k).X = Swarm.Particles(k).X + Swarm.Particles(k).V;
        
        % Check positions 
        index1 = find(Swarm.Particles(k).X > ub);
        index2 = find(Swarm.Particles(k).X < lb);
        
        Swarm.Particles(k).X(index1) = ub(index1);
        Swarm.Particles(k).X(index2) = lb(index2);
        
    end
    
    outmsg = ['Iteration# ', num2str(t) , ' Swarm.GBEST.O = ' , num2str(Swarm.GBEST.O)];
    disp(outmsg);
    
    cgCurve(t) = Swarm.GBEST.O;
end
 
semilogy(cgCurve);
xlabel('Iteration#')
ylabel('Weight')