import sqlite3


class DataBase:
    def consulta(self, sql):
        with sqlite3.connect("BaseDatos/Anahi.db") as conn:
            self.cursor = conn.cursor()
            resultado = self.cursor.execute(sql)
            conn.commit()
            return resultado
