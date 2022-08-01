/* This file contains all the create statements used in our application, 
along with the necessary insert statements used to populate the database when starting the application for the first time*/
CREATE TABLE IF NOT EXISTS Locations 
    (
        bid                 INT unsigned NOT NULL AUTO_INCREMENT,
        branch_name         VARCHAR(150) NOT NULL,
        address             VARCHAR(255) NOT NULL,
        max_occupancy       INT NOT NULL,
        hours_of_operation  VARCHAR(255) NOT NULL,
        PRIMARY KEY         (bid) 
    );
CREATE TABLE IF NOT EXISTS Equipment
(
    eid                 INT unsigned NOT NULL AUTO_INCREMENT,
    name                VARCHAR(150) NOT NULL,
    status              BOOL,
    branch_id           INT unsigned NOT NULL,
    PRIMARY KEY         (eid),
    FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Appointment
(
    aid                 INT unsigned NOT NULL AUTO_INCREMENT,
    name                VARCHAR(150) NOT NULL,
    branch_id           INT unsigned NOT NULL,
    date                VARCHAR(150),
    PRIMARY KEY         (aid),
    FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Subscription
(
    sid                 INT unsigned NOT NULL AUTO_INCREMENT,
    price               FLOAT NOT NULL,
    termlength          VARCHAR(150) NOT NULL,
    renewaldate         VARCHAR(150) NOT NULL,
    PRIMARY KEY         (sid)
);
CREATE TABLE IF NOT EXISTS Member
(
    mid                 INT unsigned NOT NULL AUTO_INCREMENT,
    firstname           VARCHAR(150) NOT NULL,
    lastname            VARCHAR(150) NOT NULL,
    birthdate           VARCHAR(150) NOT NULL,
    sub_id              INT unsigned NOT NULL,
    branch_id           INT unsigned NOT NULL,
    PRIMARY KEY         (mid),
    FOREIGN KEY (sub_id) REFERENCES Subscription(sid)
    ON DELETE CASCADE,
    FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS Employee
(
    eid                 INT unsigned NOT NULL AUTO_INCREMENT,
    firstname           VARCHAR(150) NOT NULL,
    lastname            VARCHAR(150) NOT NULL,
    birthdate           VARCHAR(150) NOT NULL,
    startdate           VARCHAR(150) NOT NULL,
    branch_id           INT unsigned NOT NULL,
    PRIMARY KEY         (eid),
    FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    ON DELETE CASCADE
);

INSERT INTO Locations (branch_name, address, max_occupancy, hours_of_operation) VALUES  ("Club 16", "10851  111 street", "100", "9-5");
INSERT INTO Locations (branch_name, address, max_occupancy, hours_of_operation) VALUES  ("Goodlife", "10851  112 street", "100", "9-5");
INSERT INTO Locations (branch_name, address, max_occupancy, hours_of_operation) VALUES  ("Anytime", "10851  110 street", "100", "9-9");

INSERT INTO subscription(price, termlength, renewaldate) VALUES(9.99, 1, "June 28");
INSERT INTO subscription(price, termlength, renewaldate) VALUES(19.99, 1, "August 28");
INSERT INTO subscription(price, termlength, renewaldate) VALUES(29.99, 1, "September 28");