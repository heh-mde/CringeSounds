from cx_Freeze import setup, Executable

executables = [Executable('code/GUI.py')]

setup(name='CringeSounds',
      version='0.1.0',
      description='SoundBoard App',
      executables=executables)