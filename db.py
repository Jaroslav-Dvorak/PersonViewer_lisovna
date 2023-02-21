import json
from copy import copy
from sql_comm import SqlComm


class DB:
    def __init__(self):
        self.local_store = "persons.json"
        self.credincials = "credincials.json"
        credincials = self.autentification()
        self.sql = SqlComm(**credincials)

        try:
            with open(self.local_store, "r", encoding='utf8') as f:
                self.persons = json.load(f)
        except Exception as e:
            self.persons = {}

    def read(self, hex_code):
        sqlstr = ("SELECT FirstName, LastName "
                  "FROM [192.168.60.13\\INST1].[HOCK].[dbo].SAI_PersonMedium_0048 "
                  f"WHERE ShortCode='{hex_code}'"
                  )
        name = self.sql.get_data_from_db(sqlstr)
        if name is not None and len(name) == 1 and isinstance(name[0], str):
            name = " ".join(name[0])
            old_persons = copy(self.persons)
            self.persons.update({hex_code: name})
            diff = dict(set(self.persons.items()) - set(old_persons.items()))
            if len(diff) == 1:
                try:
                    with open(self.local_store, "w", encoding="utf8") as f:
                        json.dump(self.persons, f, ensure_ascii=False, indent=4)
                except Exception as e:
                    print(e)
            return name

        try:
            name = self.persons[hex_code]
        except KeyError:
            name = hex_code
        return name

    def autentification(self):
        credincials = {}
        try:
            with open(self.credincials, "r", encoding='utf8') as f:
                credincials = json.load(f)
        except Exception as e:
            server = input("Server? ")
            user = input("User? ")
            password = input("Password? ")
            credincials = {"server": server,
                           "user": user,
                           "password": password}
            with open(self.credincials, "w", encoding="utf8") as f:
                json.dump(credincials, f, ensure_ascii=False, indent=4)
        finally:
            return credincials
