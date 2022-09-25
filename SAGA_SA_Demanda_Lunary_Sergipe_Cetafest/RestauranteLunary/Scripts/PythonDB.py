class PythonDB:    
    def __init__(self, DatabaseName):
        self.DatabaseName = DatabaseName
    def CreateDataBase(self):
        with open(f'Models/UserLocalStorage.py', 'w') as LocalDB:
            LocalDB.write(f'{self.DatabaseName} '+'= {}')

    def CreateTable(self, SessionId):
        with open(f'Models/UserLocalStorage.py', 'a') as LocalDB:
            LocalDB.writelines(f"\n{self.DatabaseName}['{SessionId}'] = "+"{'auth': 0, 'Cardapio': []}")
            
    def authValue(self, SessionId, Value: 1 | 0 = 0, Item = ''):
        Item = ', '.join(Item) if type(Item) is list else Item
        with open(f'Models/UserLocalStorage.py', 'r') as LocalDBr:
            lines = LocalDBr.readlines()
            with open(f'Models/UserLocalStorage.py', 'w') as LocalDBw:
                for line in lines:
                    if line.find(SessionId) == -1:
                        LocalDBw.write(line)
            with open(f'Models/UserLocalStorage.py', 'a') as LocalDBa:
                LocalDBa.writelines(f"{self.DatabaseName}['{SessionId}'] = "+"{'auth': "+f"{Value}"+", 'Cardapio': "+f"['{Item}']"+"}")

PythonDB('MemoryCard').CreateDataBase()
PythonDB('MemoryCard').CreateTable('Jaozin')
PythonDB('MemoryCard').authValue('Jaozin', 1, Item=['batata', 'danone', 'requeijao'])
