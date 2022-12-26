# WriteUp
userid와 password를 double-check 하기 때문에 blind sql injection을 통해 실제 admin의 비밀번호를 알아내야 한다. 
 
blind sql injection 을 하기 위해 필터링된 명령어를 사용하지 않고 (또는 우회해서) 인젝션을 사용해야 한다. 
```python
SQL_BAN_LIST = [
    'update', 'extract', 'lpad', 'rpad', 'insert', 'values', '~', ':', '+',
    'union', 'end', 'schema', 'table', 'drop', 'delete', 'sleep', 'substring',
    'database', 'declare', 'count', 'exists', 'collate', 'like', '!', '"',
    '$', '%', '&', '+', '.', ':', '<', '>', 'delay', 'wait', 'order', 'alter'
]
``` 

