import ftplib
import os
from glob import glob
from datetime import datetime as dt


local_ftp_dir = '../ftp/'
local_ftp_config = 'ftp_config.txt'

ftp_int = {'host':'','user':'','pass':'','dir':''}
ftp_ext = {'host':'','user':'','pass':'','dir':''}


def import_ftp_creds():
    #server_cred_file = os.path.join(local_ftp_dir,local_ftp_config)
    server_cred_file = local_ftp_config
    with open(server_cred_file,'r') as f:
        global ftp_int
        ftp_int['host'] = f.readline().rstrip('\n')
        ftp_int['user'] = f.readline().rstrip('\n')
        ftp_int['pass'] = f.readline().rstrip('\n')
        ftp_int['dir']  = f.readline().rstrip('\n')
        f.readline()
        global ftp_ext
        ftp_ext['host'] = f.readline().rstrip('\n')
        ftp_ext['user'] = f.readline().rstrip('\n')
        ftp_ext['pass'] = f.readline().rstrip('\n')
        ftp_ext['dir']  = f.readline().rstrip('\n')
    return None
        

def connect_to_available_server():
    # try internal ftp then external
    try:
        ftp = ftplib.FTP()
        ftp.connect(ftp_int['host'])
        ftp.login(ftp_int['user'],ftp_int['pass'])
        ftp.cwd(ftp_int['dir'])
        print('connected to internal server')
        return ftp
    except:
        ftp = ftplib.FTP()
        ftp.connect(ftp_ext['host'])
        ftp.login(ftp_ext['user'],ftp_ext['pass'])
        ftp.cwd(ftp_ext['dir'])
        print('connected to external server')
        return ftp
    else:
        exit
        

def upload_data(ftp_obj,local_filepath):
    # add timestamp to file
    top_dir = ftp_obj.pwd()
    split_path = local_filepath.split('/')
    filename = split_path[-1]
    stamped_filename = filename.split('.')[0] \
                       + dt.now().strftime('_%Y%m%d_%H%M%S') \
                       + '.' \
                       + filename.split('.')[-1]
    stamped_filepath = local_filepath.replace(split_path[-1],stamped_filename)
    # check directory path and add necessary directories
    for i in range(0, len(split_path)):
        test_path = ''
        for j in range(i):
            if (j>0):
                test_path = test_path + '/'
            test_path = test_path + split_path[j]
        try:
            ftp_obj.cwd(test_path)
        except:
            ftp_obj.mkd(test_path)
        finally:
            while (ftp_obj.pwd() != top_dir):
                ftp_obj.cwd('../')
    # upload data files
    try:
        ftp_obj.storbinary('STOR ' + stamped_filepath,
                           open(local_filepath,'rb'))
        print('uploaded: ' + local_filepath)
        os.remove(local_filepath)
    except Exception as e:
        print(str(e))
    return None


def sync_to_server(ftp_obj):
    files = glob('**/*.*')
    for f in files:
        upload_data(ftp_obj, f)



os.chdir(local_ftp_dir)
import_ftp_creds()
ftp_server = connect_to_available_server()
sync_to_server(ftp_server)














