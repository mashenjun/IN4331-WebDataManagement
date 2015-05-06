def selecttweets(Num):
    import csv
    import itertools

    tweetscontent = ''
    i = 1

    uncertaintweets = open('./static/uncertaintweets.csv', 'w', newline='')
    writer = csv.writer(uncertaintweets)

    with open('./static/uncertain.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            tweet = row[0]
            writer.writerow([tweet])
            i = i + 1
            if i > Num:
                break

        writer = csv.writer(f)

    uncertaintweets.close()


def postdata(Num):
    import requests
    import simplejson

    API_KEY = "NUbs14x8-jenQy1tnSJ5"
    job_id = "707980"

    selecttweets(Num)

    file_path = "./static/uncertaintweets.csv"
    csv_file = open(file_path, 'rb')

    request_url = "https://api.crowdflower.com/v1/jobs/{}/upload".format(job_id)
    headers = {'content-type': 'text/csv'}
    payload = {'key': API_KEY}

    requests.put(request_url, data=csv_file, params=payload, headers=headers)


def main(Mun):
    postdata(Mun)
    return "success"


if __name__ == '__main__':
    postdata(2)
