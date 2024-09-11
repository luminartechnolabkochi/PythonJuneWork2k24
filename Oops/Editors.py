

class Editor:
    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    def open(self):

        print(f"{self.name} open ")

    def execute(self):

        print(f"{self.name} execute")

class Vscode(Editor):

    def __init__(self, name, vendor):

        super().__init__(name,vendor)


class PyCharm(Editor):

    def __init__(self, name, vendor):
        super().__init__(name, vendor)


vsc_instance=Vscode("visualstudiocode","vscvendor")

vsc_instance.open()

pyc_instance=PyCharm("pycharm","jetbrains")

pyc_instance.open()


