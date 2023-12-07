# Socket Chat

Implementation of a Socket based chat using tkinter for the UI.


## 1. Create and activate a venv:

    $ python -m venv venv

    $ source venv/bin/activate

## 2. Change the IP in the files to acess the server.
  server.py
  
      def __init__(self, host='ip', port=port):
        self.host = host
        self.port = port
  
  client.py
  
        client.connect(('ip', port))

## 3. Run the Server on computer A:

    $ python server.py

## 4. Run the Client on computer B:

    $ python client.py



