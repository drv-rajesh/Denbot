from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return """
  <title> Denbot Server </title>
  <h2> Server is up. (yay 😌) </h2>
  <h4> About </h4>
  <ul>
    <li> ❓ - This is the server running the Discord '<i>Denbot</i>' by Dhruv Rajesh. </li>
    <li> ❌- If the server displays an error saying 'Hmm, we couldn't reach your REPL', that means the server is either <b> under maintenance or down. </b> </li>
    <li> 🧹- This server goes under maintenance regularly, however <u> not all maintenance checks will down the server. </u> </li>
    <li> ❗ - <b> This is a development server</b>, not made for production deployments. </b> </li>
    <li> 🌎 - Visit the Repl <a href="https://repl.it/@drvrajesh/Denbot"> here </a> </li>
  </ul>
  <hr>
  <p> This server was created using Flask and HTML. </p>
  """

def run():
  app.run(host='0.0.0.0', port=8080)

def keep():
  t = Thread(target=run)
  t.start()
