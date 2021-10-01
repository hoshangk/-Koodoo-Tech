import csv
import logging
import requests
from bs4 import BeautifulSoup

# Defining the basic Settings for the logs
logging.basicConfig(
    filename="script.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)


def writeCSV(outputFile, columnFields, data):
    """
    Function to Write the extracted Data into CSV File
    :return: True
    """
    #  writing to csv file
    with open(outputFile, "w", newline="") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(columnFields)

        # writing the data rows
        csvwriter.writerows(data)

        return True


def main(url):
    """
    Function will hit the url and will get all response
    :return:
    """
    # name of csv file

    try:
        logging.info(f"Reading data from url {url}")
        urlContent = requests.get(url)
        soup = BeautifulSoup(urlContent.text, "lxml")
        print(soup.findAll("title"))
        top_stories_list = []
        outputFile = "top_stories_only_headers.csv"
        columnFields = ["Top Story Title"]
        for each in soup.findAll("title"):
            title = each.text.split("-")[1:]
            top_story = "".join(title)
            top_stories_list.append([top_story.strip()])

        writeCSV(outputFile, columnFields, top_stories_list)

        # Writing Tope Sories with More Content
        outputFile = "top_stories_all_data.csv"
        columnFields = ["Top Stories", "pubDate"]
        data = list()
        for item in soup.findAll("item"):
            title = item.title.text.split("-")[1:]
            top_story = "".join(title)
            pubDate = item.pubdate.text
            data.append([top_story, pubDate])

        writeCSV(outputFile, columnFields, data)

    except Exception as e:
        logging.error(e)

    finally:
        urlContent.close()


if __name__ == "__main__":
    url = "https://www.europarl.europa.eu/rss/doc/top-stories/en.xml"
    main(url)
