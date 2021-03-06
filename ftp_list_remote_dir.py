from ftplib import FTP
import yaml
import sys

# Jenkins execution; second parameter
if len(sys.argv) == 2:
    config_data = str(sys.argv[1])

#Console execution with params; first parameter
elif len(sys.argv) == 1:
    config_data = str(sys.argv[0])

#If no params, test execution to ftp.es.debian.org
elif len(sys.argv) == 0:
    config_data = yaml.load(open('ftp_connection_params.yml', 'r'))

ftp = FTP(config_data['ftp_host'])
ftp.login(config_data['ftp_username'], config_data['ftp_password'])

print ftp.getwelcome()

for ftp_directory in config_data['ftp_final_dir']:

    ftp.cwd(ftp_directory)

    for pattern in config_data['ftp_patterns']:
        try:
            files = ftp.nlst(pattern)
        except ftp.error_perm, resp:
            if str(resp) == "550 No files found":
                pass

        for file in files:
            print ftp_directory, file

ftp.quit()