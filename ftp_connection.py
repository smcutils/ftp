from ftplib import FTP
import yaml

config_data = yaml.load(open('ftp_connection_params.yml', 'r'))

ftp = FTP(config_data['ftp_host'])
ftp.login(config_data['ftp_username'], config_data['ftp_password'])

print ftp.getwelcome()

ftp.quit()