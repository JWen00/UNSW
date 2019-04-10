LectWk08 # TODO: 

Flask cookie sessions 

```python

# Insecure way  (Raw) 
@app.route('/cook'): 
def say_cookies(): 
    if not request.cookies.get("food"): 
        res = make_response("Setting a cookie") 
        res.set_cookie("bood", "bar", max_age=60*60*24*365*2) # Gets stored on the client's local machine 

    else: 
        res = make_response("Value of cookie {} is {}".format("foodie", request.cookies))

    return res



# Secure way (Encrytion using flask) 
@app.route("/", methods=["GET", "POST"]) 
def index



def fetch_session_cart(): 
    # Creates a new cart first if the cart never existsed 
    if "cart" not in session: 
    print("Cart not in sessions') 
    cart = Cart() 
    session["cart"] = cart.id
    orders[cart.id] = cart 
```

url_for("fdsfd") --> looks for a particular function called fdsfd and links us to the route provided
