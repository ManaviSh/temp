function action=action_selector(stat)

global NA 
epsilon = 0.5;
global3;
a = speed;
ran=rand(1);
candidate=1;

sum=1/NA;

complete=0;

% Selecting each action with equal probability 

while 0==complete
    for i=1:448
        if rand(1) < epsilon
            if(rand(1)<0.5)
                act = randi([15,35], 1);
            else
                act = a.Speed(i);
            end
        else
            act = find(stat.Q(stat.current_state,:)==max(stat.Q(stat.current_state,:)));
        end
        if ran<sum
        % action selected 
        action=candidate;
        complete=1;
        
        else          
        % test if ran is associated with next action 
        candidate=act;
        sum=sum+(1/NA);
        end
    end
end
end


