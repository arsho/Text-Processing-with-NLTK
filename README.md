# Text-Processing-with-NLTK

### Installation procedure of NLTK (Natural Language Toolkit)
The following steps are performed in a ```Windows 10 (64 bit)``` machine with ```Python 3.5.2``` installed. 

* To check Python version open CMD and use this command:
```python --version```
* Create a folder. In my case I have created a folder named ```nltk```. Open CMD inside  it. Keep the CMD open for following steps.
* Install necessary packages for ```nltk``` inside a virtual environment. If you don't have virtualenv installed, install it using ```pip install virtualenv```.
* In CMD perform the following commands to create a virtual environment and to download packages inside it. Here ```D:\pyPrac\nltk``` is my path of current directory. It will differ in your case.
  ```text
  D:\pyPrac\nltk>virtualenv venv
  D:\pyPrac\nltk>venv\Scripts\activate.bat
  (venv) D:\pyPrac\nltk>pip install -U nltk
  (venv) D:\pyPrac\nltk>pip install numpy
  (venv) D:\pyPrac\nltk>python -m idlelib
  ```
* The last command will open IDLE. We use IDLE inside the virtual environment each time we are going to use NLTK package. Using this IDLE (opened inside the virtual environment), create a ```Python``` file in the same folder and run the following snippet to check if ```nltk``` has been installed properly.
  ```python
  import nltk
  print(nltk.__version__) #Output: 3.2.2
  ```
* To download ```nltk``` data, create a ```Python``` file in the same virtual environment and run the following snippet.
  ```python
  import nltk
  nltk.download()
  ```
	Select all from menu to download and set directory to: ```C:\nltk_data```. It will take around an hour to complete downloading the data. Ignore if it shows ```outdated``` for some fields.
* That's it! :+1: Here are some CMD commands you need to remember:
	* Activating virtual environment that we have created earler: ```venv\Scripts\activate.bat```
	* Open IDLE inside this virtual environment: ```(venv) D:\pyPrac\nltk>python -m idlelib```


### Book Information
* Python 3 Text Processing with NLTK 3 Cookbook by Jacob Perkins

### Code List
* Tokeinizing text into sentence: [tokenizing_text_into_sentence.py](https://github.com/arsho/Text-Processing-with-NLTK/blob/master/tokenizing_text_into_sentence.py)

#### References:

 * [NLTK website](http://www.nltk.org/index.html)
 * [NLTK official documentation to install nltk (without using virtualenv)](http://www.nltk.org/install.html)
 * [NLTK official documentation to install nltk data](http://www.nltk.org/data.html)
 * [StackOverflow Question: Reading Bengali with python Natural Language Toolkit](http://stackoverflow.com/questions/42718792/reading-bengali-with-python-natural-language-toolkit)

