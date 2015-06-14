records= LOAD '/home/steven/Desktop/text2.txt' AS (director:chararray,movie:chararray);
recordgroup =GROUP records by director;
x= FOREACH recordgroup{
	movies = FOREACH  records GENERATE movie;
	GENERATE group,movies;
} 
dump x;