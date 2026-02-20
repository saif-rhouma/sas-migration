data test;
   merge a b;
   by id;
   
   /* Condition for testing x > 5 */
   if x > 5 then do;
      y = x + 1;
   end;
run;