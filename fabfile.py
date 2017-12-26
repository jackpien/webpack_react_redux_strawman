import os
import datetime as dt
import random
import time
from StringIO import StringIO
import json

from fabric.api import *
import fabric.contrib.files as fabfiles
#from fabric.network import ssh

#ssh.util.log_to_file("paramiko.log", 10)

#env.hosts = ["54.173.36.177"]

#env.user = 'ubuntu'    
env.shell = '/bin/bash -l -c'
#env.key_filename = '/home/jpien/local/eeme/gitspace/eeme-www/scripts/platformio_util/platformio_key.pem'
#dump_fn = "pg_dump_new.sql"
#remote_path_fn = "/home/bitnami/" + dump_fn
#local_path = "./no_git/"



def _get_input(msg):
    val = raw_input(msg + "\n")
    return val

def _fp(msg):
    fastprint(msg + "\n")

def _pp(msg):
    """ 
    Print then pause
    """
    _fp(msg)
    programPause = _get_input("Press the <ENTER> key to continue...")



def help_with_running():
    #print "fab -u jpien -H 127.0.0.1 helloworld"
    #local("ls -la")
    _fp("fab -H localhost -u jpien setup_webpack_react_redux:working_dir=`pwd`")

def test_code(working_dir):
    venv = _get_input("What virtual env do you want to install this in?")
    
    with cd(working_dir):
        with prefix("source ~/.virtualenvs/" + venv + "/bin/activate"):
            fd = StringIO()
            get("package.json", fd)
            content = fd.getvalue()
            package_dict = json.loads(content)
            package_dict["scripts"] = { "dev": "webpack -d --watch",
                                        "build" : "webpack -p" }
            
            print json.dumps(package_dict, indent=4)
    
def clean_webpack_react_redux(working_dir):
    run("echo 'Start'")
    _pp("Going to clean webpack react redux strawman from " + working_dir + \
        " - OK?")

    with cd(working_dir):
        flist = ["webpack.config.js",
                 "node_modules", # Created by npm install -S
                 "package.json", # Created by npm init
                 "src", # Where we have working and build files
                 ".babelrc", # the babel settings
        ]
        for fff in flist:
            if fabfiles.exists(fff):
                run("rm -rf " + fff)

