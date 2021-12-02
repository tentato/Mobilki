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
        CREATE TABLE appointments (
            appid serial PRIMARY KEY,
            date date NOT NULL,
            hour time NOT NULL,
            patient_name varchar(40),
            patient_surname varchar(40),
            patient_phone integer,
            dentistid serial NOT NULL,
            roomid serial NOT NULL,
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

def insert_dentist(name, surname):
    """ insert the PostgreSQL database"""
    command =  """INSERT INTO dentists(name, surname) VALUES(%s, %s) RETURNING dentistid;"""
    conn = None
    dentistid = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=dentist user=postgres password=admin")
        cur = conn.cursor()
        cur.execute(command, (name, surname))
        dentistid = cur.fetchone()[0]
        # commit the changes
        conn.commit()
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return dentistid

def insert_room(number):
    """ insert the PostgreSQL database"""
    command =  """INSERT INTO rooms(number) VALUES(%s) RETURNING roomid;"""
    conn = None
    roomid = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=dentist user=postgres password=admin")
        cur = conn.cursor()
        cur.execute(command, (number,))
        roomid = cur.fetchone()[0]
        # commit the changes
        conn.commit()
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return roomid

def insert_appointment(date, hour, patient_name, patient_surname, patient_phone, dentistid, roomid, free):
    """ insert the PostgreSQL database"""
    command = """INSERT INTO appointments(date, hour, patient_name, patient_surname, patient_phone, dentistid, roomid, free) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING appid;"""
    conn = None
    appid = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=dentist user=postgres password=admin")
        cur = conn.cursor()
        cur.execute(command, (date, hour, patient_name, patient_surname, patient_phone, dentistid, roomid, free,))
        appid = cur.fetchone()[0]
        # commit the changes
        conn.commit()
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return appid

if __name__ == '__main__':
    connect()
    # create_tables() ### działa
    # insert_dentist("Ale", "Paw") ### działa
    # insert_room(10) ### działa
    # insert_appointment("02.12.2021", "14:00", "Jacek", "Placek", "123456789", 1, 1, 1)