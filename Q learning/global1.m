global NO_REPLICATIONS ITERMAX NA NS SMALL TPM TRM LAMBDA


NO_REPLICATIONS=30; % No of replications of simulation 
ITERMAX=10000; % No of iterations of learning 
NA=40; % Number of actions in each state 
NS=32; % Number of states 

LAMBDA=0.8; % discount factor

SMALL=-1000000; 

TPM(:,:,1)=[0.7,0.3;0.4,0.6];

TPM(:,:,2)=[0.9,0.1;0.2,0.8];

TRM(:,:,1)=[6,-5;7,12];
    
TRM(:,:,2)=[10,17;-14,13];

