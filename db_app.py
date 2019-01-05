from database import DatabaseConnection


if __name__ == "__main__":
    print("========================================= Connection Test ===================================")
    test_connection = DatabaseConnection()
    print("========================================= End of Test ===================================")
    test_connection.create_table_users()
    test_connection.create_table_categories()
    test_connection.create_table_tasks()
    print("######################################")
    print("Tables created successfully !!")

    print(test_connection.get_all_users())

    print("======================================== Adding New User ================================")
    # test_connection.add_new_user('Mugiba', 'Seguya', 45, 'seguyanicholus2015@gmail.com', '@123')
    # test_connection.add_new_category('SOCIAL','WEEKEND','Hangout With Friends')
    # test_connection.add_new_task('1','family','lunch','False')
    # test_connection.update_user_table('ssekitoleko','3')
    test_connection.update_category_table('POLITICAL','1')
    

