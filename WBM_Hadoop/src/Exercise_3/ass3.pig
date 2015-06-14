record1= LOAD '/home/steven/Desktop/text2.txt' AS (director:chararray,movie:chararray,year:int);
record2= LOAD '/home/steven/Desktop/text1.txt' AS (movie:chararray,actor:chararray,time:int,name:chararray);

x = FOREACH record1 GENERATE movie,director;
y = FOREACH record2 GENERATE movie,actor,name;

grouped = COGROUP x BY movie, y BY movie;
final= FOREACH grouped{
	directors = FOREACH x GENERATE director;
	actors = FOREACH y GENERATE actor,name;
	GENERATE group,directors,actors;
} 

dump final;