import os
import configparser
from PySide6.QtCore import QObject, Signal
class shared_manager(QObject):
    _instance = None
    ip_changed = Signal(str)
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
            return cls._instance
    def _load_config(self):
        self.config = configparser.ConfigParser()
        self.config_file = ("config.ini")
        if not os.path.exists(self.config_file):
            self.config["NETWORK"] = {"ip":"127.0.0.1"}
            self._save_config()
        else:
            self.config.read(self.config_file)
    def _save_config(self):
        with open (self.config_file, "w") as f:
            self.config.write(f)
    @property
    def ip(self):
        return self.config["NETWORK"]["ip"]
    @ip.setter
    def ip(self, value):
        self.config["NETWORK"]["ip"] = value
        self._save_config()
        self.ip_changed.emit(value)
shared = shared_manager()
