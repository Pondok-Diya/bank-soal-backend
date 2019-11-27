from passlib.hash import pbkdf2_sha256 as pbh
from flask_restful import Resource
from flask import request
from app.db import Database
from app import app


class Soal(Resource):
    def get(self):
        """
        Mengeluarkan soal
        """
        sql = """select * from soal"""
        return Database().get_data(sql,[])
    def post(self):
        """
        Menambahkan soal 
        """
        data = request.get_json()
        sql = """insert into soal values(0,%s,%s,%s)"""
        params = [data["judul"],pbh.hash(data["kunci_jawaban"]),data["deskripsi"]]
        return Database().commit_data(sql,params)
    def put(self,id):
        """
        Memperbaharui soal
        """
        data = request.get_json()
        sql = """update soal set judul = %s, kunci_jawaban = %s, deskripsi = %s where id = %s"""
        params = [data["judul"],pbh.hash(data["kunci_jawaban"]),data["deskripsi"],id]
        return Database().commit_data(sql,params)
    def delete(self,id):
        """
        Menghapus soal
        """
        sql = """delete from soal where id = %s"""
        params = [id]
        return Database().commit_data(sql,params)


class Jawab(Resource):
    def post(self):
        """
        Memeriksa jawaban return True jika jawaban benar dan return
        False jika jawaban salah
        """
        data = request.get_json()
        sql = """select * from soal where idsoal = %s"""
        hasil = Database().get_one(sql,[data["idsoal"]])
        if pbh.verify(data["jawaban"],hasil["kunci_jawaban"]):
            return {"msg":"selamat jawaban anda benar"}
        else:
            return {"msg":"maaf jawaban anda salah"}
        