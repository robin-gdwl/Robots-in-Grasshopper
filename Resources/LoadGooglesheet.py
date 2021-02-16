import io
import requests
import pandas as pd
import pytablereader as ptr
import pytablewriter as ptw


loader = ptr.TableUrlLoader(
    "https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks",
    "html")

google_loader = ptr.GoogleSheetsTableLoader(file_path="https://docs.google.com/spreadsheets/d/1lBCtmcVejfelk-chGjbqxn0pFboY8GZY5a5IoeRNeOg/edit?usp=sharing",
                                            quoting_flags=None,
                                            type_hints=None,
                                            type_hint_rules=None)
writer = ptw.TableWriterFactory.create_from_format_name("rst")
writer.stream = io.open("load_url_result.rst", "w", encoding=loader.encoding)
for table_data in loader.load():
    writer.from_tabledata(table_data)
    # writer.write_table()


sheet = requests.get("https://docs.google.com/spreadsheets/d/1lBCtmcVejfelk-chGjbqxn0pFboY8GZY5a5IoeRNeOg/gviz/tq?tqx=out:csv&sheet=01")
# print(sheet)
# print(sheet.text)
# print(sheet.headers)

# load from a csv text ---
loader = ptr.CsvTableTextLoader(sheet.text)
# for table_data in loader.load():
    # print("\n".join([
        # "load from text",
        # "==============",
        # "{:s}".format(ptw.dumps_tabledata(table_data)),
    # ]))
loaded = loader.load()
for table_data in loaded:
    # print(table_data.as_dataframe())
    print(table_data)
    print(table_data.rows)
    dataframe_01 = table_data.as_dataframe()

def true_to_checkmark(data):
    if isinstance(data, bool):
        if data:
            return ":white_check_mark:"
        else:
            return ":x:"
    else:
        return ":x:"

# for value in dataframe_01['Open_Source']:
    # value = true_to_checkmark(value)
dataframe_01['Open_Source'] = dataframe_01['Open_Source'].apply(true_to_checkmark) 
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(dataframe_01)
# print(dataframe_01) 
# print(loaded.rows)
# print(dir(loaded))
# print(dir(loader))
# print(loader)
writer = ptw.MarkdownTableWriter()
writer.from_csv(sheet.text)
with open("./Resources/sample.md", "w") as f:
    with open('./Resources/Intro.md','r') as intro_file:
        for line in intro_file:
            f.write(line)
    writer.stream = f
    writer.write_table()

# print(writer.headers)
# writer.write_table()

"""
flow: 
get gsheet
write intro 
write table 
write every entry
write outro
"""