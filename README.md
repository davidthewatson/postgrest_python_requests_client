# PostgREST Python Client

This repository provides a generic python REST client for any PostgREST server
with a PostgreSQL database behind it.

This client implements the following features:

* Login
* JWT Auth
* HTTP GET
* Pagination of result sets based on Content-Range header

PostgREST installation and configuration is beyond the scope of this document.

See http://postgrest.com/ for more information.

## Installation and configuration

This example uses python 3.5. You may have to edit the source to accommodate python versions < 3.5.

0. Clone this repository

        git clone https://github.com/davidthewatson/postgrest_python_requests_client.git
0. Install requirements

        pip install -r requirements.txt
0. Copy config.in to config.py

        cp config.in config.py
0. Edit credentials and urls in config.in to suit

        vi config.py
0. Save config.py

        [esc]:wq
0. Run

        python client.py
