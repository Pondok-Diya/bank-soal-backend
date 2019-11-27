from app import api
from app.controller.soal import Soal
from app.controller.soal import Jawab

api.add_resource(Soal,'/soal')
api.add_resource(Jawab,'/soal/jawab')