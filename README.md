# code-saturdays

Welcome to the Code-Saturdays Github repo.

## Installing prerequisites

### Install Git

You can download the latest from:  
https://git-scm.com/downloads

Verify you have it installed correctly   
Go to a terminal (cmd.exe on windows or terminal on mac)
and type:
```
git --version
```

Install an IDE (integrated development environment)

I **HIGHLY** recommend VS-Code
You can download it from here:  
https://code.visualstudio.com/

I would install two languages at this point:  
Python   
https://www.python.org/downloads/

and  
Node.js  
https://nodejs.org/en/

This will get you ready to write both Node.js and/or Python code as you move forward.  Python 3 is the new standard, 2.x has officially been deprecated, so welcome to 2020. :-)

## Setting up a new project

Create a new repository on github
I like to setup an GNU license, Python .gitignore and a readme file.

Clone it
```
git clone https://github.com/lotekmedia/code-saturdays.git
```

Open that folder in VS-Code

And now we can begin writing some basic code.

I'm going to focus on Python 3 to start.  

### Create a virtual environment

```
python3 -m venv ./venv
```

Activate new virtual environment
```
source venv/bin/activate
```

## Python Version
Create a hello.py file:
```python
def main():
	print ('Hello World')

if __name__ == "__main__":
	main()
```

Run python file:
```
python hello.py
```

## Node.js version
Create a hello.js file:
```javascript
console.log('Hello World');
```

Run Javascript file
```
node hello.js
```

## Web Node Version
Run npm init  
*NOTE: For entry point, type web.js*
```
npm init
```
Install Express
```
npm install express
```

Create web.js
```javascript
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))
```

Run website:
```
node web.js
```

Browse to
http://localhost:3000

# TADA!
