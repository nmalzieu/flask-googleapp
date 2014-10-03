import os

### DATABASE SETTINGS ###

DATABASE = os.environ.get('DATABASE_URL', "mysql+gaerdbms:///mydb?instance=whiteout-cloud-platform:mydb?charset=utf8")
