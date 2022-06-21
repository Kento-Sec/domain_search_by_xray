import os
import argparse


parser = argparse.ArgumentParser(description="domain_search_by_xray.py")
parser.add_argument("-f", "--file", type=str, metavar="file", help="txt目标路径 eg:\"/XX/XX/xx.txt\"")
args = parser.parse_args()
# 扫描
def get_url(txt):
    file = open(txt,encoding='utf-8',errors = 'ignore')
    for text in file.readlines():
        targeturl=text.strip('\n')
        do_scan(targeturl)

# 报告
def do_scan(targeturl):
    scan_command=r"./xray sd --target {} --text-output domain_output_{}.text".format(targeturl,targeturl)
    print(scan_command)
    os.system(scan_command)
    return

if __name__ == '__main__':
    txt = args.file
    get_url(txt)
