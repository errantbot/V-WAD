# V-WAD (Visual Web application detector)

V-WAD is a fork of Piotr Lizończyk's WAD. This fork rests largely on the shoulders of the original WAD detection system 
but provides a Graphical User Interface to launch scans and inspect results more intuitively.

<!---
![alt tag](https://github.com/errantbot/kerosene/upload/master/data/icons/flame.ico)
-->

V-WAD lets you analyze given URL(s) and detect technologies used by web application behind that URL, 
from the OS and web server level, to the programming platform and frameworks, as well as server- and client-side
applications, tools and libraries. 

For example, results of scan of server might include: 

  * OS: Windows, Linux...
  * Web server: Apache, Nginx, IIS...
  * Programming platform: PHP, Python, Ruby, Java...
  * Content management systems: Drupal, WordPress...
  * Frameworks: AngularJS, Ruby on Rails, Django...
  * various databases, analytics tools, javascript libaries, CDNs, comment systems, search engines and many others.
  

## How it works
V-WAD is built as a standalone application, using [Wappalyzer](https://github.com/AliasIO/Wappalyzer)'s
detection rules. It sends a GET request to the given URL and analyzes both HTTP response header and body (HTML page), 
looking for indications to discover web technologies used. 

Detection results may include information about versions of technologies used, for example Linux distro or Apache version. 
Results are categorized depending on type of technology (whether it is CMS or database etc.). There are now over 700 
technologies that can be discovered using V-WAD.

## Installation
V-WAD only works with Python3. In order to use V-WAD you must:
- install python3 from [python.org](https://www.python.org/downloads/)
- install the python modules required to run the software ```python3 -m pip install -r requirements.txt```
- run V-WAD ```python3 vwad.py```

## Differences between V-WAD and Wappalyzer
Although most of the rules matching functionality is simply a Python port of Wappalyzer's javascript implementation, there are some key differences between projects.

First of all, Wappalyzer (as an extension) runs on top of web browser, which means that the scripts on scanned site were ran, so variables and objects are created and accessible. 
Unfortunately, this isn't and won't be a case for V-WAD. V-WAD parses raw site content (as delivered by HTTP response), without running it in browser context. 
The consequences of that are simple - we can't use Wappalyzer's rules, that search for variables and objects in Javascript environment.

### Authors
Special thanks to the original authors/contributors of WAD:

  * Sebastian Łopieński
  * Piotr Lizończyk
  * Vincent Brillaut
  * Farzaneh Moghaddam
  * Antonio Perez Perez
  * Dame Jovanoski