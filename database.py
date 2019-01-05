import psycopg2

class DatabaseConnection(object):
    def __init__(self):
        connection_credentials = """
            dbname='postgres' user='postgres' password='admin'
            host='localhost' port='5432'
            """
        try:
            self.connection = psycopg2.connect(connection_credentials)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('\n\nDatabase connected successfully\n\n')
        except Exception as e:
            print(e)
            print('\n\nDatabase Failed successfully\n\n')


    def create_table_users(self):
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Users(user_id SERIAL, first_name VARCHAR(100), last_name VARCHAR(100), age SMALLINT, email VARCHAR(320), password chkpass, created_at TIMESTAMP DEFAULT Now(),
        PRIMARY KEY (user_id));
        """
        self.cursor.execute(create_table_command)
          

    def create_table_categories(self):
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Categories(category_id SERIAL, category_name VARCHAR(50), title VARCHAR(100), description VARCHAR(320), created_at TIMESTAMP DEFAULT Now(),
        PRIMARY KEY (category_id,title,description));
        """
        self.cursor.execute(create_table_command)
        

    def create_table_tasks(self):
        create_table_command = """
        CREATE TABLE IF NOT EXISTS Tasks(task_id SERIAL, user_id INTEGER, title VARCHAR(100), description VARCHAR(320), done BOOLEAN, created_at TIMESTAMP DEFAULT Now(), 
        PRIMARY KEY (task_id), 
        FOREIGN KEY (user_id) REFERENCES Users (user_id));
        """
        self.cursor.execute(create_table_command)
    
 #======================== A function to Add New User to Users Table =====================================   

    def add_new_user(self, first_name, last_name, age, email, password):
        insert_user_command = """
        INSERT INTO Users(first_name, last_name, age, email, password)
        VALUES ('{}', '{}', '{}', '{}', '{}');
        """.format(first_name, last_name, age, email, password)

        print(insert_user_command)
        self.cursor.execute(insert_user_command)
        print("New User has been added !!")
        count = self.cursor.rowcount
    
#======================== A function to Add New Category to Categories Table =====================================   


    def add_new_category(self, category_name, title, description):
        insert_category_command = """
        INSERT INTO Categories(category_name, title, description)
        VALUES ('{}','{}','{}');
        """.format(category_name, title, description)

        print(insert_category_command)
        self.cursor.execute(insert_category_command)
        print("New Category has been added !!")
        count = self.cursor.rowcount

#======================== A function to Add New Task to Tasks Table =====================================   

    def add_new_task(self, user_id, title, description, done):
        insert_task_command = """
        INSERT INTO Tasks(user_id, title, description, done)
        VALUES ('{}','{}','{}','{}');
        """.format(user_id, title, description, done)
        
        print(insert_task_command)
        self.cursor.execute(insert_task_command)
        print("New Task has been added !!")
        count = self.cursor.rowcount

#======================== A function to gets all records from the Users Table =====================================   


    def get_all_users(self):
        sql_statement = """
        SELECT * FROM Users;
        """
        self.cursor.execute(sql_statement)
        users = self.cursor.fetchall()
        

        print("\nShow me the databases:\n")
        # print(    "   ","id name  age  gender  broke")
        for row in users:
            print("   ", row)#row[0], row[1], row[2], row[3], row[4])
        print("=============================================\n")
        return users

#======================== A function to get all records from the Categories Table =====================================   


    def get_all_categories(self):
        sql_statement = """
        SELECT * FROM Categories;
        """
        self.cursor.execute(sql_statement)
        categories = self.cursor.fetchall()
        

        print("\nShow me the databases:\n")
        # print(    "   ","id name  age  gender  broke")
        for row in categories:
            print("   ", row)#row[0], row[1], row[2], row[3], row[4])
        print("=============================================\n")
        return categories

    #======================== A function to get all records from the Tasks Table =====================================   
    def get_all_tasks(self):
        sql_statement = """
        SELECT * FROM Tasks;
        """
        self.cursor.execute(sql_statement)
        tasks = self.cursor.fetchall()
        

        print("\nShow me the databases:\n")
        for row in tasks:
            print("   ", row)#row[0], row[1], row[2], row[3], row[4])
        print("=============================================\n")
        return tasks
    
    #======================== A function to update records in the Users Table =====================================   
    def update_user_table(self, first_name,user_id):
        update_statement = """
        UPDATE Users SET first_name = '{}' WHERE user_id = '{}'
        """.format(first_name,user_id)
        self.cursor.execute(update_statement)
        print("Update done successfully !!")
    #======================== A function to update records in the Categories Table ================================ 
    def update_category_table(self, category_name, category_id):
        update_statement = """
        UPDATE Categories SET category_name = '{}' WHERE category_id = '{}'
        """.format(category_name, category_id)

        self.cursor.execute(update_statement)
        print("Update done successfully")
    #======================== A function to update records in the Tasks Table =====================================   




