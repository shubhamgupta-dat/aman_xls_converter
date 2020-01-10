from argparse import ArgumentParser
from pandas import read_excel

ip_parser = ArgumentParser(description="To convert Dms file from xls/xlsx to csv")
ip_parser.add_argument('file',help='file name in xls/xlsx')
args = vars(ip_parser.parse_args())

# header_columns = ['Srl.', 'Follow-up Type', 'Follow-up Number', 'Follow up Due Date',
#        'Follow up Actual Date', 'Regn. No.', 'Model Name', 'Fuel Type',
#        'Chassis No.', 'Mileage', 'Due Date', 'Due Service', 'Last Service',
#        'Last Service.1', 'Sale Date', 'Cust. Catg.', 'Customer Name',
#        'Address', 'Telephone No.', 'Mobile No.', 'Customer Contact Status',
#        'Current JC', 'Service Type', 'Status', 'Next Followup Date',
#        'Engine No.', 'Customer Pick-Up Type', 'Customer Email id Status',
#        'Last Followup Remarks', 'Followup Remarks', 'Followup Response',
#        'Delivery Date (Sale)', 'Pickup/Drop', 'Ext. Warranty', 'MI Contact',
#        'Loyalty Card', 'Loyalty Card Balance', 'As On Date']

file_name = '.'.join(args['file'].split('.')[:-1])

df_raw = read_excel(args['file'],
                    skiprows=8,
                    #header = header_columns,
                    header=None
                   )

df_raw.to_csv(f'{file_name}.csv',index=False)

print(f"{file_name}.csv is created.")
