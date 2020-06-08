import requests
import os
from bs4 import BeautifulSoup


def createSubReport(url, nameLeft, nameRight, path):
    # Create directory if it doesn't already exist
    try:
        # Create target Directory
        os.mkdir(path + 'Reports')
    except FileExistsError:
        print()

    # Removing '/' from the file path to be used as a file name later
    nameLeft = nameLeft.replace('/', '_')
    nameRight = nameRight.replace('/', '_')

    # Getting HTML of the main Report
    mainReport = requests.get(url)

    soup = BeautifulSoup(mainReport.content, 'html.parser')

    # Finding all instances of 'frame' in the html code
    pages = soup.find_all('frame')

    # Extracting the src attributes
    pageTop = pages[0].attrs['src']
    pageLeft = pages[1].attrs['src']
    pageRight = pages[2].attrs['src']

    # Extracting the base url
    url = url[0:url.find('match')]

    # Creating the html doc for the Top section of full report
    pageTop = requests.get(url + pageTop)
    filePageTop = open(path + 'Reports/' + nameLeft + '_VS_' + nameRight + '_TOP.html', 'wb')
    filePageTop.write(pageTop.content)
    filePageTop.close()

    # Creating the html doc for the Left section of full report
    pageLeft = requests.get(url + pageLeft)
    filePageLeft = open(path + 'Reports/' + nameLeft + '_VS_' + nameRight + '_LEFT.html', 'wb')
    filePageLeft.write(pageLeft.content)
    filePageLeft.close()

    # Creating the html doc for the Right section of full report
    pageRight = requests.get(url + pageRight)
    filePageRight = open(path + 'Reports/' + nameLeft + '_VS_' + nameRight + '_RIGHT.html', 'wb')
    filePageRight.write(pageRight.content)
    filePageRight.close()

    # HTML code for the full sub report html doc
    html = f"""
        <html>
        <head>
            <title>Matches for submission/np_summary2.py and submission/np_summary_Copy2.py</title>
        </head>
        <frameset rows="150,*">
            <frameset cols="1000,*">
                <frame src=\"{nameLeft + '_VS_' + nameRight + '_TOP.html'}\" name="top" frameborder="0">
            </frameset>
            <frameset cols="42%,58%">
                <frame src=\"{nameLeft + '_VS_' + nameRight + '_LEFT.html'}\" name="0">
                <frame src=\"{nameLeft + '_VS_' + nameRight + '_RIGHT.html'}\" name="1">
            </frameset>
        </frameset>
    </html>
    """

    # Creating the html doc for the full sub report.
    fullReport = open(path + 'Reports/' + nameLeft + '_VS_' + nameRight + '_FULL.html', 'wb')
    fullReport.write(html.encode())
    fullReport.close()

    # Returning path to the sub report
    return 'Reports/' + nameLeft + '_VS_' + nameRight + '_FULL.html'
