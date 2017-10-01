import time
from functools import reduce
from helpers.colors import colors

# Unicode Icon: www.fileformat.info/info/unicode/category/So/list.htm
correctMark = u'\u2714'
wrongMark = u'\u2718'
stars = u'\u2728'

def evaluateTime(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        return ret, '%0.3f ms' % ((time2 - time1) * 1000)
    return wrap

def showResult(result):
  if result.get('Correct'):
    print('{mark}'.format(mark=colors.okGreen(correctMark)))
  else:
    print('{mark}'.format(mark=colors.fail(wrongMark)))
    print('{title}: {value}'.format(
      title=colors.bold('Input'),
      value=result.get('Input'),
    ))
    print('{title}: {value}'.format(
      title=colors.bold('Output'),
      value=colors.fail(result.get('Output')),
    ))
    print('{title}: {value}'.format(
      title=colors.bold('Expected'),
      value=colors.okGreen(result.get('Expected Output')),
    ))
  print('{title}: {value}'.format(
    title=colors.bold('Execute Time'),
    value=result.get('Execute Time'),
  ))

def getOutcome(test_inputs, expected_outputs, executedFunction):

  def evaluate(case):
    inputValue, expectedOutout = case
    output, executeTime = evaluateTime(executedFunction)(inputValue)
    return {
      'Input': inputValue,
      'Output': output,
      'Expected Output': expectedOutout,
      'Correct': output == expectedOutout,
      'Execute Time': executeTime,
    }

  for index, case in enumerate(zip(test_inputs, expected_outputs)):
    print('==== Case #{} ===='.format(index))
    showResult(evaluate(case))

  return
