import pyodbc

def get_age_from_birthdate(birth_date):
    age = None
    conn = None
    cursor = None
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        cursor = conn.cursor()


        # Call the SQL function CalculateAge
        query = "SELECT dbo.CalculateAge(?) AS Age"
        cursor.execute(query, (birth_date,))
        row = cursor.fetchone()
        if row:
            age = row.Age

    except pyodbc.Error as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

    return age

def insert_into_table(table_name, values):
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        cursor = conn.cursor()

        placeholders = ','.join(['?' for _ in range(len(values[0]))])
        query = f'INSERT INTO {table_name} VALUES ({placeholders})'
        
        cursor.executemany(query, values)
        conn.commit()
        print("Values inserted into", table_name, "successfully.")
    except pyodbc.Error as e:
        print("Error inserting values into", table_name + ":", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()

def delete_from_table(table_name, primary_keys, values):
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        cursor = conn.cursor()
        if isinstance(primary_keys, str):
            primary_keys = [primary_keys]  
        
        placeholders = ' AND '.join([f"{key} = ?" for key in primary_keys])
        query = f'DELETE FROM {table_name} WHERE {placeholders}'

        cursor.execute(query, values)  
        conn.commit()

    except pyodbc.Error as e:
        print("Error deleting record(s) from", table_name + ":", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()


def writequery(code):
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        cursor = conn.cursor()

        # Construct the SQL query dynamically
        query = code
        
        cursor.execute(query)
        conn.commit()
        print("The code is run successfully.")

    except pyodbc.Error as e:
        print("Error excuting values into:", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()

def get_all_ids(table_name, primary_keys):
    cursor = None
    conn = None
    ids=[]
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        cursor = conn.cursor()

        
        if isinstance(primary_keys, list):
            primary_keys = ', '.join(primary_keys)

        query = 'EXEC GetAllRecords @TableName = ?, @Keys = ?'

        cursor.execute(query, (table_name, primary_keys))
        rows = cursor.fetchall()
        if primary_keys == '*':
            ids = rows
        else:
            for row in rows:
                if len(primary_keys.split(',')) == 1:
                    ids.append(row[0])
                else:
                    ids.append(row)

    except pyodbc.Error as e:
        print("Error executing query:", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()

    return ids

def search_by_primary_key(table_name, primary_key, value):
    cursor = None
    conn = None
    try:
        conn = pyodbc.connect(
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=.;"
            "Database=Criminal Investigation System;"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        cursor = conn.cursor()
        
        query = f'SELECT * FROM {table_name} WHERE {primary_key} = ?'

        cursor.execute(query, value)
        rows = cursor.fetchall()
        

    except pyodbc.Error as e:
        print("Error searching for record(s) in", table_name + ":", e)

    finally:
        if cursor:
            cursor.close()  
        if conn:
            conn.close()
    return rows