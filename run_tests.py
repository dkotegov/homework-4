# -*- coding: utf-8 -*-

import unittest
#Раздел консультаций
from consultations.main_page import MainPageTest
from consultations.consultant_page import ConsultantsPageTest
from consultations.one_consultant_page import OneConsultantPageTest
from consultations.rubric_page import RubricPageTest
from consultations.question_page import QuestionPageTest
from consultations.ask_page import AskPageTest
#Раздел лекарств
from drugs.tests.counter_test import CounterTest
from drugs.tests.links_in_drug_page_test import LinksTest
from drugs.tests.analogs_test import AnalogsTest
from drugs.tests.catalog_test import CatalogTest
from drugs.tests.leaders_os_sells_test import MedicamentsTestLeadersOfSellsTest
from drugs.tests.search_test import DrugsSearchTest
#Раздел учреждений
from company.tests.search_test import CompanySearchTest
from company.tests.company_list_test import CompanyListTest
from company.tests.dropdown_list_test import DropdownListTest
from company.tests.paginator_test import PaginatorTest
from company.tests.make_appointment_test import MakeAppointmentTest

if __name__ == '__main__':
    unittest.main()  
