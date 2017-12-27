from flask import Flask
app = Flask(__name__)

# Imports the Google Cloud client library
from google.cloud import bigquery

# Instantiates a client
bigquery_client = bigquery.Client()

# The name for the new dataset
dataset_id = 'tweetify'

# Prepares a reference to the new dataset
dataset_ref = bigquery_client.dataset(dataset_id)
dataset = bigquery.Dataset(dataset_ref)

print('Dataset {} created.'.format(dataset.dataset_id))

@app.route('/')
def hello_world():
	    return 'Hello, World!'

@app.route('/gcp/<username>')
def get_bq(username):

	query = 'SELECT * FROM tweetify.general_fintech_tweets'
	query_job = bigquery_client.query(query)

	# Print the results.
	for row in query_job.result():  # Waits for job to complete.
		print(row)

	return username
