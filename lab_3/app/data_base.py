import MySQLdb as mdb
import sys


# class AbstractClass(object):
#
#     def __init__(self, table_name, columns_list):
#         self.__table_name = table_name
#         self.__columns_name = columns_list
#
#     def select_from(self, condition):
#         try:
#             connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
#             cursor = connection.cursor(mdb.cursors.DictCursor)
#             cursor.execute("SELECT * FROM " + self.__table_name + " " + condition)
#             return cursor.fetchall()
#         except mdb.Error as e:
#             print 'ERROR %d %s' % (e.args[0], e.args[1])
#         finally:
#             if connection:
#                 connection.close()
#
#     def fetch_all(self):
#         return self.select_from("")
#
#     def load(self, file_name):
#         try:
#             connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
#             cursor = connection.cursor()
#             file_name = '/var/lib/mysql-files/' + file_name
#             cursor.execute("LOAD DATA INFILE " + "'" + file_name + "'" + " INTO TABLE " + self.__table_name +
#                            " FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")
#             connection.commit()
#         except mdb.Error as e:
#             print 'ERROR %d %s' % (e.args[0], e.args[1])
#         finally:
#             if connection:
#                 connection.close()
#
#     def insert(self, new_data):
#         try:
#             connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
#             cursor = connection.cursor()
#             request = "INSERT INTO " + self.__table_name + "("
#             values = "VALUES("
#             for item in self.__columns_name:
#                 request += item + ","
#                 values += "'" + str(new_data[item]) + "'" + ","
#
#             request = request[:-1] + ")"
#             values = values[:-1] + ")"
#             cursor.execute(request + values)
#             connection.commit()
#         except mdb.Error as e:
#             print 'ERROR %d %s' % (e.args[0], e.args[1])
#         finally:
#             if connection:
#                 connection.close()
#
#     def update(self, id, new_data):
#         try:
#             connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
#             cursor = connection.cursor()
#
#             request = "UPDATE " + self.__table_name + " SET "
#             for item in self.__columns_name:
#                 request += item + "=" + "'" + str(new_data[item]) + "'" + ","
#
#             request = request[:-1] + " WHERE id=" + id
#             print request
#             cursor.execute(request)
#             connection.commit()
#         except mdb.Error as e:
#             print 'ERROR %d %s' % (e.args[0], e.args[1])
#         finally:
#             if connection:
#                 connection.close()
#         pass
#
#     def delete(self, condition):
#         try:
#             connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
#             cursor = connection.cursor()
#             cursor.execute("DELETE FROM " + self.__table_name + " " + condition)
#             connection.commit()
#         except mdb.Error as e:
#             print 'ERROR %d %s' % (e.args[0], e.args[1])
#         finally:
#             if connection:
#                 connection.close()
#
#     def delete_all(self):
#         self.delete("")
#
#     def select_by_id(self, id):
#         return self.select_from("WHERE id=" + str(id))
#
#     def delete_by_id(self, id):
#         self.delete("WHERE id=" + str(id))
#
#     def full_text_search(self, condition):
#         try:
#             connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
#             cursor = connection.cursor(mdb.cursors.DictCursor)
#             cursor.execute('SELECT * FROM ' + self.__table_name + ' ' + condition)
#             return cursor.fetchall()
#         except mdb.Error as e:
#             print 'ERROR %d %s' % (e.args[0], e.args[1])
#         finally:
#             if connection:
#                 connection.close()
#
#
# class Order(AbstractClass):
#
#     def __init__(self):
#         columns = ['product_id', 'client_id', 'data_time', 'amount']
#         table_name = 'main'
#         super(Order, self).__init__(table_name, columns)
#
#     def fetch_all(self):
#         return super(Order, self).fetch_all()
#
#     def select_by_id(self, id):
#         return super(Order, self).select_by_id(id)
#
#     def select_from(self, condition):
#         return super(Order, self).select_from(condition)
#
#     def full_text_search(self, condition):
#         return super(Order, self).full_text_search(condition)
#
#
# class Product(AbstractClass):
#
#     def __init__(self):
#         columns = ['name', 'type', 'cost', 'amount', 'stock_id']
#         table_name = 'product'
#         super(Product, self).__init__(table_name, columns)
#
#     def fetch_all(self):
#         return super(Product, self).fetch_all()
#
#     def select_by_id(self, id):
#         return super(Product, self).select_by_id(id)
#
#     def select_from(self, condition):
#         return super(Product, self).select_from(condition)
#
#     def full_text_search(self, condition):
#         return super(Product, self).full_text_search(condition)
#
#     def get_choice_lst(self):
#         return tuple(tuple([item['id'], item['name']]) for item in self.fetch_all())
#
#     def get_id_by_cost(self, cost):
#         return [item["id"] for item in self.select_from("WHERE cost=" + str(cost))]
#
#
# class Stock(AbstractClass):
#
#     def __init__(self):
#         columns = ['name', 'location', 'type', 'capacity']
#         table_name = 'stock'
#         super(Stock, self).__init__(table_name, columns)
#
#     def fetch_all(self):
#         return super(Stock, self).fetch_all()
#
#     def select_by_id(self, id):
#         return super(Stock, self).select_by_id(id)
#
#     def select_from(self, condition):
#         return super(Stock, self).select_from(condition)
#
#     def full_text_search(self, condition):
#         return super(Stock, self).full_text_search(condition)
#
#
# class Client(AbstractClass):
#
#     def __init__(self):
#         columns = ['name', 'company']
#         table_name = 'client'
#         super(Client, self).__init__(table_name, columns)
#
#     def fetch_all(self):
#         return super(Client, self).fetch_all()
#
#     def select_by_id(self, id):
#         return super(Client, self).select_by_id(id)
#
#     def select_from(self, condition):
#         return super(Client, self).select_from(condition)
#
#     def full_text_search(self, condition):
#         return super(Client, self).full_text_search(condition)
#
#     def get_choice_lst(self):
#         return tuple(tuple([item['id'], item['name']]) for item in self.fetch_all())
#
#     def get_id_by_company(self, company_name):
#         return [item["id"] for item in self.select_from("WHERE company=" + "'" + company_name + "'")]


# Trigger, event and procedure for lab3
def create_procedure():
    try:
        connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
        cursor = connection.cursor()
        cursor.execute("CREATE PROCEDURE clearLog() BEGIN DELETE FROM app_orderlog; END;")
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def log_trigger():
    try:
        connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
        with connection:
            cursor = connection.cursor()

            cursor.execute("DROP TRIGGER IF EXISTS logger;")
            cursor.execute(
                "CREATE TRIGGER logger "
                "BEFORE DELETE "
                "ON app_order FOR EACH ROW "
                "BEGIN "
                "INSERT INTO app_orderlog "
                "(num_order, insert_time) "
                "VALUES "
                "(OLD.id, curdate()); "
                "END;")

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def drop_trigger():
    try:
        connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
        with connection:
            cursor = connection.cursor()
            cursor.execute("DROP TRIGGER IF EXISTS logger;")

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def create_event(minutes):
    try:
        connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
        with connection:
            cursor = connection.cursor()
            cursor.execute('SET @@global.event_scheduler = ON;')
            cursor.execute("CREATE EVENT logCleaner ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL %s MINUTE DO CALL clearLog();" % minutes)
            connection.commit()
            return 0
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if connection:
            connection.close()


def drop_event():
    try:
        connection = mdb.connect('localhost', 'root', 'vlad40000', 'vpdb')
        with connection:
            cursor = connection.cursor()
            cursor.execute("DROP EVENT IF EXISTS logCleaner;")

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    create_procedure()