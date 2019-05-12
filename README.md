# Lambda Benchmark

We are testing a WSGI (Flask) App vs a ASGI (Quart) App on AWS Lambda.

## Zappa integration

Zappa integration aka (asgi=true + mangum):

https://github.com/delijati/Zappa

Info:

https://gist.github.com/erm/cf04850eed8285515e75324cebafc4b4
https://github.com/erm/mangum
https://github.com/Miserlou/Zappa/blob/master/zappa/handler.py#L601

## Benchmark

Install benchmark tool:

```
$ sudo apt-get install build-essential libssl-dev git -yo
$ git clone https://github.com/wg/wrk.git wrk
$ cd wrk
$ make
```

Also look into: https://klen.github.io/py-frameworks-bench/

Execute benchmark:

```
$ wrk -d20s -t10 -c200 http://127.0.0.1:5000/
```

### For ASGI

ATTENTION first undeploy the other app or you get an wired Zappa error

Install run locally

```
$ cd asgi_app 
$ virtualenv -p /usr/bin/python3.7 env
$ source env/bin/activate
$ pip install -e .
$ app-serve
```

Deploy via zappa

```
$ pip install git+https://github.com/delijati/Zappa
$ zappa deploy dev
# for errors use zappa tail
$ 
```

Run the benchmark:

```
% wrk -d20s -t10 -c200 https://XXX.execute-api.eu-central-1.amazonaws.com/dev
Running 20s test @ https://XXX.execute-api.eu-central-1.amazonaws.com/dev
  10 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    37.63ms   41.67ms   1.78s    99.24%
    Req/Sec   505.67    128.77   670.00     85.46%
  89432 requests in 20.09s, 44.95MB read
  Socket errors: connect 0, read 0, write 0, timeout 286
Requests/sec:   4452.44
Transfer/sec:      2.24MB
```

### WSGI

ATTENTION first undeploy the other app or you get an wired Zappa error

Install run locally

```
$ cd wsgi_app 
$ virtualenv -p /usr/bin/python3.7 env
$ source env/bin/activate
$ pip install -e .
$ app-serve
```

Deploy via zappa

```
$ pip install git+https://github.com/delijati/Zappa
$ zappa deploy dev
# for errors use zappa tail
$ 
```

Run the benchmark:

```
% wrk -d20s -t10 -c200 https://YYY.execute-api.eu-central-1.amazonaws.com/dev
Running 20s test @ https://YYY.execute-api.eu-central-1.amazonaws.com/dev
  10 threads and 200 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   104.35ms  246.97ms   1.89s    92.53%
    Req/Sec   521.65    121.54   676.00     88.16%
  97418 requests in 20.08s, 48.96MB read
Requests/sec:   4850.86
Transfer/sec:      2.44MB
```
