


class ModelForm:

    def __init__(self,*args,**kwargs):

        print("base form constructor")



class CategoryForm(ModelForm):

    def __init__(self, *args, **kwargs):

        self.user=kwargs.get("user")

        print("categor form constructor")

        super().__init__(*args, **kwargs)

    def clean(self):
        
        print(self.user)


class CategoryCreateView():

    def post(self,*args,**kwargs):

        user="django"
        form_instance=CategoryForm(user="django")

        form_instance.clean()

cat_instance=CategoryCreateView()

cat_instance.post()



