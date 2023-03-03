# StackDump

StackDump is an offline browser for StackExchange sites. It allows users to browse and search StackExchange data dumps on their local machines. 

## Dependencies

- jsonpointer 
- contextlib2 
- tqdm 
- schema 
- jsonpatch 
- docopt 
- internetarchive 

The application has been tested on Ubuntu, and it requires the above dependencies to run.

## Docker

To build the Docker image, run the following command from the project directory:

```
docker build -t default/stackdump .
```

To run the container, use the following command:

```
docker run -d -p 8080:8080 --name stackdump default/stackdump
```

To debug the container, use the following command:

```
docker run -it --rm default/stackdump /bin/ash
```

## Notes

- We faced issues with the Alpine container while running Java and getting the dependencies right.
- Most of the work done in the Dockerfile is in the `docker_start.sh` script.
- The biggest issue we faced with the Dockerfile was adding `start_solr.sh` and `start_web.sh` in some container, as both the web and the Python app need access.
- Due to the size of the files, it may be necessary to mount the share as a volume instead of copying them. We are not sure how this will affect Solr or the Python app.

### Command options for `./manage.sh`

The following command options are available for `./manage.sh`:

```
-n, --site-name         Name of the site.
-d, --site-desc         Description of the site (if not in sites).
-k, --site-key          Key of the site (if not in sites).
-c, --dump-date         Dump date of the site.
-u, --base-url          Base URL of the site on the web.
-Y                      Answer yes to any confirmation questions.
```

## References 

- https://github.com/sornram9254/stackdump
- https://www.youtube.com/watch?v=jHEBlHxEKeM
- https://stackapps.com/questions/3610/stackdump-an-offline-browser-for-stackexchange-sites
- https://archive.org/details/stackexchange
- https://docs.python-requests.org/en/latest/api/#requests.Request
- https://archive.org/services/docs/api/internetarchive/api.html#searching-items

### Alternatives

- https://github.com/Caspia/seekoff


## Troubleshooting

- https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/
- https://meta.stackexchange.com/questions/306593/how-can-i-download-the-stack-exchange-data-dump-from-archive-org-through-the-com