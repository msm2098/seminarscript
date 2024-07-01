import requests
from sql import database;
from table import table_name;
from column import column;
from data import get_data;
dbname = database();
print("DB name : ",dbname);
table_names = table_name(dbname);

print("Table names:", ', '.join(table_names))

col = []
print_col=[];
for i in table_names:
    print_col.append(i+':')
    print_col.append(column(dbname,i))

    col .append(column(dbname,i))

print("Column names")
print(*print_col, sep = ' ')
