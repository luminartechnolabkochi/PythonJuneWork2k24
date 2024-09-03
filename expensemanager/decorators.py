


def login_required(fn):

    def wrapper(request,*args,**kwargs):

        if not request.user.is_authenticated:

            messages.error(request,"invalid session")
            return redirect("signin")
        else:
            
            return fn(request,*args,**kwargs)
    return wrapper



@lo
def get(self,request,*args,**kwargs):

    print("some code block inside get")


def post(self,request,*args,**kwargs):

    print("some code block inside get")



    
