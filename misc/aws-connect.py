#!/usr/bin/env python3 

import datetime
import os
import sys
import configparser

# from termcolor import colored
# print(colored('hello', 'red'), colored('world', 'green'))

def aws_connect():

  def usage():
    """print usage"""
    print('Usage: %s [<deployment properties filename> [<aws-globals filename>]]' % sys.argv[0])
    exit(0)


  def check_envvars():
    """check if the environment variables required for deployment are set"""

    vars = 'USWITCH_PASSWORD', 'USWITCH_USERNAME', \
    'R_API_HOST_NAME', 'WWO_API_KEY', \
    'FIREHOSE_BUFFER_SECONDS', 'DATABASE_SERVER_NAME', \
    'DATABASE_PORT_NUMBER', 'DATABASE_USER', \
    'DATABASE_PASSWORD', 'REAL_TIME_INDEX_NAME', \
    'INTERVAL_INDEX_NAME', 'ES_HOST_NAME', \
    'REAL_TIME_ES_HOST_NAME', 'INTERVAL_ES_HOST_NAME', \
    'ES_PORT', 'WWO_API_KEY', \
    'CONTENTFUL_ACCESS_TOKEN', 'CONTENTFUL_SPACE_ID', \
    'R_API_HOST_NAME' # backslashes were required here, why didn't pylint complain?

    errors = 0
    for var in vars:
      val = os.getenv(var, None)
      if val is None:
        errors = errors + 1
        print(f'Error: {var} not found')
      else:
        print(f'{var}={val}')

    if errors > 0:
      print("\nbackend evironment variables are missing")
      print("have you run `. ./import_dev_secrets.sh`?")
      sys.exit('exiting.')

    print('\nDeployment environment variables all set (not necessarily correct!)\n')

  # both relative to parent dir so can be run from API or UI dir
  # depending on where you ran the env import scripts from
  deployment_path_default = '../trust-power-api/current-deployment.properties'
  aws_globals_path_default = '../TrustPowerUI/src/config/aws-globals.js'

  """parse command line"""
  """todo logic could be more elegant"""
  nargs = len(sys.argv)
  if nargs > 3:
    usage()
  if nargs == 1:
    deployment_path = deployment_path_default
    aws_globals_path = aws_globals_path_default
  elif nargs == 2:
    deployment_path = sys.argv[1]
    aws_globals_path = aws_globals_path_default
  elif nargs == 3:
    deployment_path = sys.argv[1]
    aws_globals_path = sys.argv[2]

  print('checking if the environment variables required for deployment are set:')
  check_envvars()

  # client_id, user_pool, api_resource_id, region

  # def copy_vars():
  """copy required values from backend to UI"""
  
  # print('Copying variables from', deployment_path, 'to', aws_globals_path)
  print(f'Reading variables from {deployment_path}:')

  # nonlocal client_id, user_pool, api_resource_id, region
  deployment = open(deployment_path, 'r')
  lines = deployment.readlines()
  for line in lines:
    if line.find('CLIENT_ID') != -1:
      client_id = line[line.find('=')+1:].strip()
    if line.find('USER_POOL') != -1:
      user_pool = line[line.find('=')+1:].strip()
    if line.find('API_RESOURCE_ID') != -1:
      api_resource_id = line[line.find('=')+1:].strip()
  deployment.close() # or do 'with open(file, 'r') as f: x = f.readlines()

  region = 'eu-west-1'

  try:
    if client_id and user_pool and api_resource_id and region:
      print('found all vars required for UI\n')
  except NameError:
    print('Error: var not found')
    sys.exit('exiting')

  def print_vars():
    print("export const IDENTITY_POOL_ID = 'eu-west-1:5a875129-ff88-40c5-8a38-5f320e214b44';")
    print(f"export const REGION = '{region}';")
    print(f"export const USER_POOL_ID = '{user_pool}';")
    print(f"export const USER_POOL_WEB_CLIENT_ID = '{client_id}';")
    print(f"export const ENDPOINT_AUTH = 'https://{api_resource_id}.execute-api.{region}.amazonaws.com/Test';")
    print("export const ANALYTICS_APP_ID = 'cbd4937d24514aeb8667b9782b042abc';")
    print("export const ANALYTICS_REGION = 'us-east-1';")
    sys.exit('exiting')

  def write_vars():
    """write the values of the required variables to the UI config file"""
    print(f"Writing UI AWS config file to {aws_globals_path}: ", end='')
    with open(aws_globals_path, 'w') as f:
      print(f'file opened OK for writing')

      # f.write(f"// this file created at {str(datetime.datetime.now())} by {sys.argv[0]}\n\n")
      f.write("export const IDENTITY_POOL_ID = 'eu-west-1:5a875129-ff88-40c5-8a38-5f320e214b44';\n")
      f.write(f"export const REGION = '{region}';\n")
      f.write(f"export const USER_POOL_ID = '{user_pool}';\n")
      f.write(f"export const USER_POOL_WEB_CLIENT_ID = '{client_id}';\n")
      f.write(f"export const ENDPOINT_AUTH = 'https://{api_resource_id}.execute-api.{region}.amazonaws.com/Test';\n")
      f.write("export const ANALYTICS_APP_ID = 'cbd4937d24514aeb8667b9782b042abc';\n")
      f.write("export const ANALYTICS_REGION = 'us-east-1';\n")
      
      print(f'finished writing to {aws_globals_path}\n')
      # sys.exit('exiting')

  # print_vars()
  write_vars()
  print(f'{sys.argv[0]} finished')

