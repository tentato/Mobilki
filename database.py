import psycopg2

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect("dbname=dentist user=postgres password=admin")
		
        # create a cursor
        cur = conn.cursor()
        
	    # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE dentists (
            dentistid   serial PRIMARY KEY,
            name        varchar(40) NOT NULL,
            surname     varchar(40) NOT NULL
        )
        """,
        """ 
        CREATE TABLE rooms (
	        roomid serial PRIMARY KEY,
   	        number integer UNIQUE NOT NULL
        )
        """,
        """
        CREATE TABLE terms (
            id serial PRIMARY KEY,
            date date NOT NULL,
            hour time NOT NULL,
            patient_name varchar(40),
            patient_surname varchar(40),
            patient_phone integer,
            dentistid integer NOT NULL,
            roomid integer NOT NULL,
            free integer NOT NULL,
            FOREIGN KEY (roomid) REFERENCES rooms (roomid) ON DELETE NO ACTION ON UPDATE NO ACTION,
            FOREIGN KEY (dentistid) REFERENCES dentists (dentistid) ON DELETE NO ACTION ON UPDATE NO ACTION
        )
        """)
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=dentist user=postgres password=admin")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    connect()
    create_tables()