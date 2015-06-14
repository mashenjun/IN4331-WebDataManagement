records= LOAD '/home/steven/Desktop/text1.txt' AS (title:chararray,play:chararray,time:int,name:chararray);

recordgroup =GROUP records by title;

x= FOREACH recordgroup{
	actors = FOREACH  records GENERATE play,name;
	GENERATE group,actors;
} 
dump x;