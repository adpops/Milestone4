def allTables ():
    query = """ 
    CREATE TABLE IF NOT EXISTS Locations 
    (
        id                  INT unsigned NOT NULL AUTO_INCREMENT,
        branch_name         VARCHAR(150) NOT NULL,
        address    VARCHAR(255) NOT NULL,
        max_occupancy       INT NOT NULL,
        hours_of_operation  VARCHAR(255) NOT NULL,
        PRIMARY KEY         (id) 
    )    """
    return query