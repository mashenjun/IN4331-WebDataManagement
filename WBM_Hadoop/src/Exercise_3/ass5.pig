record1= LOAD '/home/steven/Desktop/text2.txt' AS (director:chararray,movie:chararray,year:int);
record2= LOAD '/home/steven/Desktop/text1.txt' AS (movie:chararray,actor:chararray,time:int,name:chararray);

x = FOREACH record1 GENERATE movie,director;
y = FOREACH record2 GENERATE movie,actor;

joined = JOIN x by movie, y by movie;

subfilter= FILTER joined BY x::director==y::actor;
name = FOREACH subfilter GENERATE x::director,x::movie;
dump name;