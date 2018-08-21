import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--my-parameter', help='test parameter', default='myid123')
    args = parser.parse_args()

    print('Code within Docker Container launched successfully on Google Compute Engine')
    print('MY PARAMETER: ', args.my_parameter)
