import time

import pytest
import sys

sys.path.append('/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest')
from utilities.Baseclass import Baseclass
from Pages import HomePage
from Pages import HomePage
from Pages.Datadriven_usercreation import Datadriven


@pytest.mark.usefixtures('setup')
class Test_Datadriven(Baseclass):

    def test_login_to_orangehrm(self):
        print('Login test')
        login_obj = HomePage.Login_page(self.driver)
        login_obj.login_to_orangeHrm()
        time.sleep(2)

    def test_userCreate(self):
        file = Datadriven(self.driver)
        file.add_user()


obj = Test_Datadriven()
obj.test_login_to_orangehrm
obj.test_userCreate
