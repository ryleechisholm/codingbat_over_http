from django.http import response
from django.test import SimpleTestCase


class TestNearHundred(SimpleTestCase):
    def test_near_hundred_43(self):
        response = self.client.get("/near-hundred/43/")
        self.assertContains(response, False)

    def test_near_hundred_98(self):
        response = self.client.get("/near-hundred/98/")
        self.assertContains(response, True)

    def test_near_hundred_200(self):
        response = self.client.get("/near-hundred/200/")
        self.assertContains(response, True)

class TestStringSplosion(SimpleTestCase):
    def test_hello(self):
        response = self.client.get("/string-splosion/hello/")
        self.assertContains(response, "hhehelhellhello")
    
    def test_coding(self):
        response = self.client.get("/string-splosion/coding/")
        self.assertContains(response, "ccocodcodicodincoding")

    def test_tangerine(self):
        response = self.client.get("/string-splosion/tangerine/")
        self.assertContains(response, "ttatantangtangetangertangeritangerintangerine")

class TestCatDog(SimpleTestCase):
    def test_cat_dog_true1(self):
        response = self.client.get("/cat-dog/catcatdogdogdflkffdkjfdfdkj/")
        self.assertContains(response, True)

    def test_cat_dog_true2(self):
        response = self.client.get("/cat-dog/catdogcatdogyellowdogcat/")
        self.assertContains(response, True)

    def test_cat_dog_false(self):
        response = self.client.get("/cat-dog/catcatcatdog/")
        self.assertContains(response, False)

class TestLoneSum(SimpleTestCase):
    def test_lone_sum_2_3_3(self):
        response = self.client.get("/lone-sum/2/3/3/")
        self.assertContains(response, "2")
        
    def test_lone_sum_1_2_3(self):
        response = self.client.get("/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_lone_sum_all_3(self):
        response = self.client.get("/lone-sum/3/3/3/")
        self.assertContains(response, "0")