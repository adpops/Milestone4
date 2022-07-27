def allTables ():
    query = """ 
    CREATE TABLE IF NOT EXISTS Locations 
    (
        bid                 INT unsigned NOT NULL AUTO_INCREMENT,
        branch_name         VARCHAR(150) NOT NULL,
        address    VARCHAR(255) NOT NULL,
        max_occupancy       INT NOT NULL,
        hours_of_operation  VARCHAR(255) NOT NULL,
        PRIMARY KEY         (bid) 
    );
    CREATE TABLE IF NOT EXISTS Equipment
    (
        eid                 INT unsigned NOT NULL AUTO_INCREMENT,
        name                VARCHAR(150) NOT NULL,
        status              BOOL NOT NULL,
        branch_id           INT unsigned NOT NULL,
        PRIMARY KEY         (eid),
        FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    );
    CREATE TABLE IF NOT EXISTS Appointment
    (
        aid                 INT unsigned NOT NULL AUTO_INCREMENT,
        name                VARCHAR(150) NOT NULL,
        branch_id           INT unsigned NOT NULL,
        date                VARCHAR(150),
        PRIMARY KEY         (aid),
        FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    );
    CREATE TABLE IF NOT EXISTS Subscription
    (
        sid                 INT unsigned NOT NULL AUTO_INCREMENT,
        price               FLOAT NOT NULL,
        termlength          VARCHAR(150) NOT NULL,
        renewaldate         VARCHAR(150) NOT NULL,
        branch_id           INT unsigned NOT NULL,
        PRIMARY KEY         (sid),
        FOREIGN KEY (branch_id) REFERENCES Locations(bid)
    );
    CREATE TABLE IF NOT EXISTS Member
    (
        mid                 INT unsigned NOT NULL AUTO_INCREMENT,
        firstname           VARCHAR(150) NOT NULL,
        lastname            VARCHAR(150) NOT NULL,
        birthdate           VARCHAR(150) NOT NULL,
        sub_id              INT unsigned NOT NULL,
        PRIMARY KEY         (mid),
        FOREIGN KEY (sub_id) REFERENCES Subscription(sid)
    )
    """
    return query

