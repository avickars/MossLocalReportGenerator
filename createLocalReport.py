from createSubReport import createSubReport
from bs4 import BeautifulSoup
import requests
import sys

html = requests.get(sys.argv[1])
soup = BeautifulSoup(html.content,features="lxml")

subReportUrls = soup.find('table').find_all('a')

# Extracting the number of lines matched in each comparison
numLinesMatched = soup.find('table').find_all('td',{'align':'right'})

# Extracting report date and options
headerInfo = soup.find_all('p')
date = headerInfo[0].contents[0]
options = headerInfo[1].contents[0]

reportHTMLTop = f"""
<!DOCTYPE html>
<html>
	<head>
		<title> Moss Results </title>
	</head>

	<body>
		Moss Results
        <p> {date} </p>
        <p> {options} </p>
		<hr>
			<a href="http://moss.stanford.edu/general/format.html" target="_top"> How to Read the Results</a>
			<a href="http://moss.stanford.edu/general/tips.html" target="_top"> Tips</a>
			<a href="http://moss.stanford.edu/general/faq.html"> FAQ</a>
			<a href="mailto:moss-request@cs.stanford.edu">Contact</a>
			<a href="http://moss.stanford.edu/general/scripts.html">Submission Scripts</a>
			<a href="http://moss.stanford.edu/general/credits.html" target="_top"> Credits</a>
		<hr>
		<table>
			<tbody>
				<tr>
					<th>File 1</th>
					<th>File 2</th>
					<th>Lines Matched</th>
				</tr>
"""

reportHTMLBottom = """
			</tbody>
		</table>
	</body>
</html>
"""

# Iterating through all of the urls ?to the sub reports, and passing to createSubReport function to create the Sub Reports
for i in range(0, len(subReportUrls), 2):
    nameLeft = subReportUrls[i].contents[0]
    nameRight = subReportUrls[i + 1].contents[0]
    linesMatched = numLinesMatched[int(i/2)].contents[0]
    reportLocation = createSubReport(subReportUrls[i].attrs['href'], nameLeft[:-6], nameRight[:-6])
    reportHTMLTop = reportHTMLTop + f"""<tr><td> <a href={reportLocation}> {nameLeft} </a> </td>""" + f"""<td> <a href={reportLocation}> {nameRight} </a> </td>""" + f"""<td align=\"right\">{linesMatched}</td> </tr>"""

reportHTMLTop = reportHTMLTop + reportHTMLBottom
mossReport = open('mossReport.html', 'wb')
mossReport.write(reportHTMLTop.encode())
mossReport.close()
