import re
import os
from colors import colors

USERNAME = os.getlogin()
TEMPLATE_PATH = ''

def main():
  print('Hello {}, what would you like to write today?'.format(USERNAME))
  print('You can simply copy and paste leetcode question here like: "1. Two Sum"')
  rawInput = input()
  matches = re.match(r'(^\d+)\.(.+)', rawInput)
  filename = ''
  if matches is not None:
    questionIndex, questionName = matches.groups()
    qName = questionName.strip().replace(' ', '').title()
    questionNameInCamelCase = qName[0].lower() + qName[1:]
    questionNameInUnderscore = questionName.strip().lower().replace(' ', '_')
    filename = '{}_{}.py'.format(questionIndex, questionNameInUnderscore)
  if filename is not '':
    template = open('./helpers/template.py', 'r')
    template = template.read()
    template = template.replace('{{functionName}}', questionNameInCamelCase)
    f = open('./{}'.format(filename), 'w')
    f.write(template)
    f.close()
    print(colors.okGreen('Creating file `{}` with `{}` template'.format(filename, template)))
  else:
    print(colors.watning('Cannot detect filename, please start over again.'))

if __name__ == '__main__':
  main()
