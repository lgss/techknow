import json
import time
import datetime
import urllib3
import sys
import os
import sys
import xml.etree.ElementTree as ET



testruns={}
buildId=os.getenv('buildID')
with open('result.js') as json_file:
    data = json.load(json_file)
    for v in data['value']:
        testruns[v['name']] = str(v['id'])

env = json.loads(open("config.json").read())
resultsFiles = sys.argv[1].split()
errors_to_post = []
total_tests = 0
total_fails = 0
for resultFile in resultsFiles:
    testRunName=resultFile[:resultFile.rfind("/")]
    testRunName=testRunName[testRunName.rfind("/")+1:]
    
    print(resultFile)
    print(testRunName)
    counter=99999
    tree = ET.parse(resultFile)
    root = tree.getroot()
    errors = int(root.attrib['errors'])
    failures = int(root.attrib['failures'])
    total_fails += errors
    total_fails += failures
    tests = int(root.attrib['tests'])
    total_tests += tests
    print("errors: " + str(errors))
    print("failures: " + str(failures))
    print("errors + failures: " + str(errors + failures))
    for testcase in root.iter('testcase'):
        counter += 1
        for err in testcase.iter('error'):
            test_name=testcase.attrib['name']
            error_message=err.attrib['message']
            if len(error_message) > 64:
                error_message = error_message[:64] + "…"
            if len(errors_to_post) < 3:
                errors_to_post.append([test_name,error_message,counter,testruns[testRunName]])
    

url = env["appazuresite"] + "/_build/results?buildId=" + buildId + "&view=ms.vss-test-web.build-test-results-tab"

all_good = total_fails == "0"
if all_good:
    msg = "All " + env['appname'] + " tests have finished successfully."
    color = "good"
    errs = ""
    thumb = "pipeline/success.png"
else:
    msg = "There are " + str(errors) + " failing tests in " + env['appname'] + "!"
    color = "danger"
    mapf = lambda x: "Failed: " + x[0].test_id
    errs = "<a href='#'>test1</a>\n<a href='#'>test2</a>"
    thumb = "pipeline/failed.png"

    message=[]

message.append({
		"type": "section",
		"text": {
			"type": "plain_text",
			"emoji": True,
			"text": "There are " + str(total_fails) + " failing tests out of " + str(total_tests) + " in " + env['appname'] + "!"
		}
	})
message.append({
		"type": "divider"
	})
message.append({
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*Failing tests:*"
		}
	})
for etp in errors_to_post:
    message.append({
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*" + etp[0] + "*\n" + etp[1]
		},
		"accessory": {
			"type": "button",
			"text": {
				"type": "plain_text",
				"emoji": True,
				"text": "View"
			},
			"url": env["appazuresite"] + "/_build/results?buildId=" + buildId + "&view=ms.vss-test-web.build-test-results-tab&resultId=" + str(etp[2]) + "&runId=" + etp[3]
		}
	})
message.append({
		"type": "section",
		"text": {
			"type": "mrkdwn",
			"text": "*<" + env["appazuresite"] + "/_build/results?buildId=" + buildId + "&view=ms.vss-test-web.build-test-results-tab|View " + str(total_tests - len(errors_to_post)) + " more tests>*"
		}
	})

body_data = json.dumps({'blocks': message})

config_use_slack = os.getenv('use_slack')
config_slack_endpoint = os.getenv('slack_endpoint')

if config_use_slack:
    http = urllib3.PoolManager()
    r = http.request("POST", config_slack_endpoint,
                        headers={'Content-Type': 'application/json'},
                        body=body_data)
    if r.status != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (r.status, r._body)
        )
