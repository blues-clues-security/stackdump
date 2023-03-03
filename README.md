# StackDump

## Dependencies
jsonpointer, contextlib2, tqdm, schema, jsonpatch, docopt, internetarchive
Ubuntu

## Notes
- Had issues with alpine container running Java/getting the dependencies right
  - Possible to make it work, may need to go back later
- Most of the work done in the Dockerfile is in 'docker_start.sh' script
  - Biggest issue faced with Dockerfile was adding start_solr.sh and start_web.sh in some container as both the web, and the python app need access
- Due to size of files, may need to mount the share as a volume instead of copy
  - Not sure how this will affect solr or the python app
-  

### Command options for ./manage.sh
'-n', '--site-name', help='Name of the site.'
'-d', '--site-desc', help='Description of the site (if not in sites).'
'-k', '--site-key', help='Key of the site (if not in sites).'
'-c', '--dump-date', help='Dump date of the site.'
'-u', '--base-url', help='Base URL of the site on the web.'
'-Y', help='Answer yes to any confirmation questions.'

### Docker Commands
docker build -t default/stackdump
docker run -d -p 8080:8080 --name stackdump default/stackdump
[Troubleshooting]
docker run -it --rm default/stackdump /bin/bash

## References 
- https://github.com/sornram9254/stackdump
  - https://www.youtube.com/watch?v=jHEBlHxEKeM
- https://stackapps.com/questions/3610/stackdump-an-offline-browser-for-stackexchange-sites
- https://archive.org/details/stackexchange
- https://docs.python-requests.org/en/latest/api/#requests.Request
- https://archive.org/services/docs/api/internetarchive/api.html#searching-items

### Alternatives
- https://github.com/Caspia/seekoff
  - Uses 

### Troubleshooting
- https://www.whitesourcesoftware.com/free-developer-tools/blog/docker-expose-port/
- https://meta.stackexchange.com/questions/306593/how-can-i-download-the-stack-exchange-data-dump-from-archive-org-through-the-com