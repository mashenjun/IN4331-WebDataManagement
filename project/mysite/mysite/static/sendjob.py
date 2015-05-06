__author__ = 'alienware'
import requests

API_KEY = "R2K_qsUfq7ZBrdkKXPGj" # KEY_API
job_id = "mashenjun_autojob" #jobID

file_path = "temp.csv" # file store the tweete need to update to crowdflower
csv_file = open(file_path, 'rb')

request_url = "https://api.crowdflower.com/v1/jobs/{}/upload".format(job_id)
headers = {'content-type': 'text/csv'}
payload = { 'key': API_KEY }

requests.put(request_url, data=csv_file, params=payload, headers=headers)
