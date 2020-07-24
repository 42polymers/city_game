import configparser
import os


CONFIG_PATH = os.getenv('CONFIG_PATH')
if not CONFIG_PATH:
    raise Exception('CONFIG_PATH environment variable must be set')
conf = configparser.ConfigParser()
conf.read(CONFIG_PATH)

bot_id = conf['telegram']['BOT_ID']
database = conf['database']
media = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media'))
