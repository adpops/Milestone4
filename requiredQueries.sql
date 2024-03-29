/*Examples of queries that demonstrate each of the required categories in the grading scheme,
only one example is given for each query although we have multiple examples for some of them,
this was done for ease of grading */
/*Syntax may be a little bit different, as these are the Insert Statements we used in FLASK
to accomodate the user input being passed into the query*/

/*Insert*/
INSERT INTO Locations (branch_name, address, max_occupancy, hours_of_operation) VALUES  ("Club 16", "10851  111 street", "100", "9-5");

/*Delete*/
/*mid is the member id that is will be deleted, 
please see the Member table in populate.sql as we specified ON DELETE CASCADE in the create table*/
DELETE FROM Member WHERE mid =  %s, (mid,);

/*Update*/
/*This allows a specifc member to have their information be updated*/
UPDATE Member SET firstname=%s, lastname=%s, birthdate=%s, sub_id=%s , location=%s  WHERE mid=%s, (fname, lname, birthday,sub,location, mid);

/*Selection*/
/*This returns a specific member's information, depending on their mid*/
SELECT * FROM member WHERE mid =  %s, (mid,);
/*Dynamic*/
/*Returns all the data in a table depending on parameter*/
SELECT * FROM TableName

/*Projection*/
/*Getting all the values in a specific column based on the values passed for colName and TableName*/
SELECT colName FROM tableName;

/*Join*/
/*Dynamic Join*/
/*Joins two tables where the columns have identical values*/
SELECT * 
FROM table1, table2
WHERE table1.col1 = table2.col2 

/*Aggregation*/
/*Returns the number of instances of a specific table based on the user input*/
SELECT COUNT(*) FROM TableName;

/*Nested Aggregation*/
/*Returns the number of people subscribed to each membership tier*/
SELECT member.sub_id, COUNT(*) 
        FROM MEMBER 
        WHERE Member.sub_id IN 
        (SELECT sid FROM Subscription) 
        GROUP BY member.sub_id;

/*Division*/
/*Dynamic Division Query*/
/* Gets column from a table where the column is at all locations */
SELECT DISTINCT x.divColName
                FROM TableName AS x
                WHERE NOT EXISTS (
                    SELECT *
                    FROM Locations AS y
                    WHERE NOT EXISTS (
                        SELECT *
                        FROM TableName AS z
                        WHERE (z.divColName = x.divColName)
                        AND (z.branch_id = y.bid)
                    )
                );