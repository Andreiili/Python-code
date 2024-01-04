from configuration import config, logger_function
import sql_commands_and_tables 
import mysql.connector, time


def command_execute_sql(command:str, DataBase:mysql.connector.connection_cext.CMySQLConnection)->bool:
    """
    This function is for executing code directly to database
    Param command: command that we want to execute to the DATABASE
    Param DataBase: where the command will be executed
    Returns: True if the code has been executed without any problems, otherwise False    
    """
    try:
        with DataBase.cursor() as cursor:
            cursor.execute(command)
            DataBase.commit() # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html
            file_name_database_input.info(
                command,
            )

            results = cursor.fetchall()

            if len(results) > 0:
                print("Data fetched from the database into the output txt:")
                for row in results:
                    file_name_database_input.info(
                        str(row),
                    )

        return True
    except Exception as err:
        logger_database_error.error(
            f"Unexpected {err=}, {type(err)=}"
        )
        print(f"Unexpected {err=}, {type(err)=}")
        return False
        

def connect_to_mysql(config, attempts=2, delay=1)->mysql.connector.connection_cext.CMySQLConnection:
    """
    This function is for connecting right to database
    Param config: command that we want to execute to the DATABASE
    Param attempts: how many attemps are going to be for trying to connect to the database
    Param delay: delay  in seconds betwhen the attemps
    Returns: mysql.connector.connect(**config) if everything worked well, otherwise none
    """
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger_database_error.error("Failed to connect, exiting without a connection: %s", err)
                return None
            logger_database_error.warning(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts-1,
            )
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
    return None



try:
    file_name_database_error = "errors.log"
    file_name_database_input = "inputs.log"
    file_name_database_output = "outputs.log"

    logger_database_error = logger_function(file_name_database_error)
    logger_database_input = logger_function(file_name_database_input)
    logger_database_output = logger_function(file_name_database_output)
    cnx = connect_to_mysql(config)
    cnx.close()

except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    