if __name__ == '__main__':
  """main"""
  aws_connect()

# cruft

  # prequel = 'export const '
  # with open(aws_globals_path, 'w') as f:
  #   f.write()

  # REGION // always 'eu-west-1'?
  # USER_POOL_WEB_CLIENT_ID // <- CLIENT_ID
  # USER_POOL_ID // <- USER_POOL
  # ENDPOINT_AUTH //from API_RESOURCE_ID=4up81glt8l
  # ANALYTICS_APP_ID // unchanged?
  # ANALYTICS_REGION // unchanged?
  # IDENTITY_POOL_ID // ? aws cognito-identity list-identity-pools --max-results 1

  # replace lines
  # with open(aws_globals_path, 'r') as f:
  #   lines = f.readlines()
  # # print(len(lines))

  # prequel = 'export const '

  # for i, line in enumerate(lines):
  #   print(i)
  #   if line.find('USER_POOL_ID') != -1:
  #     print(prequel + 'USER_POOL_ID = ' + user_pool)
  #   elif line.find('USER_POOL_WEB_CLIENT_ID`') != -1:
  #     print(prequel + 'USER_POOL_ID = ' + client_id)
  #   elif line.find('ENDPOINT_AUTH') != -1:
  #     print(prequel + 'ENDPOINT_AUTH = ' + 'https://' + api_resource_id + '.execute-api.eu-west-1.amazonaws.com/Test')
  #   else:
  #     print(line, end='')

  # print('finished.')
  # sys.exit()

  # export const IDENTITY_POOL_ID = 'eu-west-1:5a875129-ff88-40c5-8a38-5f320e214b44';
  # // aws cognito-identity list-identity-pools --max-results 1
  # // this has changed? Should it? why?
  # // not sure why but is used for social media etc oauth signups of which there are none currently
  # export const REGION = 'eu-west-1';
  # // this stays the same...
  # // Cognito General Settings - Pool Id, App client settings =>  App client Id
  # // export const USER_POOL_ID = 'eu-west-1_eMsKeaUZh';
  # export const USER_POOL_ID = 'eu-west-1_ybxNkyK3j'; // from current-deployment.properties:USER_POOL
  # // export const USER_POOL_WEB_CLIENT_ID = 'jqh7pktcpoagjeeh3sg8vcs49';
  # export const USER_POOL_WEB_CLIENT_ID = '6et2v2h396mi5c7nqkonekfr21'; // from current-deployment.properties:CLIENT_ID=6et2v2h396mi5c7nqkonekfr21
  # // API Gateway root Invoke URL
  # // API Gateway -> TrusPower-X-XX-X -> Stages -> "Test" => "Invoke URL"
  # // export const ENDPOINT_AUTH = 'https://gik0vkzv2l.execute-api.eu-west-1.amazonaws.com/Test';
  # export const ENDPOINT_AUTH =
  #   'https://4up81glt8l.execute-api.eu-west-1.amazonaws.com/Test'; // from API_RESOURCE_ID=4up81glt8l
  # // Pinpoint project ID, region
  # // these stay the same?
  # export const ANALYTICS_APP_ID = 'cbd4937d24514aeb8667b9782b042abc';
  # export const ANALYTICS_REGION = 'us-east-1';
  # REGION // always 'eu-west-1'?
  # USER_POOL_WEB_CLIENT_ID // <- CLIENT_ID
  # USER_POOL_ID // <- USER_POOL
  # ENDPOINT_AUTH //from API_RESOURCE_ID=4up81glt8l
  # ANALYTICS_APP_ID // unchanged?
  # ANALYTICS_REGION // unchanged?
  # IDENTITY_POOL_ID // ? aws cognito-identity list-identity-pools --max-results 1


  # try:
  #     # print('config_file: ', config_file)
  #     # pass
  #     raise Exception('this is a test Exception')
  # except ValueError:
  #     # usage()
  #     print('an error occurred. exiting.')
  #     sys.exit()

  # config = configparser.ConfigParser()
  # config['test'] = {
  #   'test1' : '1',
  #   'test2' : '2',
  #   'test3' : 'abc',
  # }
  # print(config)

  # with open('test.ini', 'w') as awsfile:
  #   config.write(awsfile)
    # print('stuff')
