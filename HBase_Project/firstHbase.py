import happybase
import csv

connection = happybase.Connection()

# before first use:
connection.open()
print(connection.tables())

connection.create_table(
    'mytable1',
    {'cf1': dict(max_versions=1),
     'cf2': dict(max_versions=1),  # use defaults
    }
)
