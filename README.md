<br>
<div align="center">

<h3 align="center">Truth Table Drawer and Equivalence Checker</h3>


  <p align="center">
    This project draws logical equation's truth tables, and check if two equations are equivalent.

![alt text](https://github.com/Mohamed-ElGemeie/Discrete-math-equation-tool/blob/main/examples/exp-imp-qvp.PNG?raw=True)    
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot](https://github.com/Mohamed-ElGemeie/Discrete-math-equation-tool/blob/main/examples/main_btn.PNG?raw=True)

This project was made as a submission for my university's "Discrete Math" course. Its aim is to teach discrete math basics to people unfamiliar with it, and create a nice animation while doing it, also designed to be simple and easy on the eye for new students and teachers testing new equations.<br><br> It takes from the user a logical equation using the specigied charahcters to draw that equation's truth table, and if the user passes two equations: it draws thier truth tables and check for their equivlence. 




### Built With

* [Python 3.9.5](https://www.python.org/downloads/release/python-395/)
    * Turtle 0.3.2 
    * Tkinter 0.1.0

<!-- GETTING STARTED -->
## Getting Started
To get started, download [Truth_table_drawer.py](https://github.com/Mohamed-ElGemeie/Discrete-math-equation-tool/blob/main/Truth_table_drawer.pyy)

### Prerequisites

Pip install libraries

* Pip install 
 ```sh
pip install tk
pip install PythonTurtle

  ```

<!-- USAGE -->
# Usage

## limits
You can only input the following characters:<br>
<br>Accepted Operations: 
<br>
<b>
v (OR)<br>^ (AND)<br>~ (NOT)<br>o (XOR)<br>> (Implies)<br>$ (Biconditional)<br>() (Brackets)</b>

Accepted Letter/Predicates/Variables:<br><b>
p , q , r , s</b><br><br>

## Usage examples

![alt text](https://github.com/Mohamed-ElGemeie/Discrete-math-equation-tool/blob/main/examples/exp-imp-qvp.PNG?raw=True)    
The not ( ~ ) operator takes the following argument (whatever is infront of it) as its variable, so please when using the ~ operator make sure that it follows a predicate/variable or a bracket that contains an equation.<br><br><pre>Examples:<br> p > q<br>~q > ~p _These two are equivalent_<br>--------------------------------<br>p v ~ p v r  _here is calculates ~ p then pairs it with r_<br>p v ~(p v r) _here it calculates (p v r) first ,then applies the ~ operator to them_</pre>
To understand how these variables and operators work,<br> _please refer to the [List of logic symbols](https://en.wikipedia.org/wiki/List_of_logic_symbols)_

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.




<!-- CONTACT -->
## Contact

Mohamed Elgemeie -- [Linkedin](https://www.linkedin.com/in/mohamed-elgemeie/) -- mgalal2002@outlook.com

Project Link: https://github.com/Mohamed-ElGemeie/Discrete-math-equation-tool/blob/main/Truth_table_drawer.py
