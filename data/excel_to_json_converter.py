import xlrd
from collections import OrderedDict
import simplejson as json

# extract workbook from excel file
wb = xlrd.open_workbook("<relative path to excel file>") # put here relative path to excel file

# extract required sheet by index from workbook
sh = wb.sheet_by_index(0)

data_list = []

delimiter = '<sep>' # <sep> is used as delimiter in excel files to avoid confusion with comma

for row_num in range(1, sh.nrows):
    data = OrderedDict()

    row_values = sh.row_values(row_num)
    data['tag'] = row_values[0]

    data['patterns'] = [x.strip() for x in row_values[1].split(delimiter)]
    data['responses'] = [x.strip() for x in row_values[2].split(delimiter)]

    # if some reponse has not yet been written then keep it's tag as temporary response for testing purpose
    if (data['responses'] == ["***to_do***"] or data['responses'] == [""]):
        data['responses'] = [data['tag']+" (response is yet to be written!)"]

    data['context'] = [""]
    data_list.append(data)

data_list = {'intents': data_list}

with open('<path to json file to save data>', 'w') as f: # put here relative path to json file in which data (intents) are to be saved
    json.dump(data_list, fp=f, indent=4)

