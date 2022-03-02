import happybase
import csv

connection = happybase.Connection()

# before first use:
connection.open()
print(connection.tables())

table = connection.table('mytable')

table.put(b'row-key', {b'cf1': b'value1',
                       b'cf2': b'value2'})

row = table.row(b'row-key')
print(row[b'cf1'])  # prints 'value1'

for key, data in table.rows([b'row-key-1', b'row-key-2']):
    print(key, data)  # prints row key and data for each row

for key, data in table.scan(row_prefix=b'row'):
    print(key, data)  # prints 'value1' and 'value2'

row = table.delete(b'row-key')
