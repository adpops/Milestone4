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

/*Projection*/
/*Getting all the membership prices for the admin */

/*Join*/
/*Combines the membership and subscription tables to show the admin information about the user's and their subscriptions*/
SELECT m.firstname, m.lastname, m.birthdate, m.location, s.price, s.termlength, s.renewaldate 
        FROM member m, subscription s 
        WHERE m.sub_id = s.sid;

/*Aggregation*/
/*Returns the number of appointments booked across all locations*/
SELECT COUNT(*) FROM Appointment;

/*Nested Aggregation*/
/*Returns the number of people subscribed to each membership tier*/
SELECT member.sub_id, COUNT(*) 
        FROM MEMBER 
        WHERE Member.sub_id IN 
        (SELECT sid FROM Subscription) 
        GROUP BY member.sub_id;

/*Division*/
/*Returns the name of people who are presented all locations based on their first name*/
SELECT DISTINCT x.firstname
        FROM Member AS x
        WHERE NOT EXISTS (
            SELECT *
            FROM Locations AS y
            WHERE NOT EXISTS (
                SELECT *
                FROM Member AS z
                WHERE (z.firstname = x.firstname)
                AND (z.location = y.bid)
            )
        );