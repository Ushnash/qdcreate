# qdcreate
Small utility written in Python that lets one supply a file to the [QPid Dispatch Router]: https://qpid.apache.org/components/dispatch-router/index.html `qdmanage` utility for effecting topology changes. The utility also lets you update the router's config file, making changes permanent.

## Usage
```
usage: qdcreate.py [-h] [-o OUTFILE] infile

positional arguments:
  infile                name of the file containing data for qdmanage

optional arguments:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        file to append the results to. Ideally, this is an
                        existing qdrouterd.conf file. If absent, data is
                        written to STDOUT.
```
