# from db.db import Database
from bs4 import BeautifulSoup
import requests
import re

class IP2:  
    def __init__(self):
        # self.__db = Database()
        self.project_id = 0
        self.loggedOn = False

    def search(self, params):
        """ convenience method """
        self.login(params['username'], params['password'])
        self.set_project_id()
        self.set_experiment_id()
        self.set_experiment_path()
        self.upload_spectra(params['files'])
        self.prolucid_search(params['search_criteria'])
        self.check_job_status()

    def login(self, username, password):
        """ login to IP2 """
        login_req = requests.post('http://goldfish.scripps.edu/ip2/j_security_check', {
            'j_username': username,
            'j_password': password,
            'rememberMe': 'on',
            'login': 'Login'
        })

        self.cookies = login_req.history[0].cookies

        return True

    def set_project_id(self):
        """ get project id for cravattdb project or else create new project """

        project_id = self.__find_project_id()

        if not project_id:
            self.__create_new_project()
            project_id = self.__find_project_id()

        self.project_id = project_id
        return project_id

    def set_experiment_id(self, name):
        exp_req = requests.get('http://goldfish.scripps.edu/ip2/viewExperiment.html', {
            'projectName': 'cravattdb',
            'pid': self.project_id
        }, cookies=self.cookies)

        soup = BeautifulSoup(exp_req.text)
        table = soup.find('table', id='experimentO')
        forms = table.find_all('form', action="editExperiment.html")

        for form in forms:
            sampleInput = form.find('input', attrs={'name':'sampleName'}, value=name)

            if sampleInput:
                self.experiment_id = int(form.find('input', attrs={'name': 'expId'})['value'])
                return

    def set_experiment_path(self):
        path_req = requests.get(
            'http://goldfish.scripps.edu/ip2/eachExperiment.html', 
            {
                'experimentId': self.experiment_id,
                'projectName': 'cravattdb',
                'pid': self.project_id
            },
            cookies = self.cookies
        )

        soup = BeautifulSoup(path_req.text)

        # soup.find('b', text="Spectra Path:").next_sibling.string.strip().replace('/spectra', '')
        text = soup.find('div', class_='add_spectra').find('script', text=re.compile(r'.+expPath.+')).contents[0]
        path = re.search('"expPath":\s"([\w/]+)"', text)
        self.experiment_path = path.group(1)


    def create_experiment(self, name):
        """ create experiment under project """

        requests.post(
            'http://goldfish.scripps.edu/ip2/addExperiment.html',
            {
                'pid': self.project_id,
                'projectName': 'cravattdb',
                'sampleName': name,
                'sampleDescription': '',
                'instrumentId': 34,
                'month': 6,
                'date': '03',
                'year': 2015,
                'description': ''
            },
            cookies=self.cookies
        )

    def upload_spectra(self, files):
        """ upload .ms2 files """
        for f in files:
            requests.post(
                'http://goldfish.scripps.edu/helper/spectraUpload.jsp',
                {
                    'Filename': f.name,
                    'expPath': self.experiment_path,
                    'Filedata': f,
                    'Upload': 'Submit Query'
                },
                cookies=self.cookies,
                files={ f.name: f}
            )

    def prolucid_search(self):
        """ perform prolucid search """

        self.__db.execute('SELECT FROM ')
        requests.post(
            'http://goldfish.scripps.edu/ip2/prolucidProteinId.html',
            )

    def check_job_status(self):
        """ check if job is finished """

    def get_dtaselect(self):
        """ finally grab what we came for """

    def __find_project_id(self):
        project_req = requests.get(
            'http://goldfish.scripps.edu/ip2/viewProject.html',
            cookies=self.cookies
        )

        text = project_req.text
        index = text.find('cravattdb')

        if index != -1:
            text = text[index:]
            return int(re.search('viewExperiment\.html\?pid=(\d+)', text).group(1))
        else:
            return False


    def __create_new_project(self):
        """ create new ip2 project for cravattdb experiments """
        requests.post(
            'http://goldfish.scripps.edu/ip2/addProject.html', 
            {
                'projectName': 'cravattdb2',
                'desc': ''
            },
            cookies=self.cookies
        )