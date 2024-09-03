

class BaseForm:

    def clean(self,*args,**kwargs):

        self.cleaned_data={"num1":10,"num2":20}

        return self.cleaned_data
    

class CategoryForm(BaseForm):

    def clean(self, *args, **kwargs):

        self.cleaned_data=super().clean()#{"num1":10,"num2":20}

        n1=self.cleaned_data.get("num1")

        if n1>50:

            print("n1 greater tahn 50")

        else:

            print("n1 < 50")

        return self.cleaned_data
    
form_instance=CategoryForm()

print(form_instance.clean())


