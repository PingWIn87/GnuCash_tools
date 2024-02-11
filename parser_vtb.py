import json
import argparse
import pprint
import os


def parse_statement(statement_path):
    try:
        json_file = open(os.path.normpath(statement_path), 'r', encoding="utf8")
        json_data = json.load(json_file)
        return json_data
    except Exception:
        print("Oops!\n"
              "Open file error!\n"
              "Try again...")

def create_table_statement(statement_data):
    table_statement = list()
    for record in statement_data['operations']:
        state_data = dict()
        state_data['date'] = record['eventTime']
        state_data['comment'] = record['fullOperationName']
        if record['debet']:
            state_data['sum'] = -record['operationAmount']['sum']
        else:
            state_data['sum'] = record['operationAmount']['sum']
        table_statement.append(state_data)
    return table_statement

def write_csv(csv_path, statement_data):
    try:
        csv_file = open(os.path.normpath(csv_path), 'w', encoding="utf8")
        for record in statement_data:
            record_sting="{};{};{}\n".format(record['date'],record['sum'],record['comment'])
            csv_file.write(record_sting)
        csv_file.close()
    except Exception:
        print("Oops!\n"
              "Open file error!\n"
              "Try again...")
        csv_file.close()

def clear_self_transfers(csv_file_path):
    lines = list()
    data_file = open(csv_file_path, 'r+', encoding='utf8')
    lines = data_file.readlines()
    data_file.seek(0)
    # truncate the file
    data_file.truncate()
    for line in lines:
        if line.find("Перевод между своими счетами") == -1:
            data_file.write(line)

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename')
parser.add_argument('-d', action = 'store_true', default= False)
args = parser.parse_args()
pprint.pprint(args)
data = parse_statement(args.filename)
statement_table = create_table_statement(data)
csv_file_name = os.path.basename(args.filename).replace(".json", ".csv")
csv_file_path = os.path.normpath("{}/{}".format(os.path.dirname(args.filename),csv_file_name))
write_csv(csv_file_path,statement_table)
if args.d:
    clear_self_transfers(csv_file_path)






