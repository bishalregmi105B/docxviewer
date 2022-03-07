from docx2pdf import convert
toconvname="xyz.docx"
convname="xyz.pdf"
def conv():
    convert(toconvname,convname)
    return convname
