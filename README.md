# Milestone4
For Milestone 4, our group developed a full-stack web application that replicates the computer system used at a gym. However, rather than using PHP as suggested in the class tutorial, we chose to develop our app using a combination of Flask and MySQL for the back-end, while using HTML, CSS, and Jinja2 for the front-end. This design choice was taken as some of our group members had previous python experience while none of us had previously used PHP.

Our app was divided into 2 separate views, one for users and one for admins. Potential uses for the admin view could be the gym owner, or employees, while the user view would primarily be used for new member sign-ups, and accessing one’s information.

Users can:
Sign up and become members at various locations
Look at the information they provided
Update their information, or delete their signup
Book appointments to work out at specific locations

Admins can:
View all the members, and modify their information
View all the equipment, and modify them
View all locations, and modify them
View all appointments, and modify them
View all employees, and modify them

Changes from the original Schema:

Surprisingly, our schema used did have some significant changes from our proposed create statements in Milestone 3. This was due to us having many tables that only had a primary key, or very few attributes in general. To solve this issue, we chose to combine many of our tables into larger tables. For example, we combined our proposed Machine Type and Machine Status tables, into our larger Equipment table. By combining small tables, we were able to make development much simpler, as we were able to avoid complicated join queries that use multiple tables, when we could simply combine the tables instead. 

We chose to remove our exercise related tables from our final project. After implementing our skeleton, we realized that having an exercise table would be incredibly impractical, as hundreds of Exercises could be associated with a given piece of equipment, such as a bench or dumbbell. As a result, we chose to remove this feature as we could not find a potential use for it in either members or admins. Aside from this, the applications functionality was essentially the same as we originally proposed, we believe this was a good design choice rather than forcefully integrating our exercise-related tables.

The base URL is localhost:5000/home, so please go to this URL when running the program
	

