import subprocess
import os


def version(path_to_bin):
    args = (os.path.join(path_to_bin, 'version'))
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    version_str = popen.stdout.read().decode("utf-8")
    for line in version_str.split("\n"):
        print(line)


def train(path_to_bin, config_file, train_path, mode, output_model="", previous_model="", dev_path="", train_ext="*",
          dev_ext="*", cross_validation=0):
    args =[]
    args.append(os.path.join(path_to_bin, 'nlptrain'))
    args.extend(["-c", config_file])
    args.extend(["-t", train_path])
    args.extend(["-mode", mode])
    args.extend(["-cv", str(cross_validation)])
    if output_model:
        args.extend(["-m", output_model])
    if previous_model:
        args.extend(["-p", previous_model])
    if dev_path:
        args.extend(["-d", dev_path])
    if train_ext:
        args.extend(["-te", train_ext])
    if dev_ext:
        args.extend(["-de", dev_ext])
    popen = subprocess.Popen(args, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(popen.stdout.readline, ""):
        print(line)
    popen.wait()


def decode(path_to_bin, config_file, input_path, input_ext="*", output_ext="nlp", format="raw", threads=2):
    args = []
    args.append(os.path.join(path_to_bin, 'nlpdecode'))
    args.extend(["-c", config_file])
    args.extend(["-i", input_path])
    args.extend(["-ie", input_ext])
    args.extend(["-oe", output_ext])
    args.extend(["-format", format])
    args.extend(["-threads", str(threads)])
    popen = subprocess.Popen(args, stdout=subprocess.PIPE, bufsize=1)
    for line in iter(popen.stdout.readline, ""):
        print(line)
    popen.wait()
