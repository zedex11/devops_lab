DevOps Lab 2020 summer


####INSTALLATION INSTRUCTIONS###
.
.
.
wget https://bootstrap.pypa.io/get-pip.py -O - | python

pip install wheel

python setup.py bdist_wheel

pip install .
.
.
.
.
###USING###
.
.
.
snapshot -t {$} -i {$}

t - txt or json allow parametrs - (output file format)

i - snapshot interval (sec)

expample: snapshot -t json -i 15

(default value - t = txt, i=30)
.
.
.
.
###UNINSTALL###
.
.
pip uninstall snapshot