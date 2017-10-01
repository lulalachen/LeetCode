HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def getOutput(color, text):
  return color + text + ENDC

class colors(object):

  def header(text):
    return getOutput(HEADER, str(text))

  def okBlue(text):
    return getOutput(OKBLUE, str(text))

  def okGreen(text):
    return getOutput(OKGREEN, str(text))

  def warning(text):
    return getOutput(WARNING, str(text))

  def fail(text):
    return getOutput(FAIL, str(text))

  def bold(text):
    return getOutput(BOLD, str(text))

  def underline(text):
    return getOutput(UNDERLINE, str(text))
