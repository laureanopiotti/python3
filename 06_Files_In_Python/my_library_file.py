def save_to_file(content,filename):
    with open(filename,'w') as fp:
        fp.write(content)


def read_file(filename):
    with open(filename) as fp:
        return fp.read()