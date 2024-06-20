#> Import Libraries
import io
import contextlib
import sys
import os
from dotenv import load_dotenv
import aiml



#> Initializations
load_dotenv()
kernel = aiml.Kernel()



#> Usage and Help Functions
def usage(ret=False):
  """Usage message."""
  USAGE_MSG = f"Usage: py {sys.argv[0]} session_id [request_message] \n\nsession_id: A unique session ID for the user.\n\nrequest_message: Optional request for the user's session. (if not passed DEFAULT_REQUEST will be used)"

  if ret: return USAGE_MSG
  print(USAGE_MSG)

def help(ret=False):
  """Help message."""
  HELP_MSG = "Help:\n\nThis script takes a session ID and optional additional requests and performs some action based on them."  + usage(True)

  if ret: return HELP_MSG
  print(HELP_MSG)



#> Custom Exceptions
class BrainFileInaccessible(Exception):
  """Brain File either does not exists or is not readable."""
  def __init__(self, message="Brain File does not exists"):
    self.message = message
    super().__init__(self.message)

class IncorrectArguments(Exception):
  """CLI areguments are not accurate"""
  def __init__(self, message=None):
    self.message = message if message else usage()
    super().__init__(self.message)




#> Validation
if len(sys.argv) == 1:
  usage()
  sys.exit(1)

if len(sys.argv) < 2:
  usage()
  sys.exit(1)


#> Special Commands
if sys.argv[1] == 'help':
  help()
  sys.exit(0)

if sys.argv[1] == 'usage':
  usage()
  sys.exit(0)





#> Config
BRAIN_FILE      =     os.getenv('BRAIN_FILE'       )  or "bot_brain.brn"
VERBOSE         = int(os.getenv('VERBOSE'          )) or 0
DEFAULT_REQUEST =     os.getenv('DEFAULT_REQUEST'  )  or 'Hi'
SESSION_ID      =     os.getenv('STATIC_SESSION_ID')  or sys.argv[1] or 'default'


#> Setup

# 1. Load Brain File
if os.path.exists(BRAIN_FILE):
  if VERBOSE > 0 : print("Loading brain from", BRAIN_FILE)
  with contextlib.redirect_stdout(io.StringIO()):
    kernel.loadBrain(BRAIN_FILE)
else:
  raise BrainFileInaccessible()




#> Process
request_input = ' '.join([x.strip() for x in sys.argv[2:]])
if VERBOSE > 1: print(f"Request  = {request_input}\nResponse = ", end='')
print(
  kernel.respond(
    request_input or DEFAULT_REQUEST,
    SESSION_ID
  )
)