# COMP4920 Project: Sesalta  

### To install this project:

Navigate to where you want to store the project, eg:  
`cd && mkdir -p Projects && cd $_`

If you haven't already, add a SSH key to your GitHub account so that you don't need to sign in every time:  
[Adding a new SSH key to your GitHub account](https://help.github.com/en/articles/adding-a-new-ssh-key-to-your-github-account)

Then clone the project:  
`git clone git@github.com:ThatMattG/Sesalta.git`

## Install prerequisites:  

### Homebrew:  
Check if you have it installed already by running: `brew update`;  
Otherwise run:  
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### Bash:  
`brew install bash`

### Python 3.7.4:  
On Mac: `brew install pyenv` <- This will install pyenv, which we will use to manage our Python version  
On Linux: `curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash`

`pyenv install 3.7.4` <- This will install python 3.7.4  
^If that doesn't work try: `CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install 3.7.4`  

`brew install pipenv` <- This will install pipenv, which we will use to manage our Python packages  

### Virtual Env:  
`pip install --upgrade virtualenv`  
`pip install --upgrade virtualenvwrapper`  

`echo 'export WORKON_HOME=$HOME/.virtualenvs # virtualenvs' >> ~/.profile`  
`echo 'export PROJECT_HOME=$HOME/Projects # virtualenvs' >> ~/.profile`  
`echo '. ~/.pyenv/versions/3.7.4/bin/virtualenvwrapper.sh # virtualenvs' >> ~/.profile`  

## Create a Virtual Env:  

`mkvirtualenv sesalta --python=$HOME/.pyenv/versions/3.7.4/bin/python`  
Note: If `~/Projects/Sesalta` isn't the path to the project, then change it in the command  
`echo "cd ~/Projects/Sesalta/" >> ~/.virtualenvs/sesalta/bin/postactivate`  

Now whenever you want to work on the project, just run this command and a virtualenv will activate automatically:  
`workon sesalta`  

Make sure you have the virtual env activated before proceeding, your terminal should be prefixed like so:  
`(sesalta) <your terminal name here>:~/Projects/Sesalta$`  

Install Python Packages:  
`pipenv sync`  


Install Node Version Manager:  
`brew install nvm`  

Add NVM shims to your profile:
```  
mkdir ~/.nvm
echo 'export NVM_DIR="$HOME/.nvm" # nvm' >> ~/.profile
echo '. $(brew --prefix)/opt/nvm/nvm.sh # nvm' >> ~/.profile  
```

Restart your terminal and then run:  
`nvm install 10.16.2`  

Install Yarn (NPM Package Manager):  
`brew install yarn --without-node`  


### To run this project:
Switch to the project:  
`workon sesalta`

Run the Flask server:  
`cd api && pipenv sync && flask run`  

Run the React server:  
`cd frontend && yarn start`  


### deployment
CDN: d316o4cbhc2v3a.cloudfront.net
original domain: http://sesalta.s3-website-ap-southeast-2.amazonaws.com/
