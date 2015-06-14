record1= LOAD '/home/steven/Desktop/text2.txt' AS (director:chararray,movie:chararray,year:int);
record2= LOAD '/home/steven/Desktop/text1.txt' AS (movie:chararray,actor:chararray,time:int,name:chararray);

x = FOREACH record1 GENERATE movie,director;
y = FOREACH record2 GENERATE movie,actor,name;

grouped = COGROUP y BY actor,x by director;

filtered_data1 = FILTER grouped BY NOT IsEmpty(y) and NOT IsEmpty(x) ;

final= FOREACH filtered_data1{
	directors = FOREACH x GENERATE movie;
	actors = FOREACH y GENERATE movie;
	GENERATE group,actors,directors;
} 

dump final;

