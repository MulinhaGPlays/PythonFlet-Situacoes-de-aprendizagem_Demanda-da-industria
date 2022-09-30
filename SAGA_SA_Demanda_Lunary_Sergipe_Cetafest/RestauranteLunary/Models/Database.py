from typing import List, Optional
import pyodbc #importar biblioteca
Dados_Conexao = (
    "Driver={SQL Server};"
    "Server=.\SENAI;"
    "Database=RestauranteLunary;"
)

conexao = pyodbc.connect(Dados_Conexao, autocommit=True) 
print("Banco De Dados Conectado Com Sucesso!")

RestauranteLunary = conexao.cursor() #conectar ao banco de dados

class Database:
    global RL
    RL = RestauranteLunary
    def SELECT(COLUMN: Optional[List] | str = '*',
               TABLE: Optional[List] | str = None):
        """_summary_
            Executa o comando SELECT do SQL Server
        Args:
            COLUMN (Optional[List] | str, optional): _description_. o padrão é '*'.
            TABLE (Optional[List] | str, optional): _description_. o padrão é None.
        """
        COLUMN = ', '.join(COLUMN) if type(COLUMN) is list else COLUMN
        TABLE = ', '.join(TABLE) if type(TABLE) is list else TABLE
        try:
            RL.execute(f"SELECT {COLUMN} FROM {TABLE}")
        except:
            pass
    
    def INSERT_INTO(TABLE: Optional[List] | str = None,
                    COLUMN: Optional[List] | str = None,
                    VALUES: Optional[List] | str = None):
        COLUMN = ', '.join(COLUMN) if type(COLUMN) is list else COLUMN
        TABLE = ', '.join(TABLE) if type(TABLE) is list else TABLE
        VALUES = ', '.join(VALUES) if type(VALUES) is list else VALUES
        return RL.execute(f"INSERT INTO {TABLE} ({COLUMN}) VALUES ({VALUES});")
    
    def SELECT_WHERE(COLUMN: Optional[List] | str = '*',
               TABLE: Optional[List] | str = None,
               COLUMNCond: Optional[List] | str = '*',
               Operator: str = '=',
               Condition = 'NULL'):
        COLUMN = ', '.join(COLUMN) if type(COLUMN) is list else COLUMN
        COLUMNCond = ', '.join(COLUMNCond) if type(COLUMNCond) is list else COLUMNCond
        TABLE = ', '.join(TABLE) if type(TABLE) is list else TABLE
        try:    
            RL.execute(f"SELECT {COLUMN} FROM {TABLE} WHERE {COLUMNCond} {Operator} '{Condition}';")
        except:
            pass
    
    def SELECT_ORDERby(COLUMN: Optional[List] | str = '*',
                       TABLE: Optional[List] | str = None,
                       COLUMNCond: Optional[List] | str = '*',
                       ORDER = 'ASC'):
        try:
            RL.execute(f"SELECT {COLUMN} FROM {TABLE} ORDER BY {COLUMNCond} {ORDER}")
        except:
            pass
    
    def UPDATE(TABLE: Optional[List] | str = None, 
               COLUMN: Optional[List] | str = '*',
               VALUES: Optional[List] | str = None,
               COLUMNCond: Optional[List] | str = '*',
               Operator: str = '=',
               Condition = 'NULL'):
        return RL.execute(f"UPDATE {TABLE} SET {COLUMN} = '{VALUES}' WHERE {COLUMNCond} {Operator} '{Condition}'")
    
    def DELETE_WHERE(TABLE: Optional[List] | str = None, 
                     COLUMN: Optional[List] | str = '*',
                     Operator: str = '=',
                     Condition = 'NULL'):
        return RL.execute(f"DELETE FROM {TABLE} WHERE {COLUMN} {Operator} '{Condition}'")
    
    def FETCHALL():return RL.fetchall()
    
    def DELETE(TABLE: Optional[List] | str = None):return RL.execute(f"DELETE {TABLE}")