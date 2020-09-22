DevOps Lab 2020 summer


*********INSTALLATION INSTRUCTIONS********
wget https://bootstrap.pypa.io/get-pip.py -O - | python
pip install wheel
python setup.py bdist_wheel
pip install .
snapshot -t {$} -i {$}

t - txt or json allow parametrs - (output file format)
i - snapshot interval (sec)

default value t = txt, i=30


**********UNINSTALL*********
pip uninstall snapshot