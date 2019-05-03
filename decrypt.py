import argparse
import zlib

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--inputfile', type=str, required=True, help='input file')
parser.add_argument('-o', '--outputfile', type=str, default='decompress.eps', help='output file')
args = parser.parse_args()

def decompressPostscript(path):
    with open(path, 'rb') as f:
        data = f.read()
        result = zlib.decompress(data, -15)
        return result

def postscriptTofile(binary_data, filename):
    with open(filename, 'wb') as f:
        f.write(binary_data)

def main():
    path = args.inputfile
    output = args.outputfile
    
    binary_data = decompressPostscript(path)
    postscriptTofile(binary_data, output)

    print('Done')

if __name__ == '__main__':
    main()