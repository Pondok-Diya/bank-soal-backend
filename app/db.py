import pymysql
from app import app

class Database:
    def koneksi(self):
        db = pymysql.connect('localhost','root','root','belajar')
        return db
    def get_data(self,sql,params=[]):
        """
        Mengeluarkan beberapa records dari database berdasarkan query(sql)
        dan parameternya(params) dalam bentuk list dengan elemen berupa dictionary
        """
        try:
            con = self.koneksi()
            cur = con.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql,params)
            hasil = cur.fetchall()
            con.close()
            return hasil
        except Exception as e:
            app.logger.error(e,exc_info=True)
            return {"msg":"terjadi kesalahan"},500
    def get_one(self,sql,params=[]):
        """
        Mengeluarkan sebuah record dari database berdasarkan query(sql)
        dan parameternya(params) dalam bentuk dictionary
        """
        try:
            con = self.koneksi()
            cur = con.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql,params)
            hasil = cur.fetchone()
            con.close()
            return hasil
        except Exception as e:
            app.logger.error(e,exc_info=True)
            return {"msg":"terjadi kesalahan"},500
    def commit_data(self,sql,params=[]):
        try:
            con = self.koneksi()
            cur = con.cursor(pymysql.cursors.DictCursor)
            hasil = cur.execute(sql,params)
            print(hasil)
            con.commit
            con.close()
            return {'msg':'Sukses'}
        except Exception as e:
            app.logger.error(e,exc_info=True)
            return {"msg":"terjadi kesalahan"},500