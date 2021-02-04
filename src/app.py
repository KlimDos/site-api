#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Simple FastAPI asyncron interface with uvicorn .

Example:

        $ python app.py  <list> of uvicorn arguments

The tool is using local unified classes from do-contenttech/packages

Attributes:

    ENV (str): Environment
    -f(bool): Force

Todo:
    * TODO 

.. _Google Python Style Guide:
   https://google.github.io/styleguide/pyguide.html
"""

# Standard library imports
import os
import sys
import json

# Third party imports
from fastapi import FastAPI
import uvicorn

# Module level variables
#ENV = sys.argv[1]
#FORCE = False

#if len(sys.argv) == 3:
#    if sys.argv[2] == "-f":
#        FORCE = True

def usage():
    print(
        f"\n\nUsage:\n python {sys.argv[0]} sit -f ")



def main():
    """ Main wrapper """

    #outputs = Logger()

    # if len(sys.argv) < 1:
    #     usage()
    #     sys.exit(1)

    # Init
    app = FastAPI(
        debug = True,
        title = "Microservice name API",
        description = "Some meaningfull description",
        version = "0.0.1-alpha",
        )
    print('getcwd:      ', os.getcwd())
    print('__file__:    ', __file__)
    print('basename:    ', os.path.basename(__file__))
    print('dirname:     ', os.path.dirname(__file__))

    # Data
    with open("{}/data.json".format(os.path.dirname(__file__))) as f:
        data = json.load(f)

    # Routes
    @app.get("/api/v1/data")
    async def get_data():
        """Retrive all data from DB"""
        return data 
    
    return app


# if you run in locally
if __name__ == '__main__':
    uvicorn.run(main(), host='127.0.0.1', port=8000)
