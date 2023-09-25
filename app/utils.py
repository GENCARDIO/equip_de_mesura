import pandas as pd
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import re
import subprocess
import zipfile
from flask import send_file


def llegir_excel(path_excel):
    path_excel = "/home/gencardio/Baixades/LDG_REG_202_INVENTARI APARELLS_V6.xlsx"
    data = pd.read_excel(path_excel, skiprows=4)
    filas = data.to_numpy().tolist()
    return filas


def create_docx(data):

    doc = DocxTemplate("app/templates/fitxa_tecnica_template.docx")
    report_name = data["codi_aux"] + ".docx"

    # print(data["img_1"])
    img_1 = InlineImage(doc, image_descriptor='app/static/' + data["img_1"], width=Mm(20), height=Mm(20))
    img_2 = InlineImage(doc, image_descriptor='app/static/' + data["img_2"], width=Mm(20), height=Mm(20))
    img_3 = InlineImage(doc, image_descriptor='app/static/' + data["img_3"], width=Mm(20), height=Mm(20))

    patro_data = r'^\d{4}-\d{2}-\d{2}$'
    data_alta_aux = data["data_alta"]
    if re.match(patro_data, data_alta_aux[:10]):
        data_alta = data_alta_aux[:10]
    else:
        data_alta = data["data_alta"]
    data_baixa_aux = data["data_baixa"]
    if re.match(patro_data, data_baixa_aux[:10]):
        data_baixa = data_baixa_aux[:10]
    else:
        data_baixa = data["data_baixa"]

    body = {
        "codi_aux": data["codi_aux"],
        "descripcio": data["descripcio"],
        "fabricant": data["fabricant"],
        "ref_fabricant": data["ref_fabricant"],
        "serial_number": data["serial_number"],
        "model": data["model"],
        "emp_subministradora": data["emp_subministradora"],
        "servei_tecnic": data["servei_tecnic"],
        "telefon": data["telefon"],
        "img_1": img_1,
        "data_alta": data_alta,
        "condicions_equip": data["condicions_equip"],
        "data_baixa": data_baixa,
        "situacio_contractual": data["situacio_contractual"],
        "preu": data["preu"],
        "tipus": data["tipus"],
        "img_2": img_2,
        "amplada": data["amplada"],
        "alçada": data["alçada"],
        "profunditat": data["profunditat"],
        "pes": data["pes"],
        "volum": data["volum"],
        "condicions_ambientals": data["condicions_ambientals"],
        "humitat": data["humitat"],
        "presa_aigua": data["presa_aigua"],
        "img_3": img_3,
        "marca_pantalla": data["marca_pantalla"],
        "model_pantalla": data["model_pantalla"],
        "num_serie_pantalla": data["num_serie_pantalla"],
        "codi_pantalla": data["codi_pantalla"],
        "marca_sai": data["marca_sai"],
        "model_sai": data["model_sai"],
        "num_serie_sai": data["num_serie_sai"],
        "codi_sai": data["codi_sai"],
        # Cont Comercial: data[?],
        # Cont Tecnic: data[?],
        # Observacions: data[?],
        "marca_lector": data["marca_lector"],
        "model_lector": data["model_lector"],
        "num_serie_lector": data["num_serie_lector"],
        "codi_lector": data["codi_lector"],
        "marca_impresora": data["marca_impresora"],
        "model_impresora": data["model_impresora"],
        "num_serie_impresora": data["num_serie_impresora"],
        "codi_impresora": data["codi_impresora"],
        "marca_tensio": data["marca_tensio"],
        "model_tensio": data["model_tensio"],
        "num_serie_tensio": data["num_serie_tensio"],
        "codi_tensio": data["codi_tensio"],
        "soft_1": data["soft_1"],
        "versio_1": data["versio_1"],
        "soft_2": data["soft_2"],
        "versio_2": data["versio_2"],
        "soft_3": data["soft_3"],
        "versio_3": data["versio_3"],
        "soft_4": data["soft_4"],
        "versio_4": data["versio_4"],
        "soft_5": data["soft_5"],
        "versio_5": data["versio_5"],
        "personal_tecnic_udmmp": data["personal_tecnic_udmmp"],
        "facultatius_udmmp": data["facultatius_udmmp"],
        "personal_tecnic_udmmp_2": data["personal_tecnic_udmmp_2"],
        "facultatius_udmmp_2": data["facultatius_udmmp_2"],
        "personal_tecnic_udmmp_3": data["personal_tecnic_udmmp_3"],
        "facultatius_udmmp_3": data["facultatius_udmmp_3"],
        "personal_tecnic_udmmp_4": data["personal_tecnic_udmmp_4"],
        "facultatius_udmmp_4": data["facultatius_udmmp_4"],
        "personal_tecnic_udmmp_5": data["personal_tecnic_udmmp_5"],
        "facultatius_udmmp_5": data["facultatius_udmmp_5"],
        "ref_fung1": data["ref_fung1"],
        "desc_fung1": data["desc_fung1"],
        "ref_fung2": data["ref_fung2"],
        "desc_fung2": data["desc_fung2"],
        "ref_fung3": data["ref_fung3"],
        "desc_fung3": data["desc_fung3"],
        "ref_fung4": data["ref_fung4"],
        "desc_fung4": data["desc_fung4"],
        "ref_fung5": data["ref_fung5"],
        "desc_fung5": data["desc_fung5"],
        "doc1": data["doc1"],
        "doc2": data["doc2"],
        "cont_manteniment": data["cont_manteniment"],
        "manteniment_ext": data["manteniment_ext"],
        "manteniment_int": data["manteniment_int"],
        "verificacio_int": data["verificacio_int"],
        "verificacio_ext": data["verificacio_ext"],
        "cal_ext": data["cal_ext"],
        "cal_int": data["cal_int"],
        "nom_contracte": data["nom_contracte"],
        "emp_respon1": data["emp_respon1"],
        "periode_cober1": data["periode_cober1"],
        "dades_cont1": data["dades_cont1"],
        "emp_respon2": data["emp_respon2"],
        "periode_cober2": data["periode_cober2"],
        "dades_cont2": data["dades_cont2"],
        "emp_respon_prev_ext": data["emp_respon_prev_ext"],
        "periodicitat_prev_ext": data["periodicitat_prev_ext"],
        "cont_prev_ext": data["cont_prev_ext"],
        "mant_prev_ext": data["mant_prev_ext"],
        "verif_prev_ext": data["verif_prev_ext"],
        "calib_prev_ext": data["calib_prev_ext"],
        "marges_accept_prev_ext": data["marges_accept_prev_ext"],
        "desc_prev_int": data["desc_prev_int"],
        "periodicitat_prev_int": data["periodicitat_prev_int"],
        "marges_accept_prev_int": data["marges_accept_prev_int"],
        "desc_verif_int": data["desc_verif_int"],
        "periodicitat_verif_int": data["periodicitat_verif_int"],
        "marges_accept_verif_int": data["marges_accept_verif_int"],
        "calib_desc_int": data["calib_desc_int"],
        "calib_periodicitat_int": data["calib_periodicitat_int"],
        "calib_marges_accept_int": data["calib_marges_accept_int"],
    }

    context = {"body": body}
    doc.render(context)
    doc.save("app/docx/" + report_name)
    return "app/docx/" + report_name, data["codi_aux"]


def create_pdf(docx, report_name):

    path_docx = docx
    path_pdf = "app/pdfs/" + report_name + ".pdf"

    subprocess.run(["unoconv", "-f", "pdf", "-o", path_pdf, path_docx])


def zip_files(file, file_2, zip_name):

    arxius = [file, file_2]
    zip = zip_name + ".zip"
    path_zip = "zips/" + zip

    with zipfile.ZipFile(path_zip, 'w') as arxiu_zip:
        for arxiu in arxius:
            arxiu_zip.write(arxiu)

    return send_file(path_zip, as_attachment=True)
