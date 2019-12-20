import xml.etree.ElementTree as ET

def xml_to_txt(indir, outdir):
    f = open(indir)
    f_w = open(outdir, "a")
    tree = ET.parse(f)
    treeroot = tree.getroot()
    textbody = treeroot.find("text").find("body")
    seperator = " "
    for book in textbody.iter("div"):
        for chapter in book.iter("div"):
            for sentence in chapter.iter("seg"):
                plaintext = sentence.text
                s = plaintext.split()
                plaintext = seperator.join(s)
                f_w.write(plaintext+"\n")

inputpath = input("Input the path for your xml corpus: ")
outputpath = input("Input the path for output file: ")
xml_to_txt(inputpath, outputpath)
print("Succeeded.")
