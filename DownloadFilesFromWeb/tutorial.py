import urllib.request

url = "http://www.sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv"

def downloadFile(url) :
    response = urllib.request.urlopen(url) # connection is stored in response
    csv = response.read()
    csv_str = str(csv)
    fw = open("Data.csv", "w")
    array = csv_str.split("\\n")
    for f in array :
        fw.write(f + "\n")
    fw.close()

downloadFile(url)
