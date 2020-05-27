#!/usr/bin/env python3

"""
    Flask app to send logs to Datadog and tracing the application using APM (Datadog's Application Performance Monitoring).
    Author: Sadip Giri (sadipgiri14@gmail.com)
    Date: 10th April, 2020
"""

from flask import Flask, render_template, request
import time
import os
from ddtrace import tracer

app = Flask(__name__)

@app.route('/')
def hello():
    '''
        render hello.html file
    '''
    return render_template('hello.html')

@app.route('/index', methods = ['POST', 'GET'])
def index():
    '''
        - render index.html file
        - receive information such as API key, logs, # of logs to send to repective account
        - use os command to curl Datadog's logs endpoint to send logs
        - timer to successfully send logs
        - finally render back to index.html file
    '''
    if request.method == 'POST':
        api_key = request.form['DD_API_KEY']
        log_msg = request.form['LOG_MSG']
        times = int(request.form['NUM_OF_LOGS'])

        # limiting the number of logs to 100 so that it won't take alot of resources
        if times > 10000:
            times = 10000

        # Using Datadog's logs API endpoint to send logs:
        command = '''
        curl -X POST https://http-intake.logs.datadoghq.com/v1/input \
            -H "Content-Type: text/plain" \
            -H "DD-API-KEY: {0}" \
            -d '{1}'
        '''.format(api_key, log_msg)
        
        for i in range(times):
            time.sleep(0.025)
            os.system(command)

        # print(get_correlation_ids())

        return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')