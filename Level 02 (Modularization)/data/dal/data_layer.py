import mysql.connector as mysql

HOST = "localhost"
DATABASE = "medium_clone"
USER = "YOUR_USER"
PASSWORD = "YOUR_PASSWORD"


class DataAccessor:
    """
    Class to handle data access using mysql.connector
    """

    def __init__(self):
        self.cnx = mysql.connect(
            host=HOST, database=DATABASE, user=USER, password=PASSWORD
        )

    @staticmethod
    def __handle_where(where_row):
        return " \nWHERE " + "\n  AND ".join(
            f" {col}='{value!s}'" for col, value in where_row.items()
        )

    def read(self, table, columns=None, where_row=None):
        """
        Executes a SELECT statement against table.

        Arguments:
        table                -- name of the table to be read
        columns (optional)   -- list of columns to be read from table
        where_row (optional) -- dict used to build WHERE clause

        Returns: list of rows returned from the SELECT statement.
        """

        stmt = (
            "SELECT " + ", ".join(columns) + f" \nFROM {table}"  # from clause
            if columns
            else "SELECT *"
            # from clause
            f"\nFROM {table}"
        )

        # where clause
        if where_row:
            stmt += self.__handle_where(where_row)

        # submit and return results
        csr = self.cnx.cursor(dictionary=True, buffered=True)
        execute_query = csr.execute(stmt)
        result = csr.fetchall()
        csr.close()

        return result

    def insert(self, table, values):
        """
        Executes an INSERT statement against table.

        Arguments:
        table  -- name of the table to be written to
        values -- list of rows (dicts) to be inserted

        Returns: Number of rows inserted.
        """
        # build list of column names
        cols = values[0].keys()

        # generate insert statement
        stmt = (
            f"INSERT INTO {table} (create_at,"
            + ",".join(col for col in cols)
            + ") VALUES "
            + ",\n".join(
                [
                    "(now(), "
                    + (", ".join("'" + row[value] + "'" for value in row))
                    + ")"
                    for row in values
                ]
            )
        )

        # submit
        csr = self.cnx.cursor(dictionary=True)
        execute_query = csr.execute(stmt)
        self.cnx.commit()
        modified_rows = csr.rowcount
        csr.close()

        # return stmt
        return print(f"{modified_rows} Rows Affected")

    def update(self, table, values, where_row=None):
        """
        Executes an UPDATE statement against a table.

        Arguments:
        table                -- name of the table to be updated
        values               -- dict of columns and values to update
        where_row (optional) -- dict used to build WHERE clause

        Returns: Number of rows updated.
        """
        # generate update statement
        stmt = f"UPDATE {table} SET " + ", ".join(
            f"{col}='{value!s}'" for col, value in values.items()
        )

        if where_row:
            stmt += self.__handle_where(where_row)

        # submit
        csr = self.cnx.cursor(dictionary=True)
        execute_query = csr.execute(stmt)
        self.cnx.commit()
        modified_rows = csr.rowcount
        csr.close()

        return print(f"{modified_rows} Rows Affected")

    def delete(self, table, where_row=None):
        """
        Executes a DELETE statement against a table.

        Arguments:
        table                -- name of the table to be deleted
        where_row (optional) -- dict used to build WHERE clause

        Returns: Number of rows deleted.
        """
        # generate delete statement
        stmt = f"DELETE FROM {table}"

        # where clause
        if where_row:
            stmt += self.__handle_where(where_row)

        # submit
        csr = self.cnx.cursor(dictionary=True)
        execute_query = csr.execute(stmt)
        self.cnx.commit()
        deleted_rows = csr.rowcount
        csr.close()

        return print(f"{deleted_rows} rows affected")