# Webpack installation inspired by - https://www.codementor.io/reactjs/tutorial/beginner-guide-setup-reactjs-environment-npm-babel-6-webpack
# Redux React installation inspired by - http://academy.plot.ly/react/4-redux-state-management/
def setup_webpack_react_redux(working_dir):
    run("echo 'Start'")
    venv = _get_input("What virtual env do you want to install this in?")

    _pp("Installing webpack react redux strawman into " + working_dir + \
        " - OK?")

    # Create virtual env if it does not exist
    if fabfiles.exists("~/.virtualenvs/" + venv) == False:
        with prefix("source /usr/local/bin/virtualenvwrapper.sh"):
            run("mkvirtualenv " + venv)

    with prefix("source ~/.virtualenvs/" + venv + "/bin/activate"):
        with cd(working_dir):
            # Do we need to install nodenv?
            if not fabfiles.exists("~/.virtualenvs/" + venv + "/bin/nodeenv"):
                run("pip install nodeenv")

            # Do we need to install npm?
            if not fabfiles.exists("~/.virtualenvs/" + venv + "/bin/npm"):
                run("nodeenv -p")

            if not fabfiles.exists("package.json"):
                # -y answers yes to defaults
                run("npm init -y")

                # Update the npm tool runner with webpack commands
                # so we can "npm run build"
                # or "npm run dev"
                fd = StringIO()
                get("package.json", fd)
                content = fd.getvalue()
                package_dict = json.loads(content)

                # --devtool source-map allows us to debug in browser the
                # pre translated JSX files
                package_dict["scripts"] = { \
                        "dev": "webpack -d --devtool source-map  --watch",
                        "build" : "webpack -p"
                }
            
                run("rm package.json")
                run("touch package.json")
                fabfiles.append("package.json",
                                json.dumps(package_dict, indent=4))

                

            if not fabfiles.exists("node_modules/.bin/webpack"):
                # -S saves to package.json dependencies - like requirements.txt
                run("npm i webpack -S")

            # Just test one babel module to see if we need to install the
            # entire kitchen sink
            if not fabfiles.exists("node_modules/babel-preset-es2015"):
                run("npm i babel-core babel-loader babel-preset-es2015 " + \
                    "babel-preset-react-app -S")

            # Tells babel-loader which presets to load.
            if not fabfiles.exists(".babelrc"):
                run("touch .babelrc")
                fabfiles.append(".babelrc",
                                "{\n" +
                                "  \"presets\" : [\"es2015\", \"react-app\"]\n" +
                                "}\n")

            # Tells webpack to look at APP_DIR/index.jsx as starting point
            # to bundle everything into BUILD_DIR/bundle.js
            if not fabfiles.exists("webpack.config.js"):
                run("touch webpack.config.js")
                fabfiles.append("webpack.config.js",
                    "var webpack = require('webpack');\n" +
                    "var path = require('path');\n\n" +
                    "var BUILD_DIR = path.resolve(__dirname, 'src/client/public');\n" +
                    "var APP_DIR = path.resolve(__dirname, 'src/client/app');\n\n"+
                    "var config = {\n" +
                    "  entry: APP_DIR + '/index.jsx',\n" +
                    "  output: {\n" +
                    "    path: BUILD_DIR,\n" +
                    "    filename: 'bundle.js'\n" +
                    "  },\n" +
                    "  module : {\n" +
                    "    loaders : [\n" +
                    "      {\n" +
                    "        test : /\.jsx?/,\n" + # Test all js, jsx files
                    "        include : APP_DIR,\n" +
                    "        loader : 'babel-loader'\n" +
                    "      }\n" +
                    "    ]\n" +
                    "  }\n" +
                    "};\n\n"
                    "module.exports = config;")

            if not fabfiles.exists("src/client"):
                run("mkdir -p src/client/public")
                run("mkdir -p src/client/app")

            # Do we have react installed
            if not fabfiles.exists("node_modules/react"):
                run("npm install react react-dom -S")
                
            # Main html file
            if not fabfiles.exists("src/client/index.html"):
                with cd("src/client"):
                    run("touch index.html")
                    fabfiles.append("index.html",
                                    "<html>\n" +
                                    "<head>\n" +
                                    "<meta charset=\"utf-8\">\n" +
                                    "<title>React.js using NPM, Babel6 and Webpack</title>\n" +
                                    "</head>\n" +
                                    "<body>\n" +
                                    "<div id=\"app\" />\n" +
                                    "<script src=\"public/bundle.js\" type=\"text/javascript\"></script>\n" +
                                    "</body>\n" +
                                    "</html>")

            # Entry JS file where webpack will look to start bundling
            if not fabfiles.exists("src/client/app/index.jsx"):
                with cd("src/client/app"):
                    run("touch index.jsx")
                    fabfiles.append("index.jsx",
                                    """
import React from 'react';
import {render} from 'react-dom';
import AwesomeComponent from './AnotherComponent.jsx';

class App extends React.Component {
  render () {
    return <div>
             <p> Hello React!</p>
             <AwesomeComponent />
           </div>;
  }
}

render(<App/>, document.getElementById('app')); 
                                    """)

            # Other JSX components
            if not fabfiles.exists("src/client/app/AnotherComponent.jsx"):
                with cd("src/client/app"):
                    run("touch AnotherComponent.jsx")
                    fabfiles.append("AnotherComponent.jsx",
                                    """
import React from 'react';

class AwesomeComponent extends React.Component {

  constructor(props) {
    super(props);
    this.state = {likesCount : 0};
    //this.onLike = this.onLike.bind(this);
  }

  // Fat arrow operator binds this which makes it unnecessary to explicitly 
  // bind in constructor
  // onLike() {...} turns into onLike = () => {...}
  onLike = () => {
    let newLikesCount = this.state.likesCount + 1;
    this.setState({likesCount: newLikesCount});
  }

  render() {
    return (
      <div>
        Likes : <span>{this.state.likesCount}</span>
        <div><button onClick={this.onLike}>Like Me</button></div>
      </div>
    );
  }

}

export default AwesomeComponent;
                                    """)

            # Do we have redux installed
            if not fabfiles.exists("node_modules/redux"):
                run("npm install redux react-redux -S")

    _fp("")
    _fp("""
Some redux thoughts:

1) In reducer.js
  - define an initialState
  - define a reducer 
    - takes "current state" & an "action", does something, returns new state
      - this is passed back to each React component's connected mapPropToState

2) In action.js
  - define all the actions you care about
    - "CHANGE_LOCATION" token + new_state pair

3) In main index.jsx
  - wrap redux "Provider" around main React component in React.render
    - Provider is given a store to use.
      - The store is bound to a the reducer we defined in reduce.js

4) In each React component
  - "connect" that component (using Redux's connect) during export
    - connect will also bind a mapPropToState func
      - mapPropToState converts store's state to a this.prop.prop_state 
        - this.prop.prop_state is used by React components render.
  - render via this.props (not this.state)
  - React component never directly modifies this.state
    - Only dispatches "actions" when state change occurs
    
    """)
    _fp("... with that said run...")
    _fp("1) workon " + venv)
    _fp("2) ./node_modules/.bin/webpack -d")
    _fp("  -OR-")
    _fp("   npm run build -OR- npm run dev")
    _fp("3) open web browser to src/client/index.html")
    _fp("4) try to add redux components via http://academy.plot.ly/react/4-redux-state-management/")
    
