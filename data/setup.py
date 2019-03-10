import sys
from cx_Freeze import setup, Executable

setup(
	name = "Sneakers" ,
	version = "0.1" , #Versiyonu
	description = "Sneakers Çekici" ,
	executables = [Executable("calistir.py", base = "Win32GUI")])