import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from . import send_email

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

DIRNAME = os.path.dirname(__file__)

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    os.path.join(DIRNAME, 'python_drive_key.json'), scope)

client = gspread.authorize(credentials)

modif_val = client.open("Modify_Values_Sheet").sheet1

def change_format(value):
    spl = value.split(':')
    hh = spl[0]
    mm = spl[1]
    
    return hh + "h" + mm + "min"

def update_values(color, reader, tag, area):

    #Test fail cases here

    reader_spl = reader.split(':')
    tag_spl = tag.split(':')
    area_spl = area.split(':')

    if ":" not in reader or ":" not in tag or ":" not in area:
        return "Please enter values in the correct format!"

    reader_spl.extend(tag_spl)
    reader_spl.extend(area_spl)

    for i in reader_spl:
        if len(i) != 2:
            return "Please enter values in the correct format!"

    reader = change_format(reader)
    tag = change_format(tag)
    area = change_format(area)

    data = modif_val.get_values()
    next_edit_row_available = len(data) + 1

    modif_val.update_cell(next_edit_row_available, 1, color) 
    modif_val.update_cell(next_edit_row_available, 2, reader)
    modif_val.update_cell(next_edit_row_available, 3, tag)
    modif_val.update_cell(next_edit_row_available, 4, area)

    send_email.send_email_ftn(color, reader, tag, area)
    
    return "Updated Successfully!"