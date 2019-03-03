import sqlalchemy

class MySQLHelper:
  def __init__(self):
    self._passwd = self.__set_passwd()
    self._username = 'root'
    self._host = 'hlr710vm.homelinux.com' 
    self._port = 3306
    self._db = 'cmawhinn_codestock'
    self.conn = self.__connect_to_db()


  def __set_passwd(self):
    with open('password.txt', 'r') as fp:
      return fp.readline().strip('\n')

  
  def __connect_to_db(self):
    engine = sqlalchemy.create_engine('mysql://' + self._username + ':' + 
        self._passwd + '@' + self._host + ':' + repr(self._port) + '/' + self._db,
        encoding='utf-8', echo=True)

    return engine.connect()
    

  def query_db(self):
    query = select([cols.created_at,
      cols.name]).order_by(cols.created_at).limit(1)

    for row in self.conn.execute(query):
      print(row)


  def get_passwd(self):
    return self._passwd


  def get_username(self):
    return self._username


  def get_host(self):
    return self._host


  def get_port(self):
    return self._port


  def get_db(self): 
    return self._db
