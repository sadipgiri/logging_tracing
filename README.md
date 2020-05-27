# Flask App to send <a href="https://docs.datadoghq.com/logs/">Logs</a> to Datadog and tracking the application using <a href="https://docs.datadoghq.com/tracing/">APM</a>


Tracing Python Application: https://docs.datadoghq.com/tracing/setup/python/

Logs Endpoint: https://docs.datadoghq.com/api/?lang=bash#send-logs-over-http

<br/>
  
## Code Requirements

The code is in Python3 (version 3.0 or higher will work). The only other requirement is: 
- <a href="https://docs.datadoghq.com/agent/basic_agent_usage/?tab=agentv6v7">datadog-agent</a>, 
- <a href="https://docs.datadoghq.com/tracing/setup/python/">datadog-tracing-library</a> & 
- <a href="http://flask.pocoo.org">flask</a>


### Execution Option 1:

To run the program, simply run app.py file:

```
python app.py
```

To <a href="https://docs.datadoghq.com/tracing/setup/python/">automatically instrument</a> the flask application, simply run:

```
ddtrace-run python app.py
```

Add <a href="https://docs.datadoghq.com/tracing/app_analytics/?tab=python">app analytics</a>:

```
DD_TRACE_ANALYTICS_ENABLED=true ddtrace-run python app.py
```

Set an <a href="https://docs.datadoghq.com/tracing/setup/python/#environment-variable">application's environment</a> e.g. prod, staging:

```
DATADOG_ENV=fun DD_TRACE_ANALYTICS_ENABLED=true ddtrace-run python app.py
```

### Execution Option 2:

```
docker-compose build --no-cache
docker-compose up
```

Logging Welcome page:

<a href="http://0.0.0.0:5000/">http://0.0.0.0:5000/ </a> and send yourself logs as well as trace flask app.

To everything down:

```
docker-compose down

```

### Author

* **<a href="https://sadipgiri.github.io">Sadip Giri</a>** - (sadipgiri@bennington.edu)

### Contact

Feel free to contact me (PRs are always welcome!) with any questions, comments, suggestions, bug reports, etc.

### Implementations:

- Flask app sending logs to Datadog UI:

![](https://p-qkfgo2.t2.n0.cdn.getcloudapp.com/items/qGudAzjg/Image%202020-04-12%20at%208.21.19%20PM.png?v=fd978360ca5be4be78e1bf51a27d6d61)

-  Automatic tracing of the application:

![](https://p-qkfgo2.t2.n0.cdn.getcloudapp.com/items/jkulryy2/Image%202020-04-12%20at%208.45.48%20PM.png?v=178e8ce17acacfdb7b294f72e2a54e7a)