from dataclasses import dataclass

import psycopg2


class ConfigDB:
    dbname = "lesson_1"
    user = "postgres"
    password = "1"
    host = "127.0.0.1"
    port = 5432


class DB:
    con = psycopg2.connect(**dict(filter(lambda x: not x[0].startswith("__"), ConfigDB.__dict__.items())))
    cur = con.cursor()

    def get_dict_resultset(self, result):
        columns = list(self.cur.description)
        results = []
        for row in result:
            row_dict = {}
            for i, col in enumerate(columns):
                row_dict[col.name] = row[i]
            results.append(row_dict)

        # display
        return results

    def select(self, **conditions)->list:
        columns = " , ".join(self.cols) if self.cols else "*"
        table_name = self.__class__.__name__.lower() + "s"
        condition_format = "where " + " = %s and ".join(conditions.keys()) + " = %s" if conditions else ""
        query = f"select {columns} from {table_name} {condition_format}"
        params = tuple(conditions.values())
        self.cur.execute(query, params)
        results = []
        for i in self.get_dict_resultset(self.cur.fetchall()):
            results.append(self.__class__(**i))
        return results

    def insert(self):
        table_name = self.__class__.__name__.lower() + "s"
        attrs = self.__dict__
        del attrs['cols']
        attrs = dict((key , val) for key , val in attrs.items() if val)
        cols_format = " , ".join(attrs.keys())
        params_format = " , ".join(["%s"] * len(attrs))
        query = f"insert into {table_name} ({cols_format}) values ({params_format})"
        params = tuple(attrs.values())
        self.cur.execute(query, params)
        self.con.commit()

    def update(self , **conditions):
        table_name = self.__class__.__name__.lower() + "s"
        attrs = self.__dict__
        del attrs['cols']
        attrs = dict((key, val) for key, val in attrs.items() if val)
        set_fields_format = " = %s ,".join(attrs.keys()) + " = %s "
        con_format = "where " + " = %s and ".join(conditions.keys()) + " = %s " if conditions else ""
        query = f"update {table_name} set {set_fields_format} {con_format}"
        params = tuple(list(attrs.values()) + list(conditions.values()))
        self.cur.execute(query, params)
        self.con.commit()

# TODO Bot + postgresql





class User(DB):
    def __init__(self, *cols,
                 user_id=None,
                 first_name=None,
                 last_name=None,
                 username=None,
                 phone_number=None,
                 email=None,
                 longitude=None,
                 latitude=None,
                 created_at=None,
                 ):
        self.cols = cols
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.longitude = longitude
        self.latitude = latitude
        self.created_at = created_at


class Product(DB):
    def __init__(self,
                 *cols,
                 id=None,
                 name=None,
                 price=None,
                 category_id=None,
                 ):
        self.cols = cols
        self.id = id
        self.name = name
        self.price = price
        self.category_id = category_id

class Category(DB):
    def __init__(self,
                 *cols,
                 id=None,
                 name=None,
                 ):
        self.cols = cols
        self.id = id
        self.name = name


Category(name = "Iphone2").update(id= 1)





