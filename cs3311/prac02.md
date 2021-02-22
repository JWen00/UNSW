# Prac02 

### Setup
```
ssh grieg 
source /srvr/$USER/env 
pg start
... 
pg stop 
logout
```

Commands Practiced 

* select * from TABLE where Attribute=condition; 
* select count(*) from TABLE  where Attribute=condition 
* select * from TABLE where Attribute ilike '%ATTR%'; 
* select ATTR, count(*) from TABLE group by ATTR;
* select c.code, c.title
from   Courses c, Staff s
where  s.name='Andrew Taylor' and c.lecturer=s.userid;
    
    /// IS THE SAME AS 
* select c.code, c.title
from   Courses c join Staff s on (c.lecturer=s.userid)
where  s.name='Andrew Taylor';
