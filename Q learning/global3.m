global NO_REPLICATIONS ITERMAX NA NS SMALL TPM TRM LAMBDA


NO_REPLICATIONS=30; % No of replications of simulation 
ITERMAX=448; % No of iterations of learning 
NA=40; % Number of actions in each state 
NS=32; % Number of states 

LAMBDA=0.8; % discount factor
T = readtable('data.xls');
    speed = T(1:448,[2 4]);
    power = T(1:448,[2 6]);
    distance = T(1:448,[2 7]);
    elevation = T(1:448,[2 3]);
SMALL=-1000000; 

TPM=zeros(NS, NA);
    
TRM=zeros(NS, NA);

