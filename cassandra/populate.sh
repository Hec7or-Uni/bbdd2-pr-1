cqlsh -u cassandra -p cassandra < createTable.cql
cqlsh -u cassandra -p cassandra < users.cql
cqlsh -u cassandra -p cassandra < MOCK_DATA_BOOKS.cql
cqlsh -u cassandra -p cassandra < MOCK_DATA_USERS.cql
cqlsh -u cassandra -p cassandra < MOCK_DATA_RENT_BY_BOOK.cql
cqlsh -u cassandra -p cassandra < MOCK_DATA_RENT_BY_USER.cql