import pyodbc
from is_rpi import is_rpi


class SqlComm:
    def __init__(self, server, user, password):
        self.settings = dict(
            database="master",
            server=server,
            port="1433",
            user=user,
            password=password
        )
        if is_rpi():
            self.settings["driver"] = 'FreeTDS'
        else:
            self.settings["driver"] = 'SQL Server'

    def get_data_from_db(self, sqlstr):
        try:
            conn = pyodbc.connect(
                f"Driver={self.settings['driver']};"
                f"Server={self.settings['server']};"
                f"Database={self.settings['database']};"
                f"UID={self.settings['user']};"
                f"PWD={self.settings['password']};"
                f"PORT={self.settings['port']}"
            )
            cursor = conn.cursor()
            cursor.execute(sqlstr)
            newdata = cursor.fetchall()
        except Exception as e:
            print("Error SQL:")
            print(e)
            return None
        else:
            cursor.close()
        return newdata


# sql = SqlComm(server=r"192.168.60.13\inst1",
#               user="VyrobaStandalone",
#               password="Kmt0203")
# query = "SELECT FirstName, LastName FROM [HOCK].[dbo].SAI_PersonMedium_0048 WHERE ShortCode='9FBB47'"
# res = sql.get_data_from_db(query)
# print(res)
