# Set and Unset DNS  Python

A cross-platform python app to set and unset primary and secondary DNS

## How does it work

First of all, be sure that `python` has been installed and be added to the path.
You can be sure of that by typing the `python3 -V` command on your terminal and
it should respond you something like this:

`Python 3.11.2`

After that, we have two ways to set or unset the DNS:

### Easy Way

You can double-click <`name`_dns.py> to automatically run and set the dns, or
double-click <unset_dns.py> to unset the dns.

Note that you should set your os to open .py files with python to work;
Or you can simply run this command in your terminal to run the above files like as you always run a python program:

```
python3 <x_dns.py>
```

or

```
python <x_dns.py>
```

or

```
py <x_dns.py>
```

Try which one works for you.

You can make your own custom DNS. Just copy the file and change the primary and secondary ip in the file.

### Fundamental Way

Run this command in the directory that `core.py` file exists:

```
python3 core.py <primary_dns> <secondary_dns>
```

or

```
python core.py <primary_dns> <secondary_dns>
```

or

```
py core.py <primary_dns> <secondary_dns>
```

Try which one works for you.

## How to Install

First download and unzip the app.

Then run this file to install all the requirements:

```
pip install -r ./requirements.txt
```

or

```
pip3 install -r ./requirements.txt
```

Now you can use it.

Enjoy :)

## Notes

- If this script is not working for you try to run the terminal as administrator or super-user and then run python file
  in terminal.
- If the terminal windows pop-ups and it takes relatively a lot of time, don't close it and let it finishes its job.
  The pop-ups should be closed automatically