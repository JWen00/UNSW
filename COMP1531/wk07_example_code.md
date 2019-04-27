
# Flask 

Flask instance is will handle all the http request parameters  
For every URL, it needs to map to a python function 

### Methods 'GET' and 'POST' 

If the method is set as 'GET' in the html form, values are passed in through the URL, for example: 

> `localhost::8080/?name=dsad&acc=pre` 

However, this is insecure, and when we collect information from the user, we want to use 'POST' method. 

Consider `@app.route('/', methods=["GET", "POST"])`
> Note: '/' is also known as the landing page 

Having two methods means that when we initially load the landing page we use a 'GET' request  

But when we collect information from our form, we use a POST' request. 


