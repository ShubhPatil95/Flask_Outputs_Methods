# Flask_Outputs_Methods
In this repository I have mentioned about some methods by which we can show our outputs of flask app. 
These methods would proof very hady in the development and testing phase of app and will reduce your depedancy on front end team for interface development.

PLease refer below sections and follow the step by step approach.

<details><summary> <h2> 01-Constant_Inputs.py </h2> </summary>
<p>

<strong> Here in this section we can see how flask app will work taking the constant inputs </strong> 

* Create a folder Flask_App and move into same
```ruby
mkdir Flask_App
cd Flask_App
```
* Create a file 01-Constant_Inputs.py and copy paste code from [01-Constant_Inputs.py](https://github.com/ShubhPatil95/Flask_Outputs_Methods/blob/main/01-Constant_Inputs.py)
```ruby
touch 01-Constant_Inputs.py
```
* Run a file 01-Constant_Inputs.py in spyder or run through command line interface
```ruby
python3 01-Constant_Inputs.py
```
* Click below URL's to check the outputs
<br>[For Addition Click Me](http://localhost:8000/addition) [For Substraction Click Me](http://localhost:8000/substraction)</br>
 
* Now you can read and try to understand code written in 01-Constant_Inputs.py and for any questions feel free to reach out to me on linkedin [Shubham Patil](https://www.linkedin.com/in/datascientistshubhampatil)
</p>
</details>

<details><summary> <h2> 02-Inputs_Through_URL.py </h2> </summary>
<p>

<strong> Here in this section we will see how can we pass inputs through URL </strong> 

* Create a folder Flask_App and move into same
```ruby
mkdir Flask_App
cd Flask_App
```
* Create a file 02-Inputs_Through_URL.py and copy paste code from [https://github.com/ShubhPatil95/Flask_Outputs_Methods/blob/main/02-Inputs_Through_URL.py)
```ruby
touch 02-Inputs_Through_URL.py
```
* Run a file 02-Inputs_Through_URL.py in spyder or run through command line interface
```ruby
python3 02-Inputs_Through_URL.py
```
* Click below URL's to check the outputs. Here you can put any value of a and b and it will give you addition and substraction.
  - e.g If you want to do addition of 10 and 20 then URL should be http://localhost:8000/addition?a=10&b=20
<br>[For Addition Click Me](http://localhost:8000/addition?a=100&b=100) [For Substraction Click Me](http://localhost:8000/substraction?a=100&b=100)</br>
 
* Now you can read and try to understand code written in 02-Inputs_Through_URL.py and for any questions feel free to reach out to me on linkedin [Shubham Patil](https://www.linkedin.com/in/datascientistshubhampatil)
</p>
</details>

<details><summary> <h2> 03-Inputs_Through_Swagger.py </h2> </summary>
<p>

<strong> Here in this section we will use swagger to pass inputs to app, which would be very convinient in development phase</strong> 

* Create a folder Flask_App and move into same
```ruby
mkdir Flask_App
cd Flask_App
```
* Create a file 03-Inputs_Through_Swagger.py and copy paste code from [03-Inputs_Through_Swagger.py](https://github.com/ShubhPatil95/Flask_Outputs_Methods/blob/main/03-Inputs_Through_Swagger.py)
```ruby
touch 03-Inputs_Through_Swagger.py
```
* Run a file 03-Inputs_Through_Swagger.py in spyder or run through command line interface
```ruby
python3 03-Inputs_Through_Swagger.py
```
* Click below URL's to open swagger. 
<br>[Click Here To Go To Swagger](http://localhost:8000/apidocs)</br>
 
* Click On [addition] or [substraction] drop down=> click on [Try it Out] => Enter First and Second number=> Click [Execute] => Check output in [Response body]
<br>[Click Here To Go To Swagger](http://localhost:8000/apidocs)</br>

* Now you can read and try to understand code written in 03-Inputs_Through_Swagger.py and for any questions feel free to reach out to me on linkedin [Shubham Patil](https://www.linkedin.com/in/datascientistshubhampatil)
</p>
</details>



<details><summary> <h2> 04-Inputs_Through_HTML.py </h2> </summary>
<p>

<strong> Here in this section we will see how to connect HTML page with flask app to take inputs and show outputs</strong> 

* Create a folder Flask_App and move into same
```ruby
mkdir Flask_App
cd Flask_App
```
* Create a file 04-Inputs_Through_HTML.py and copy paste code from [04-Inputs_Through_HTML.py](https://github.com/ShubhPatil95/Flask_Outputs_Methods/blob/main/04-Inputs_Through_HTML.py)
```ruby
touch 04-Inputs_Through_HTML.py
```
* Create a folder templates and create a file index.html and copy paste code from [index.html](https://github.com/ShubhPatil95/Flask_Outputs_Methods/blob/main/templates/index.html)
```ruby
mkdir templates
cd mkdir 
touch index.html
```  
* Run a file 04-Inputs_Through_HTML.py in spyder or run through command line interface
```ruby
python3 04-Inputs_Through_HTML.py
```
* Click below URL's to open swagger. 
<br>[Click Here To Open App URL](http://localhost:8000)</br>
 
* On App page, Enter First and Second number and then enter SUM or SUB for addition and substraction respectively.

* Now you can read and try to understand code written in 03-Inputs_Through_Swagger.py and for any questions feel free to reach out to me on linkedin [Shubham Patil](https://www.linkedin.com/in/datascientistshubhampatil)
</p>
</details>

Among above methods we can choose any one to see our app output while developing any flask application.
