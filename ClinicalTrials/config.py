import ConfigParser
import os.path 
 
def config(filename='database.ini', section='postgresql'):
    HERE = os.path.abspath(os.path.dirname(__file__))
    CONFIG_PATH = os.path.join(HERE, filename)
    print(os.path.isfile(CONFIG_PATH))
    # create a parser
    parser = ConfigParser.RawConfigParser()
    # read config file
    parser.read(CONFIG_PATH)
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db