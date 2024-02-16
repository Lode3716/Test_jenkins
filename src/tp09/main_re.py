"""
   
 auth : l.devigne

"""
import re
from glob import glob



def main():
    logs = glob('*.log')
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                # ip_result = re.findall(r"^(.+?)\s", line)
                code_retour_html = re.findall(r"\"\s(\d{3})\s", line)

                print(code_retour_html)


if __name__ == '__main__':
    main()
