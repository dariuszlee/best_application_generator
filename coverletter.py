from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-c", "--company", help="Help text")
parser.add_argument("-i", "--hirer", default="whom it may concern", help="Help text")
parser.add_argument("-p", action="store_true")

a = parser.parse_args()

if a.p:
    filePath = "./templates/general_dev_pdf.md"
else:
    filePath = "./templates/general_dev.md"

with open(filePath) as f:
    fStr = "".join(f.readlines())
    formatted = fStr.format(company=a.company, hirer=a.hirer)
    print(formatted)
