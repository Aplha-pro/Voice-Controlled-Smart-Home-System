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



#> Config
BRAIN_FILE      =     os.getenv('BRAIN_FILE'       )  or "bot_brain.brn"
VERBOSE         = int(os.getenv('VERBOSE'          )) or 0
DEFAULT_REQUEST =     os.getenv('DEFAULT_REQUEST'  )  or 'Hi'


#> Setup

# 1. Load Brain File
if os.path.exists(BRAIN_FILE):
  if VERBOSE > 0 : print("Loading brain from", BRAIN_FILE)
  with contextlib.redirect_stdout(io.StringIO()):
    kernel.loadBrain(BRAIN_FILE)
else:
  raise BrainFileInaccessible()



def apply_mc_change(device, state):
  devices = {
    'fan': 1,
    'light': 2,
    'ac': 3,
  }
  states = {
    'on': True,
    'off': False,
  }

  # > Aliases
  for psb in [
      'air conditioner',
      'cooler',
      'inverter',
    ]:
    if device == psb: device = 'ac'

  for psb in [
      'roof fan',
      'some air',
      'breeze',
      'pankha',
    ]:
    if device == psb: device = 'fan'

  for psb in [
      'roshni',
      'lamp',
    ]:
    if device == psb: device = 'light'

  for st in [
      'active',
    ]:
    if state == st: state = 'on'

  for st in [
      'inactive',
    ]:
    if state == st: state = 'off'


  

  pass



#> Process
def run_model(session_id='default', request_input='Hi'):
  global VERBOSE, DEFAULT_REQUEST

  if VERBOSE > 1: print(f"Request  = {request_input}\nResponse = ", end='')
  
  response = kernel.respond(
    request_input or DEFAULT_REQUEST,
    os.getenv('STATIC_SESSION_ID') or session_id
  )

  # status o fan, light, ac
  command = kernel.getPredicate(
    'command',
    os.getenv('STATIC_SESSION_ID') or session_id
  )

  device = kernel.getPredicate(
    'device',
    os.getenv('STATIC_SESSION_ID') or session_id
  )

  print(f"command={command}")
  print(f"device={device}")

  return response