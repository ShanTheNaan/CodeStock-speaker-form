import MySQLdb

class MySQLHelper:
  def __init__(self):
    self._passwd = self.__set_passwd()
    self._username = 'root'
    self._host = 'hlr710vm.homelinux.com' 
    self._port = 3306
    self._db = 'cmawhinn_codestock'
    self.conn = None
    self.curse = self.__connect_to_db()


  def __set_passwd(self):
    with open('password.txt', 'r') as fp:
      return fp.readline().strip('\n')

  
  def __connect_to_db(self):
    print(self._passwd)
    conn = MySQLdb.connect(host=self._host, port=self._port,
        user=self._username, passwd=self._passwd, db=self._db)

    self.conn = conn
    return conn.cursor()

  def query_db(self, query):
    num_rows = self.curse.execute(query)
    self.conn.query(query)
    r = self.conn.store_result()
    rows = r.fetch_row(maxrows=0)

    return rows


  def get_all_talks_for_user(self, uid):
    query = "SELECT bt.TalkId, tt.EventTitle, st.FirstName, st.LastName FROM \
      bridge_table bt INNER JOIN talk_table tt ON tt.TalkId = bt.TalkId INNER JOIN \
      speaker_table st ON st.SpeakerId = bt.SpeakerId WHERE bt.SpeakerId=" + str(uid)

    self.conn.query(query)  
    r = self.conn.store_result()
    rows = r.fetch_row(maxrows=0)


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
