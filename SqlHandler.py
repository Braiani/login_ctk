import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class SqlHandler:
    def __init__(self) -> None:
        self.connection = False
        self.config = self.get_info_from_env()
        self.connect()
    
    def connect(self):
        if not self.connection:
            try:
                if not self.config:
                    raise Exception("Erro ao recuperar as informações de acesso ao Banco.")
                
                self.connection = mysql.connector.connect(
                    host=self.config['host'],
                    port=self.config['port'],
                    database=self.config['database'],
                    user=self.config['user'],
                    password=self.config['password'],
                )

                if self.connection.is_connected():
                    print("Conetcado com sucesso:", self.connection.get_server_info())

            except Error as e:
                print("Erro ao tentar conectar com o MySQL", e)
            except Exception as error:
                print(error)

    @staticmethod
    def get_info_from_env():
        try:
            load_dotenv()
            return {
                'host': os.getenv('host', '10.28.2.15'),
                'port': os.getenv('port', '3306'),
                'database': os.getenv('database', 'mercado'),
                'user': os.getenv('user', 'suporte'),
                'password': os.getenv('password', 'suporte')
            }
        except Exception as e:
            print(f'Erro ao carregar variáveis de ambiente: {e}')
            return False
    
    
    def exec_query(self, query, params=None, commit=False):
        if not self.connection:
            try:
                self.connect()
            except:
                return False
        
        cursor = self.connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            if not commit:
                records = cursor.fetchall()
                return records
            else:
                self.connection.commit()
                return cursor.rowcount
        except Error as e:
            print(e)
            return False
        finally:
            cursor.close()

if __name__ == "__main__":
    import Main
    
    Main