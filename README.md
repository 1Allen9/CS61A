# CS61A
CS61A course
## lab log
### lab00
**2025-02-23**
- lab00完成
- ok脚本的本地使用
- 非编程（write code）任务无法(--local)计分
- windows OS, use 'python'
- linux OS, use 'python3'
```bash
python ok -u --local #for: 1unlock
python ok --local #for: autograde
python ok --score --local #for autograde
```
### lab01
**2025-03-09**
done lab01

learned doctest
```py
def foo(x):
    """A random function.

    >>> foo(4)
    4
    >>> foo(5)
    5
    """
```
The lines in the docstring that look like interpreter outputs are the doctests. To run them, go to your terminal and type:
```bash
python3 -m doctest file.py
```
This effectively loads your file into the Python interpreter, and checks to see if each doctest input (e.g. foo(4)) is the same as the specified output (e.g. 4). If it isn't, a message will tell you which doctests you failed.

The command line tool has a -v option that stands for verbose.
```bash
python3 -m doctest file.py -v
```

**- optional question**
**2025-03-10**
done
## hw log
### hw01
**forgot date, someday in Feb**
done hw01
