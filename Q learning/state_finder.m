function candidate=state_finder(stat)

global NO_REPLICATIONS ITERMAX NA NS SMALL TPM TRM
global3;
ran=rand(1);

old_action=stat.old_action;
old_state=stat.old_state;
sum=TPM(old_state,1,old_action);

candidate=1;
complete=0;

while 0==complete
    for j = 1:448
        a = distance;
        b = elevation;
        if(a.Distance(j)~=0)
            theta = asin(a.Distance(j)/b.Elevation(j));
        else
            theta = 0;
        end
            if ran<sum 

            complete=1;

            else

            candidate=state_assignment(theta);

            sum=sum+TPM(old_state,candidate,old_action);

            end
    end
        
end
                  
