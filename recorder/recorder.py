# -*- Coding: utf-8 -*-
# Utiles
from .utils import file_exists, random_name, write_file, remove_file
from .models import Audio
from .services import AudioService
from .plugins.audio_help import AudioHelp
from config import Settings, Routes 

class Record():
    """ Clase de grabación de audio. """
    def __init__(self, interface):
        self.routes = Routes()
        self.interface = interface
        self.audio_h = AudioHelp()
        self.listAudios()
        self.filename = None

    def listAudios(self):
        pass


    def recordAudio(self, callback):
        print("Grabando...")
        

    def stopAudio(self):
        print("Deteniendo grabación...")