# Puppet-Master

Efficently and effortlessly create, maintain, re-use sock puppets for OSINT investigations in a consistent fashion.

## Purpose 
- The goal of this project is to help OSINT investigators to easily create and store sock puppets. This script can automatically and consistently prepare their browser and system accordingly to each puppet based on stored information.
- The idea was inspired by [this talk](https://www.youtube.com/watch?v=v8EP6xOcB8M) - I highly recommended to watch it.
- This script automates some parts of it.
## Requirement 
- Python 3
- Requests 
- Selenium
- Firefox 
- [geckodriver](https://github.com/mozilla/geckodriver/releases)
## Features
<pre><code>
user@Ubuntu:~/Desktop/code/Puppet-Master$ ./puppet-master.py -h
usage: puppet-master.py [-h] [-i] [-r] [-db] [-m index] [-v index] [-d index]
                        [-l index]

Specify an optional argument with the index corresponding to a puppet to
interact with it

optional arguments:
  -h, --help    show this help message and exit
  -i, --init    Set up new puppet
  -r, --random  Generate a random puppet
  -db           List the puppets and their corresponding index
  -m index      Modify infomation of a puppet
  -v index      View infomation of a puppet
  -d index      Remove a puppet
  -l index      Load a puppet
</code></pre>

### TODO 
- Location and timezone services.
- Keep track of the age of puppets.
- Add browser extensions.
- Add some screenshot/demo
- Better documentation 
