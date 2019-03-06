import sys
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
  
  def __connect_to_db(self):
    print(self._passwd)
    conn = MySQLdb.connect(host=self._host, port=self._port,
        user=self._username, passwd=self._passwd, db=self._db)

    self.conn = conn
    return conn.cursor()


  def __populate_db(self, csv_filename):
    with open(csv_filename, newline='') as csvfile:
      talks = csv.reader(csvfile, delimiter=',', quotechar='|')
      for row in talks: 
        if len(row) < 6: 
          #TODO need to gracefully handle failure
          print('Malformed CSV file')
          sys.exit(1)
        talk_name = row[0]
        talk_date = row[1]
        talk_locn = row[2]
        talk_desc = row[3]
        speakers_first = row[4::2]
        speakers_last  = row[5::2]

        #TODO: Error check -- is this needed? Map will default to inserting
        #'None' in the case where the lists aren't the same size
        if len(speakers_first) != len(speakers_last):
          pass
        for idx, f_name in enumerate(speakers_first):
          #TODO: create query string to enter into db
          pass



  def query_db(self, query):
    num_rows = self.curse.execute(query)
    self.conn.query(query)
    r = self.conn.store_result()
    rows = r.fetch_row(maxrows=0)

    return rows


  def get_all_talks_for_speaker(self, uid):
    query = "SELECT bt.TalkId, tt.EventTitle, st.FirstName, st.LastName FROM \
      bridge_table bt INNER JOIN talk_table tt ON tt.TalkId = bt.TalkId INNER JOIN \
      speaker_table st ON st.SpeakerId = bt.SpeakerId WHERE bt.SpeakerId=" + str(uid)

    self.conn.query(query)  
    r = self.conn.store_result()
    rows = r.fetch_row(maxrows=0)

    print(rows)
    for talk in rows:
      self.conn.query("SELECT * FROM comments_table WHERE TalkId=" + str(talk[0]))
      r = self.conn.store_result()
      talk_rows = r.fetch_row(maxrows=0)
      print(talk_rows)

