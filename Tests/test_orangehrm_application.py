import pytest
import sys

sys.path.append('/Users/sudhansu/Desktop/Folder/My Projects/Selenium project/seleniumPytest')
from utilities.Baseclass import Baseclass
from Pages import HomePage
from Pages import Dahsboard_Menu


@pytest.mark.usefixtures('setup')
class Test_OrangeHrm(Baseclass):
    def test_login_to_orangehrm(self):
        print('Login test')
        login_obj = HomePage.Login_page(self.driver)
        login_obj.login_to_orangeHrm()

    def test_dashboard_menu(self):
        dahsboard = Dahsboard_Menu.Dashboard_menu(self.driver)
        dahsboard.check_menus()

    def test_search_menu(self):
        dahsboard = Dahsboard_Menu.Dashboard_menu(self.driver)
        size = len(dahsboard.menu_names)
        for i in range(size - 1):
            dahsboard.test_search_functionality(size=size, menu_names=dahsboard.menu_names[i])


obj =Test_OrangeHrm()
obj.test_login_to_orangehrm
obj.test_dashboard_menu
