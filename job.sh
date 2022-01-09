# running AlphaServer with specific port
terminal -e python3 server.py 1234

# running AlphaClient who made 3 attempt
terminal -e python3 client.py 1234 nodeABC
python3 client.py 1234 nodeABC
python3 client.py 1234 nodeABC

# running AlphaClient who made 2 attempt
terminal -e python3 client.py 1234 nodeXYZ
python3 client.py 1234 nodeXYZ