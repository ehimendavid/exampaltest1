# Exampal mobile app project
# written by Ehimen David
# 2023
from kivy.properties import StringProperty, ListProperty
from kivy.uix import checkbox
from kivy.uix.button import Button
# Importing the right modules
from kivymd.app import MDApp
from kivy.uix.widget import Widget
import json
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.list import BaseListItem, IRightBodyTouch, OneLineRightIconListItem, TwoLineRightIconListItem
from kivymd.uix.pickers import MDTimePicker
from kivy.clock import Clock
import datetime
from kivymd.uix.label import MDLabelLabel

from kivy.core.text.markup import MarkupLabel
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.selectioncontrol import MDCheckbox

#from .label import MDIcon, MDLabel
# setting all variable

TotalScore = 0


# All the class for the screens



class MDLabelLabel(MDLabelLabel):
    markup: True
    def on_text(self, *args, **Kwargs):
        self.adjust_font_size()

    def on_size(self, *args, **Kwargs):
        self.adjust_font_size()
    def adjust_font_size(self):
        font_size = self.font_size
        while True:
            lbl = MarkupLabel(font_name=self.font_name, font_size=font_size, text=self.text)
            lbl.refresh()
            lbl_available_height = self.height - self.padding_y * 2
            lbl_available_width = self.width - self.padding_x * 2
            if font_size > lbl_available_width:
                font_size = lbl_available_height
            elif lbl.content_width > lbl_available_width or \
                lbl.content_height > lbl_available_height:
                font_size *= 0.95
            else:
                break

        while True:
            lbl = MarkupLabel(font_name=self.font_name, font_size=font_size, text=self.text)
            lbl.refresh()
            if lbl.content_width * 1.1 <  lbl_available_width and \
                lbl.content_height * 1.1 < lbl_available_height:
                font_size *= 1.05
            else:
                break
class HomePage(Screen):
    pass


class ProfilePage(Screen):
    pass

class SearchPage(Screen):
    pass


class InfoPage(Screen):
    pass


class SettingsPage(Screen):
    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()

    def get_time(self,instance, time):
        print(time)

    def schedule(self, *args):
        pass


'''class BaseistItemWithSwitch(BaseListItem):

class BaseListItemListSwitch(BaseListItem):

class RightSwitchContainer(IRightBodyTouch, MDSwitch):

class OneLineListItemWithSwitch(OneLineRightIconListItem, BaseListItemListSwitch):
    pass

class TwoLineListItemWithSwitch(TwoLineRightIconListItem, BaseListItemListSwitch):
    pass'''


class WaecSubject(Screen):
    pass


class NecoSub(Screen):
    pass


class JambSubject(Screen):
    pass


class MockSub(Screen):
    pass


class Syllabus(Screen):
    pass


class JambGuide(Screen):
    pass


class MathematicsYear(Screen):
    pass

class clicked(MDRaisedButton):
    pass




class Math2023(Screen):
    colors = ListProperty([2,0,0,5])

    counter=0

    press_property = StringProperty('0')

    def on_press_button(self):
        """TotalScore = + 1
        print(TotalScore)"""
        self.counter+=1
        self.press_property = str(self.counter)

    SecondCounter = 0

    press_property = StringProperty('0')

    def on_press_secondbutton(self):
        if self.ids.correct_button1.md_bg_color == [255, 230, 0, 1]:
            self.SecondCounter += 1
            self.press_property = str(self.SecondCounter)
        else:
            self.SecondCounter -= 1
            self.press_property = str(self.SecondCounter)


    def checkbox_click(self, instance, value, topping, score):
        if value == True:
            print(str(1))
            self.counter += 1
            self.press_property = str(self.counter)
        else:
            self.counter -= 1
            self.press_property = str(self.counter)

    def check(self):
        print('hello')


    #correct Butttttoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooon#

    def set_text12(self):
        if self.ids.wrong_button.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_button.md_bg_color = 255, 230, 0, 1

        else:
            self.ids.wrong_button.md_bg_color = [2, 0, 0, 5]

    def set_text13(self):
        if self.ids.wrong_b2n.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_b2n.md_bg_color = 255, 230, 0, 1

        else:
            self.ids.wrong_b2n.md_bg_color = [2, 0, 0, 5]


    def set_text1(self):
        if self.ids.correct_button1.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_button1.md_bg_color = 255, 230, 0, 1
            self.SecondCounter += 1
            self.press_property = str(self.SecondCounter)
        else:
            self.ids.correct_button1.md_bg_color = [2, 0, 0, 5]
            self.SecondCounter -= 1
            self.press_property = str(self.SecondCounter)

    def set_text2(self):
        if self.ids.correct_button2.md_bg_color == [2,0,0,5]:
            self.ids.correct_button2.md_bg_color = 255, 230, 0, 1
            self.SecondCounter += 1
            self.press_property = str(self.SecondCounter)
        else:
            self.ids.correct_button2.md_bg_color = [2,0,0,5]
            self.SecondCounter -= 1
            self.press_property = str(self.SecondCounter)

    def set_text3(self):
        if self.ids.correct_button3.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_button3.md_bg_color = 255, 230, 0, 1
            self.SecondCounter += 1
            self.press_property = str(self.SecondCounter)
        else:
            self.ids.correct_button3.md_bg_color = [2, 0, 0, 5]
            self.SecondCounter -= 1
            self.press_property = str(self.SecondCounter)

    def set_text4(self):
        if self.ids.correct_button4.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_button4.md_bg_color = 255, 230, 0, 1
            self.SecondCounter += 1
            self.press_property = str(self.SecondCounter)
        else:
            self.ids.correct_button4.md_bg_color = [2, 0, 0, 5]
            self.SecondCounter -= 1
            self.press_property = str(self.SecondCounter)

    def set_text5(self):
        if self.ids.correct_button5.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_button5.md_bg_color = 255, 230, 0, 1
            self.SecondCounter += 1
            self.press_property = str(self.SecondCounter)
        else:
            self.ids.correct_button5.md_bg_color = [2, 0, 0, 5]
            self.SecondCounter -= 1
            self.press_property = str(self.SecondCounter)

    #Wrong Buttttttttttttttooooooooooooooooooooooooooooooooooooooooooooonnnnnnnnnnnnnn#

    #1st Q wrong button

    def show_wrong1(self):
        if self.ids.wrong_button1.md_bg_color == [2,0,0,5]:
            self.ids.wrong_button1.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_button1.md_bg_color = [2, 0, 0, 5]


    def show_wrong3(self):
        if self.ids.wrong_button3.md_bg_color == [2,0,0,5]:
            self.ids.wrong_button3.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_button3.md_bg_color = [2,0,0,5]

    def set_text22(self):
        if self.ids.wrong2_1.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong2_1.md_bg_color = 255, 230, 0, 1

        else:
            self.ids.wrong2_1.md_bg_color = [2, 0, 0, 5]

    def set_text23(self):
        if self.ids.wrong2_2.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong2_2.md_bg_color = 255, 230, 0, 1

        else:
            self.ids.wrong2_2.md_bg_color = [2, 0, 0, 5]

    def set_text24(self):
        if self.ids.wrong2_3.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong2_3.md_bg_color = 255, 230, 0, 1

        else:
            self.ids.wrong2_3.md_bg_color = [2, 0, 0, 5]




    # 2nd Q wrong button
    def show_2_wrong1(self):
        self.ids.wrong2_1.md_bg_color = 255, 230, 0, 1

    def show_2_wrong2(self):
        self.ids.wrong2_2.md_bg_color = 255, 230, 0, 1

    def show_2_wrong3(self):
        self.ids.wrong2_3.md_bg_color = 255, 230, 0, 1


    #Third Wrong Buuuuuuuuuutttttttttttttttttttttttttttttooooooooooooooooooooooooooooooooon
    def wrong3_1(self):
        if self.ids.wrong_31.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_31.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_31.md_bg_color = [2, 0, 0, 5]

    def wrong3_2(self):
        if self.ids.wrong_32.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_32.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_32.md_bg_color = [2, 0, 0, 5]

    def wrong3_3(self):
        if self.ids.wrong_33.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_33.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_33.md_bg_color = [2, 0, 0, 5]

    #4th WRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRooooooooooooooonnnnnnnnggggggggg BBBBBBBBBbbbuuuuuuuuuutttttttoooooooonnnnn

    def wrong4_1(self):
        if self.ids.wrong_41.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_41.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_41.md_bg_color = [2, 0, 0, 5]

    def wrong4_2(self):
        if self.ids.wrong_42.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_42.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_42.md_bg_color = [2, 0, 0, 5]

    def wrong4_3(self):
        if self.ids.wrong_43.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_43.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_43.md_bg_color = [2, 0, 0, 5]


#5th WRRRRRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOONNNNNNNNNNNNNNBUTTTTTTTTTTON
    def wrong5_1(self):
        if self.ids.wrong_51.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_51.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_51.md_bg_color = [2, 0, 0, 5]

    def wrong5_2(self):
        if self.ids.wrong_52.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_52.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_52.md_bg_color = [2, 0, 0, 5]

    def wrong5_3(self):
        if self.ids.wrong_53.md_bg_color == [2, 0, 0, 5]:
            self.ids.wrong_53.md_bg_color = 255, 230, 0, 1
        else:
            self.ids.wrong_53.md_bg_color = [2, 0, 0, 5]



    def set_score(self):
        self.ids._totalscore.text = self.press_property
        self.ids.correct_button1.md_bg_color = 0, 230, 0, 1
        self.ids.correct_button2.md_bg_color = 0, 230, 0, 1
        self.ids.correct_button3.md_bg_color = 0, 230, 0, 1
        self.ids.correct_button4.md_bg_color = 0, 230, 0, 1
        self.ids.correct_button5.md_bg_color = 0, 230, 0, 1
        if self.press_property >= "5":
            self.ids._grade.text = "A1"
        elif self.press_property == "4":
            self.ids._grade.text = "B2"
        elif self.press_property == "3":
            self.ids._grade.text = "C6"
        elif self.press_property == "2":
            self.ids._grade.text = "D7"
        elif self.press_property == "1":
            self.ids._grade.text = "E8"
        else:
            self.ids._grade.text = "F9"


#ALTERNAAAAAAAAAAAAAAATTTTTTTTTTTTIVVVVVVVVVVEEEEEEEEEEE  FOR MATHHHHHHHHHHHHSSSSSSSSSSSSS

    AlternateCounter = 0

    press_property = StringProperty('0')

    def set_2text1(self):
        if self.ids.correct_2button1.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_2button1.md_bg_color = 255, 230, 0, 1
            self.AlternateCounter += 1
            self.press_property = str(self.AlternateCounter)
        else:
            self.ids.correct_2button1.md_bg_color = [2, 0, 0, 5]
            self.AlternateCounter -= 1
            self.press_property = str(self.AlternateCounter)

    def set_2text2(self):
        if self.ids.correct_2button2.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_2button2.md_bg_color = 255, 230, 0, 1
            self.AlternateCounter += 1
            self.press_property = str(self.AlternateCounter)
        else:
            self.ids.correct_2button2.md_bg_color = [2, 0, 0, 5]
            self.AlternateCounter -= 1
            self.press_property = str(self.AlternateCounter)

    def set_2text3(self):
        if self.ids.correct_2button3.md_bg_color == [2, 0, 0, 5]:
            self.ids.correct_2button3.md_bg_color = 255, 230, 0, 1
            self.AlternateCounter += 1
            self.press_property = str(self.AlternateCounter)
        else:
            self.ids.correct_2button3.md_bg_color = [2, 0, 0, 5]
            self.AlternateCounter -= 1
            self.press_property = str(self.AlternateCounter)

    def alternative_q11(self):
        if self.ids._alt_q11.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q11.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q11.md_bg_color = [2, 0, 0, 5]

    def alternative_q12(self):
        if self.ids._alt_q12.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q12.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q12.md_bg_color = [2, 0, 0, 5]

    def alternative_q13(self):
        if self.ids._alt_q13.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q13.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q13.md_bg_color = [2, 0, 0, 5]

    #2nd wrong for alternative
    def alternative_q21(self):
        if self.ids._alt_q21.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q21.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q21.md_bg_color = [2, 0, 0, 5]

    def alternative_q22(self):
        if self.ids._alt_q22.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q22.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q22.md_bg_color = [2, 0, 0, 5]

    def alternative_q23(self):
        if self.ids._alt_q23.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q23.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q23.md_bg_color = [2, 0, 0, 5]

#3rd alternative question
    def alternative_q31(self):
        if self.ids._alt_q31.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q31.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q31.md_bg_color = [2, 0, 0, 5]

    def alternative_q32(self):
        if self.ids._alt_q32.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q32.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q32.md_bg_color = [2, 0, 0, 5]

    def alternative_q33(self):
        if self.ids._alt_q33.md_bg_color == [2, 0, 0, 5]:
            self.ids._alt_q33.md_bg_color = 255, 230, 0, 1
        else:
            self.ids._alt_q33.md_bg_color = [2, 0, 0, 5]



    def set_2score(self):
        self.ids._totalscore2.text = self.press_property
        self.ids.correct_2button1.md_bg_color = 0, 230, 0, 1
        self.ids.correct_2button2.md_bg_color = 0, 230, 0, 1
        self.ids.correct_2button3.md_bg_color = 0, 230, 0, 1


    freshcount = 0

    def refresh_all(self):
        self.press_property = str('0')
        self.ids._totalscore.text = self.press_property
        self.ids.correct_button1.md_bg_color = [2, 0, 0, 5]
        self.ids.correct_button2.md_bg_color = [2, 0, 0, 5]
        self.ids.correct_button3.md_bg_color = [2, 0, 0, 5]
        self.ids.correct_button4.md_bg_color = [2, 0, 0, 5]
        self.ids.correct_button5.md_bg_color = [2, 0, 0, 5]

    '''def change_color(self):
        if self.MDRaisedButton.md_bg_color == [2,0,0,5]:
            self.md_bg_color = 255, 230, 0, 1
        else:
            self.md_bg_color = 2,0,0,5'''



class Math2022(Screen):
    check = []
    counter = 0

    press_property = StringProperty('0')

    def checkbox_click(self, instance, value, number, topping, score):
        if value == True:
            Math2022.check.append(str(number) + topping)
            output = ''
            for x in Math2022.check:
                output = f'{output} {x}'
            print(str(1))
            self.counter += 1
            self.press_property = str(self.counter)

            self.ids.output_label.text = f'you selected: {output}'
        else:
            Math2022.check.remove(str(number) + topping)
            output = ''
            for x in Math2022.check:
                output = f'{output} {x}'
            self.ids.output_label.text = f'you selected: {output}'
            self.counter -= 1
            self.press_property = str(self.counter)

    def show_score(self):
        self.ids._score.text = self.press_property

    def fresh_all(self):
        self.ids._score.text = str(0)
        self.ids._1a.active = False
        self.ids._1b.active = False
        self.ids._1c.active = False
        self.ids._2a.active = False
        self.ids._2b.active = False
        self.ids._2c.active = False
        self.ids._3a.active = False
        self.ids._3b.active = False
        self.ids._3c.active = False






class Math2021(Screen):
    pass


class Math2020(Screen):
    pass


class Math2019(Screen):
    pass


class Math2018(Screen):
    pass


class Math2017(Screen):
    pass


class Math2016(Screen):
    pass


class Math2015(Screen):
    pass


class EnglishYear(Screen):
    pass


class English2023(Screen):
    pass


class English2022(Screen):
    pass


class English2021(Screen):
    pass


class English2020(Screen):
    pass


class English2019(Screen):
    pass


class English2018(Screen):
    pass


class English2017(Screen):
    pass


class English2016(Screen):
    pass


class English2015(Screen):
    pass


class PhysicsYear(Screen):
    pass


class Physics2023(Screen):
    pass


class Physics2022(Screen):
    pass


class Physics2021(Screen):
    pass


class Physics2020(Screen):
    pass


class Physics2019(Screen):
    pass


class Physics2018(Screen):
    pass


class Physics2017(Screen):
    pass


class Physics2016(Screen):
    pass


class Physics2015(Screen):
    pass


class ChemistryYear(Screen):
    pass


class Chemistry2023(Screen):
    pass


class Chemistry2022(Screen):
    pass


class Chemistry2021(Screen):
    pass


class Chemistry2020(Screen):
    pass


class Chemistry2019(Screen):
    pass


class Chemistry2018(Screen):
    pass


class Chemistry2017(Screen):
    pass


class Chemistry2016(Screen):
    pass


class Chemistry2015(Screen):
    pass


class By(Screen):
    pass


class B23(Screen):
    pass


class B22(Screen):
    pass


class B21(Screen):
    pass


class B20(Screen):
    pass


class B19(Screen):
    pass


class B18(Screen):
    pass


class B17(Screen):
    pass


class B16(Screen):
    pass


class B15(Screen):
    pass


class EconomicsYear(Screen):
    pass


class Ec23(Screen):
    pass


class Ec22(Screen):
    pass


class Ec21(Screen):
    pass


class Ec20(Screen):
    pass


class Ec19(Screen):
    pass


class Ec18(Screen):
    pass


class Ec17(Screen):
    pass


class Ec16(Screen):
    pass


class Ec15(Screen):
    pass


class CivicYear(Screen):
    pass


class MarketingYear(Screen):
    pass


class AccountingYear(Screen):
    pass


class LiteratureYear(Screen):
    pass


class FurtherMathYear(Screen):
    pass


class ChristianReligionStudiesYear(Screen):
    pass


class GeographyYear(Screen):
    pass


class CommerceYear(Screen):
    pass


# JAAAAAAAAAAAAAAAAAAAAAAMB#


class jMathematicsYear(Screen):
    pass


class jEnglishYear(Screen):
    pass


class jChemistryYear(Screen):
    pass


class jPhysicsYear(Screen):
    pass


class jBY(Screen):
    pass


class jEconomicsYear(Screen):
    pass


class jCivicYear(Screen):
    pass


class jMarketingYear(Screen):
    pass


class jAccountingYear(Screen):
    pass


class jLiteratureYear(Screen):
    pass


class jLiteratureYear(Screen):
    pass


class jFurtherMathYear(Screen):
    pass


class jChristianReligionStudiesYear(Screen):
    pass


class jGeographyYear(Screen):
    pass


class jCommerceYear(Screen):
    pass


# NEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEECCCCCCCCCCCOOOOOOOOOOOO
class NMathematicsYear(Screen):
    pass


class NEnglishYear(Screen):
    pass


class NPhysicsYear(Screen):
    pass


class NChemistryYear(Screen):
    pass


class NBY(Screen):
    pass


class NEconomicsYear(Screen):
    pass


class NCivicYear(Screen):
    pass


class NMarketingYear(Screen):
    pass


class NAccountingYear(Screen):
    pass


class NLiteratureYear(Screen):
    pass


class NFurtherMathYear(Screen):
    pass


class NChristianReligionStudiesYear(Screen):
    pass


class NGeographyYear(Screen):
    pass


class NCommerceYear(Screen):
    pass


class NecoSubject(Screen):
    pass


class Economicss23:
    pass


class Economics15:
    pass


class Economics16:
    pass


class Economics17:
    pass


class Economics18:
    pass


class Economics19:
    pass


class Economics20:
    pass


class Economicss22:
    pass


class Economics21:
    pass


class CivicYear23(Screen):
    pass


class CivicYear22(Screen):
    pass


class CivicYear21(Screen):
    pass


class CivicYear20(Screen):
    pass


class CivicYear19(Screen):
    pass


class CivicYear18(Screen):
    pass


class CivicYear17(Screen):
    pass


class CivicYear16(Screen):
    pass


class CivicYear15(Screen):
    pass


class MarketingYear2023(Screen):
    pass


class MarketingYear2022(Screen):
    pass


class MarketingYear2021(Screen):
    pass


class MarketingYear2020(Screen):
    pass


class MarketingYear2019(Screen):
    pass


class MarketingYear2018(Screen):
    pass


class MarketingYear2017(Screen):
    pass


class MarketingYear2016(Screen):
    pass


class MarketingYear2015(Screen):
    pass


class AccountingYear2023(Screen):
    pass


class AccountingYear2022(Screen):
    pass


class AccountingYear2021(Screen):
    pass


class AccountingYear2020(Screen):
    pass


class AccountingYear2019(Screen):
    pass


class AccountingYear2018(Screen):
    pass


class AccountingYear2017(Screen):
    pass


class AccountingYear2016(Screen):
    pass


class AccountingYear2015(Screen):
    pass


# Creating main app class
class LiteratureYear2023(Screen):
    pass


class LiteratureYear2022(Screen):
    pass


class LiteratureYear2021(Screen):
    pass


class LiteratureYear2020(Screen):
    pass


class LiteratureYear2019(Screen):
    pass


class LiteratureYear2018(Screen):
    pass


class LiteratureYear2017(Screen):
    pass


class LiteratureYear2016(Screen):
    pass


class LiteratureYear2015(Screen):
    pass


class FurtherMathYear2023(Screen):
    pass


class FurtherMathYear2022(Screen):
    pass


class FurtherMathYear2021(Screen):
    pass


class FurtherMathYear2020(Screen):
    pass


class FurtherMathYear2019(Screen):
    pass


class FurtherMathYear2018(Screen):
    pass


class FurtherMathYear2017(Screen):
    pass


class FurtherMathYear2016(Screen):
    pass


class FurtherMathYear2015(Screen):
    pass


class ChristianReligionStudies2023(Screen):
    pass


class ChristianReligionStudies2022(Screen):
    pass


class ChristianReligionStudies2021(Screen):
    pass


class ChristianReligionStudies2020(Screen):
    pass


class ChristianReligionStudies2019(Screen):
    pass


class ChristianReligionStudies2018(Screen):
    pass


class ChristianReligionStudies2017(Screen):
    pass


class ChristianReligionStudies2016(Screen):
    pass


class ChristianReligionStudies2015(Screen):
    pass


class GeographyYear2023(Screen):
    pass


class GeographyYear2022(Screen):
    pass


class GeographyYear2021(Screen):
    pass


class GeographyYear2020(Screen):
    pass


class GeographyYear2019(Screen):
    pass


class GeographyYear2018(Screen):
    pass


class GeographyYear2017(Screen):
    pass


class GeographyYear2016(Screen):
    pass


class GeographyYear2015(Screen):
    pass


class CommerceYear2023(Screen):
    pass


class CommerceYear2023(Screen):
    pass


class CommerceYear2022(Screen):
    pass


class CommerceYear2021(Screen):
    pass


class CommerceYear2020(Screen):
    pass


class CommerceYear2019(Screen):
    pass


class CommerceYear2018(Screen):
    pass


class CommerceYear2017(Screen):
    pass


class CommerceYear2016(Screen):
    pass


class CommerceYear2015(Screen):
    pass


class JMath2023(Screen):
    pass


class JMath2022(Screen):
    pass


class JMath2021(Screen):
    pass


class JMath2020(Screen):
    pass


class JMath2019(Screen):
    pass


class JMath2018(Screen):
    pass


class JMath2019(Screen):
    pass


class JMath2018(Screen):
    pass


class JMath2017(Screen):
    pass


class JMath2016(Screen):
    pass


class JMath2015(Screen):
    pass


class JEnglish2023(Screen):
    pass


class JEnglish2022(Screen):
    pass


class JEnglish2021(Screen):
    pass


class JEnglish2020(Screen):
    pass


class JEnglish2019(Screen):
    pass


class JEnglish2018(Screen):
    pass


class JEnglish2017(Screen):
    pass


class JEnglish2016(Screen):
    pass


class JEnglish2015(Screen):
    pass


class JPhysics2023(Screen):
    pass


class JPhysics2022(Screen):
    pass


class JPhysics2021(Screen):
    pass


class JPhysics2020(Screen):
    pass


class JPhysics2019(Screen):
    pass


class JPhysics2018(Screen):
    pass


class JPhysics2017(Screen):
    pass


class JPhysics2016(Screen):
    pass


class JPhysics2015(Screen):
    pass


class JChemistry2023(Screen):
    pass


class JChemistry2022(Screen):
    pass


class JChemistry2021(Screen):
    pass


class JChemistry2020(Screen):
    pass


class JChemistry2019(Screen):
    pass


class JChemistry2018(Screen):
    pass


class JChemistry2017(Screen):
    pass


class JChemistry2016(Screen):
    pass


class JChemistry2015(Screen):
    pass


class JB23(Screen):
    pass


class JB22(Screen):
    pass


class JB21(Screen):
    pass


class JB20(Screen):
    pass


class JB19(Screen):
    pass


class JB18(Screen):
    pass


class JB17(Screen):
    pass


class JB16(Screen):
    pass


class JB15(Screen):
    pass


class JEc23(Screen):
    pass


class JEc22(Screen):
    pass


class JEc21(Screen):
    pass


class JEc20(Screen):
    pass


class JEc19(Screen):
    pass


class JEc18(Screen):
    pass


class JEc17(Screen):
    pass


class JEc16(Screen):
    pass


class JEc15(Screen):
    pass


class JCivicYear23(Screen):
    pass


class JCivicYear22(Screen):
    pass


class JCivicYear21(Screen):
    pass


class JCivicYear20(Screen):
    pass


class JCivicYear19(Screen):
    pass


class JCivicYear18(Screen):
    pass


class JCivicYear17(Screen):
    pass


class JCivicYear16(Screen):
    pass


class JCivicYear15(Screen):
    pass


class JMarketingYear2023(Screen):
    pass


class JMarketingYear2022(Screen):
    pass


class JMarketingYear2021(Screen):
    pass


class JMarketingYear2020(Screen):
    pass


class JMarketingYear2019(Screen):
    pass


class JMarketingYear2018(Screen):
    pass


class JMarketingYear2017(Screen):
    pass


class JMarketingYear2016(Screen):
    pass


class JMarketingYear2015(Screen):
    pass


class JAccountingYear2023(Screen):
    pass


class JAccountingYear2022(Screen):
    pass


class JAccountingYear2021(Screen):
    pass


class JAccountingYear2020(Screen):
    pass


class JAccountingYear2019(Screen):
    pass


class JAccountingYear2018(Screen):
    pass


class JAccountingYear2017(Screen):
    pass


class JAccountingYear2016(Screen):
    pass


class JAccountingYear2015(Screen):
    pass


class JLiteratureYear2023(Screen):
    pass


class JLiteratureYear2022(Screen):
    pass


class JLiteratureYear2021(Screen):
    pass


class JLiteratureYear2020(Screen):
    pass


class JLiteratureYear2019(Screen):
    pass


class JLiteratureYear2018(Screen):
    pass


class JLiteratureYear2017(Screen):
    pass


class JLiteratureYear2016(Screen):
    pass


class JLiteratureYear2015(Screen):
    pass


class JFurtherMathYear2023(Screen):
    pass


class JFurtherMathYear2022(Screen):
    pass


class JFurtherMathYear2021(Screen):
    pass


class JFurtherMathYear2020(Screen):
    pass


class JFurtherMathYear2019(Screen):
    pass


class JFurtherMathYear2018(Screen):
    pass


class JFurtherMathYear2017(Screen):
    pass


class JFurtherMathYear2016(Screen):
    pass


class JFurtherMathYear2015(Screen):
    pass


class JChristianReligionStudies2023(Screen):
    pass


class JChristianReligionStudies2022(Screen):
    pass


class JChristianReligionStudies2021(Screen):
    pass


class JChristianReligionStudies2020(Screen):
    pass


class JChristianReligionStudies2019(Screen):
    pass


class JChristianReligionStudies2018(Screen):
    pass


class JChristianReligionStudies2017(Screen):
    pass


class JChristianReligionStudies2016(Screen):
    pass


class JChristianReligionStudies2015(Screen):
    pass


class JGeographyYear2023(Screen):
    pass


class JGeographyYear2022(Screen):
    pass


class JGeographyYear2021(Screen):
    pass


class JGeographyYear2020(Screen):
    pass


class JGeographyYear2019(Screen):
    pass


class JGeographyYear2018(Screen):
    pass


class JGeographyYear2017(Screen):
    pass


class JGeographyYear2016(Screen):
    pass


class JGeographyYear2015(Screen):
    pass


class JCommerceYear2023(Screen):
    pass


class JCommerceYear2023(Screen):
    pass


class JCommerceYear2022(Screen):
    pass


class JCommerceYear2021(Screen):
    pass


class JCommerceYear2020(Screen):
    pass


class JCommerceYear2019(Screen):
    pass


class JCommerceYear2018(Screen):
    pass


class JCommerceYear2017(Screen):
    pass


class JCommerceYear2016(Screen):
    pass


class JCommerceYear2015(Screen):
    pass

class CircularAvatarImage(MDCard):
    avatar = StringProperty()
    name = StringProperty()


class StoryCreator(MDCard):
    avatar = StringProperty()


class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    comments = StringProperty()
    posted_ago = StringProperty()


class MainApp(MDApp):
    global screen_manager
    screen_manager = ScreenManager()

    def refresh_all(self):
        self.theme_cls.primary_palette = 'Blue'

    def build(self):
        # Setting window size & setting deault theme
        Window.size = [305, 590]
        self.theme_cls.theme_style = "Light"

        self.theme_cls_accent_hue = '400'
        self.title = 'Exampal'



        # files for all the screen#

        # All hompage and waec tab files
        Builder.load_file('homepage.kv')
        Builder.load_file('profilepage.kv')
        Builder.load_file('searchpage.kv')
        Builder.load_file('infopage.kv')
        Builder.load_file('settingpage.kv')
        Builder.load_file('waecmath.kv')
        Builder.load_file('waecpage.kv')
        Builder.load_file('nsubject.kv')
        Builder.load_file('waecmath.kv')
        #Builder.load_file('screenmanager.kv')
        Builder.load_file('Math2023.kv')
        Builder.load_file('Math2022.kv')
        Builder.load_file('Math2021.kv')
        Builder.load_file('Math2020.kv')
        Builder.load_file('Math2019.kv')
        Builder.load_file('Math2018.kv')
        Builder.load_file('Math2017.kv')
        Builder.load_file('Math2016.kv')
        Builder.load_file('Math2015.kv')

        Builder.load_file("waec_english.kv")
        Builder.load_file('English2023.kv')
        Builder.load_file('English2022.kv')
        Builder.load_file('English2021.kv')
        Builder.load_file('English2020.kv')
        Builder.load_file('English2019.kv')
        Builder.load_file('English2018.kv')
        Builder.load_file('English2017.kv')
        Builder.load_file('English2016.kv')
        #Builder.load_file('English2015.kv')

        Builder.load_file("waec_physics.kv")
        Builder.load_file("Physics2023.kv")
        Builder.load_file("Physics2022.kv")
        Builder.load_file("Physics2021.kv")
        Builder.load_file("Physics2020.kv")
        Builder.load_file("Physics2019.kv")
        Builder.load_file("Physics2018.kv")
        Builder.load_file("Physics2017.kv")
        Builder.load_file("Physics2016.kv")
        Builder.load_file("Physics2015.kv")

        Builder.load_file("waec_chemistry.kv")
        Builder.load_file("Chemistry2023.kv")
        Builder.load_file("Chemistry2022.kv")
        Builder.load_file("Chemistry2021.kv")
        Builder.load_file("Chemistry2020.kv")
        Builder.load_file("Chemistry2019.kv")
        Builder.load_file("Chemistry2018.kv")
        Builder.load_file("Chemistry2017.kv")
        Builder.load_file("Chemistry2016.kv")
        Builder.load_file("Chemistry2015.kv")

        Builder.load_file("waec_biology.kv")
        Builder.load_file("biology2023.kv")
        Builder.load_file("biology2022.kv")
        Builder.load_file("biology2021.kv")
        Builder.load_file("biology2020.kv")
        Builder.load_file("biology2019.kv")
        Builder.load_file("biology2018.kv")
        Builder.load_file("biology2017.kv")
        Builder.load_file("biology2016.kv")
        Builder.load_file("biology2015.kv")

        Builder.load_file("waec_economics.kv")
        Builder.load_file("waec_economics23.kv")
        Builder.load_file("waec_economics22.kv")
        Builder.load_file("waec_economics21.kv")
        Builder.load_file("waec_economics20.kv")
        Builder.load_file("waec_economics19.kv")
        Builder.load_file("waec_economics18.kv")
        Builder.load_file("waec_economics17.kv")
        Builder.load_file("waec_economics16.kv")
        Builder.load_file("waec_economics15.kv")

        Builder.load_file("waec_civic.kv")
        Builder.load_file("waec_civic23.kv")
        Builder.load_file("waec_civic22.kv")
        Builder.load_file("waec_civic21.kv")
        Builder.load_file("waec_civic20.kv")
        Builder.load_file("waec_civic19.kv")
        Builder.load_file("waec_civic18.kv")
        Builder.load_file("waec_civic17.kv")
        Builder.load_file("waec_civic16.kv")
        Builder.load_file("waec_civic15.kv")

        Builder.load_file("waec_account.kv")
        Builder.load_file("waec_account23.kv")
        Builder.load_file("waec_account22.kv")
        Builder.load_file("waec_account21.kv")
        Builder.load_file("waec_account20.kv")
        Builder.load_file("waec_account19.kv")
        Builder.load_file("waec_account18.kv")
        Builder.load_file("waec_account17.kv")
        Builder.load_file("waec_account16.kv")
        Builder.load_file("waec_account15.kv")

        Builder.load_file("waec_marketing.kv")
        Builder.load_file("waec_marketing23.kv")
        Builder.load_file("waec_marketing22.kv")
        Builder.load_file("waec_marketing21.kv")
        Builder.load_file("waec_marketing20.kv")
        Builder.load_file("waec_marketing19.kv")
        Builder.load_file("waec_marketing18.kv")
        Builder.load_file("waec_marketing17.kv")
        Builder.load_file("waec_marketing16.kv")
        Builder.load_file("waec_marketing15.kv")

        Builder.load_file("waec_furthermaths.kv")
        Builder.load_file("waec_furthermaths23.kv")
        Builder.load_file("waec_furthermaths22.kv")
        Builder.load_file("waec_furthermaths21.kv")
        Builder.load_file("waec_furthermaths20.kv")
        Builder.load_file("waec_furthermaths19.kv")
        Builder.load_file("waec_furthermaths18.kv")
        Builder.load_file("waec_furthermaths17.kv")
        Builder.load_file("waec_furthermaths16.kv")
        Builder.load_file("waec_furthermaths15.kv")

        Builder.load_file("waec_literature.kv")
        Builder.load_file("waec_literature23.kv")
        Builder.load_file("waec_literature22.kv")
        Builder.load_file("waec_literature21.kv")
        Builder.load_file("waec_literature20.kv")
        Builder.load_file("waec_literature19.kv")
        Builder.load_file("waec_literature18.kv")
        Builder.load_file("waec_literature17.kv")
        Builder.load_file("waec_literature16.kv")
        Builder.load_file("waec_literature15.kv")

        Builder.load_file("waec_crs.kv")
        Builder.load_file("waec_crs23.kv")
        Builder.load_file("waec_crs22.kv")
        Builder.load_file("waec_crs21.kv")
        Builder.load_file("waec_crs20.kv")
        Builder.load_file("waec_crs19.kv")
        Builder.load_file("waec_crs18.kv")
        Builder.load_file("waec_crs17.kv")
        Builder.load_file("waec_crs16.kv")
        Builder.load_file("waec_crs15.kv")

        Builder.load_file("waec_geography.kv")
        Builder.load_file("waec_geography23.kv")
        Builder.load_file("waec_geography22.kv")
        Builder.load_file("waec_geography21.kv")
        Builder.load_file("waec_geography20.kv")
        Builder.load_file("waec_geography19.kv")
        Builder.load_file("waec_geography18.kv")
        Builder.load_file("waec_geography17.kv")
        Builder.load_file("waec_geography16.kv")
        Builder.load_file("waec_geography15.kv")

        Builder.load_file("waec_commerce.kv")
        Builder.load_file("waec_commerce23.kv")
        Builder.load_file("waec_commerce22.kv")
        Builder.load_file("waec_commerce21.kv")
        Builder.load_file("waec_commerce20.kv")
        Builder.load_file("waec_commerce19.kv")
        Builder.load_file("waec_commerce18.kv")
        Builder.load_file("waec_commerce17.kv")
        Builder.load_file("waec_commerce16.kv")
        Builder.load_file("waec_commerce15.kv")

        # JAMB tab fileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeees

        Builder.load_file("jambsubject.kv")
        Builder.load_file('jmath.kv')
        Builder.load_file('jMath2023.kv')
        Builder.load_file('jMath2022.kv')
        Builder.load_file('jMath2021.kv')
        Builder.load_file('jMath2020.kv')
        Builder.load_file('jMath2019.kv')
        Builder.load_file('jMath2018.kv')
        Builder.load_file('jMath2017.kv')
        Builder.load_file('jMath2016.kv')
        Builder.load_file('jMath2015.kv')

        Builder.load_file("j_english.kv")
        Builder.load_file('JEnglish2023.kv')
        Builder.load_file('JEnglish2022.kv')
        Builder.load_file('JEnglish2021.kv')
        Builder.load_file('JEnglish2020.kv')
        Builder.load_file('JEnglish2019.kv')
        Builder.load_file('JEnglish2018.kv')
        Builder.load_file('JEnglish2017.kv')
        Builder.load_file('JEnglish2016.kv')
        Builder.load_file('JEnglish2015.kv')

        Builder.load_file("j_physics.kv")
        Builder.load_file("jPhysics2023.kv")
        Builder.load_file("jPhysics2022.kv")
        Builder.load_file("jPhysics2021.kv")
        Builder.load_file("jPhysics2020.kv")
        Builder.load_file("jPhysics2019.kv")
        Builder.load_file("jPhysics2018.kv")
        Builder.load_file("jPhysics2017.kv")
        Builder.load_file("jPhysics2016.kv")
        Builder.load_file("jPhysics2015.kv")

        Builder.load_file("j_chemistry.kv")
        Builder.load_file("jChemistry2023.kv")
        Builder.load_file("jChemistry2022.kv")
        Builder.load_file("jChemistry2021.kv")
        Builder.load_file("jChemistry2020.kv")
        Builder.load_file("jChemistry2019.kv")
        Builder.load_file("jChemistry2018.kv")
        Builder.load_file("jChemistry2017.kv")
        Builder.load_file("jChemistry2016.kv")
        Builder.load_file("jChemistry2015.kv")

        Builder.load_file("j_biology.kv")
        Builder.load_file("Jbiology2023.kv")
        Builder.load_file("jbiology2022.kv")
        Builder.load_file("jbiology2021.kv")
        Builder.load_file("jbiology2020.kv")
        Builder.load_file("jbiology2019.kv")
        Builder.load_file("jbiology2018.kv")
        Builder.load_file("jbiology2017.kv")
        Builder.load_file("jbiology2016.kv")
        Builder.load_file("jbiology2015.kv")

        Builder.load_file("j_economics.kv")
        Builder.load_file("j_economics23.kv")
        Builder.load_file("j_economics22.kv")
        Builder.load_file("j_economics21.kv")
        Builder.load_file("j_economics20.kv")
        Builder.load_file("j_economics19.kv")
        Builder.load_file("j_economics18.kv")
        Builder.load_file("j_economics17.kv")
        Builder.load_file("j_economics16.kv")
        Builder.load_file("j_economics15.kv")

        Builder.load_file("j_civic.kv")
        Builder.load_file("j_civic23.kv")
        Builder.load_file("j_civic22.kv")
        Builder.load_file("j_civic21.kv")
        Builder.load_file("j_civic20.kv")
        Builder.load_file("j_civic19.kv")
        Builder.load_file("j_civic18.kv")
        Builder.load_file("j_civic17.kv")
        Builder.load_file("j_civic16.kv")
        Builder.load_file("j_civic15.kv")

        Builder.load_file("j_account.kv")
        Builder.load_file("j_account23.kv")
        Builder.load_file("j_account22.kv")
        Builder.load_file("j_account21.kv")
        Builder.load_file("j_account20.kv")
        Builder.load_file("j_account19.kv")
        Builder.load_file("j_account18.kv")
        Builder.load_file("j_account17.kv")
        Builder.load_file("j_account16.kv")
        Builder.load_file("j_account15.kv")

        Builder.load_file("j_marketing.kv")
        Builder.load_file("j_marketing23.kv")
        Builder.load_file("j_marketing22.kv")
        Builder.load_file("j_marketing21.kv")
        Builder.load_file("j_marketing20.kv")
        Builder.load_file("j_marketing19.kv")
        Builder.load_file("j_marketing18.kv")
        Builder.load_file("j_marketing17.kv")
        Builder.load_file("j_marketing16.kv")
        Builder.load_file("j_marketing15.kv")

        Builder.load_file("j_furthermaths.kv")
        Builder.load_file("j_furthermaths23.kv")
        Builder.load_file("j_furthermaths22.kv")
        Builder.load_file("j_furthermaths21.kv")
        Builder.load_file("j_furthermaths20.kv")
        Builder.load_file("j_furthermaths19.kv")
        Builder.load_file("j_furthermaths18.kv")
        Builder.load_file("j_furthermaths17.kv")
        Builder.load_file("j_furthermaths16.kv")
        Builder.load_file("j_furthermaths15.kv")

        Builder.load_file("j_literature.kv")
        Builder.load_file("j_literature23.kv")
        Builder.load_file("j_literature22.kv")
        Builder.load_file("j_literature21.kv")
        Builder.load_file("j_literature20.kv")
        Builder.load_file("j_literature19.kv")
        Builder.load_file("j_literature18.kv")
        Builder.load_file("j_literature17.kv")
        Builder.load_file("j_literature16.kv")
        Builder.load_file("j_literature15.kv")

        Builder.load_file("j_crs.kv")
        Builder.load_file("j_crs23.kv")
        Builder.load_file("j_crs22.kv")
        Builder.load_file("j_crs21.kv")
        Builder.load_file("j_crs20.kv")
        Builder.load_file("j_crs19.kv")
        Builder.load_file("j_crs18.kv")
        Builder.load_file("j_crs17.kv")
        Builder.load_file("j_crs16.kv")
        Builder.load_file("j_crs15.kv")

        Builder.load_file("j_geography.kv")
        Builder.load_file("j_geography23.kv")
        Builder.load_file("j_geography22.kv")
        Builder.load_file("j_geography21.kv")
        Builder.load_file("j_geography20.kv")
        Builder.load_file("j_geography19.kv")
        Builder.load_file("j_geography18.kv")
        Builder.load_file("j_geography17.kv")
        Builder.load_file("j_geography16.kv")
        Builder.load_file("j_geography15.kv")

        Builder.load_file("j_commerce.kv")
        Builder.load_file("j_commerce23.kv")
        Builder.load_file("j_commerce22.kv")
        Builder.load_file("j_commerce21.kv")
        Builder.load_file("j_commerce20.kv")
        Builder.load_file("j_commerce19.kv")
        Builder.load_file("j_commerce18.kv")
        Builder.load_file("j_commerce17.kv")
        Builder.load_file("j_commerce16.kv")
        Builder.load_file("j_commerce15.kv")

        # NECO tab files
        Builder.load_file("n_subject.kv")
        Builder.load_file('n_math.kv')
        Builder.load_file("n_english.kv")
        Builder.load_file("n_physics.kv")
        Builder.load_file("n_chemistry.kv")
        Builder.load_file("n_biology.kv")
        Builder.load_file("n_economics.kv")
        Builder.load_file("n_civic.kv")
        Builder.load_file("n_account.kv")
        Builder.load_file("n_marketing.kv")
        Builder.load_file("n_furthermaths.kv")
        Builder.load_file("n_literature.kv")
        Builder.load_file("n_crs.kv")
        Builder.load_file("n_geography.kv")
        Builder.load_file("n_commerce.kv")
        Builder.load_file('variable.py')

        # All the screens for the app

        # All home screen and wnd waec subject and year screen
        #sm = ScreenManager()
        screen_manager.add_widget(Builder.load_file("checkmd_splash.kv"))
        screen_manager.add_widget(HomePage(name='home'))
        screen_manager.add_widget(ProfilePage(name='profile'))
        screen_manager.add_widget(SearchPage(name='search'))
        screen_manager.add_widget(InfoPage(name='info'))
        screen_manager.add_widget(SettingsPage(name='settings'))
        screen_manager.add_widget(WaecSubject(name='waecsubject'))
        screen_manager.add_widget(JambSubject(name='jambsubject'))

        screen_manager.add_widget(MathematicsYear(name='waec math year'))
        screen_manager.add_widget(Math2023(name='math23'))
        screen_manager.add_widget(Math2022(name='math22'))
        screen_manager.add_widget(Math2021(name='math21'))
        '''screen_manager.add_widget(Math2020(name='math20'))
        screen_manager.add_widget(Math2019(name='math19'))
        screen_manager.add_widget(Math2018(name='math18'))
        screen_manager.add_widget(Math2017(name='math17'))
        screen_manager.add_widget(Math2016(name='math16'))
        screen_manager.add_widget(Math2015(name='math15'))

        sm.add_widget(EnglishYear(name='waec english year'))
        sm.add_widget(English2023(name='english23'))
        sm.add_widget(English2022(name='english22'))
        sm.add_widget(English2021(name='english21'))
        sm.add_widget(English2020(name='english20'))
        sm.add_widget(English2019(name='english19'))
        sm.add_widget(English2018(name='english18'))
        sm.add_widget(English2017(name='english17'))
        sm.add_widget(English2016(name='english16'))
        sm.add_widget(English2015(name='english15'))

        sm.add_widget(PhysicsYear(name='waec physics year'))
        sm.add_widget(Physics2023(name='physics23'))
        sm.add_widget(Physics2022(name='physics22'))
        sm.add_widget(Physics2021(name='physics21'))
        sm.add_widget(Physics2020(name='physics20'))
        sm.add_widget(Physics2019(name='physics19'))
        sm.add_widget(Physics2018(name='physics18'))
        sm.add_widget(Physics2017(name='physics17'))
        sm.add_widget(Physics2016(name='physics16'))
        sm.add_widget(Physics2015(name='physics15'))

        sm.add_widget(ChemistryYear(name='waec chemistry year'))
        sm.add_widget(Chemistry2023(name='chemistry23'))
        sm.add_widget(Chemistry2022(name='chemistry22'))
        sm.add_widget(Chemistry2021(name='chemistry21'))
        sm.add_widget(Chemistry2020(name='chemistry20'))
        sm.add_widget(Chemistry2019(name='chemistry19'))
        sm.add_widget(Chemistry2018(name='chemistry18'))
        sm.add_widget(Chemistry2017(name='chemistry17'))
        sm.add_widget(Chemistry2016(name='chemistry16'))
        sm.add_widget(Chemistry2015(name='chemistry15'))

        sm.add_widget(By(name='by'))
        sm.add_widget(B23(name="b23"))
        sm.add_widget(B22(name="b22"))
        sm.add_widget(B21(name="b21"))
        sm.add_widget(B20(name="b20"))
        sm.add_widget(B19(name="b19"))
        sm.add_widget(B23(name="b18"))
        sm.add_widget(B22(name="b17"))
        sm.add_widget(B21(name="b16"))
        sm.add_widget(B20(name="b15"))

        sm.add_widget(EconomicsYear(name='waec economics year'))
        sm.add_widget(Ec23(name="ec23"))
        sm.add_widget(Ec22(name="ec22"))
        sm.add_widget(Ec21(name="ec21"))
        sm.add_widget(Ec20(name="ec20"))
        sm.add_widget(Ec19(name="ec19"))
        sm.add_widget(Ec18(name="ec18"))
        sm.add_widget(Ec17(name="ec17"))
        sm.add_widget(Ec16(name="ec16"))
        sm.add_widget(Ec15(name="ec15"))

        sm.add_widget(CivicYear(name='waec civic year'))
        sm.add_widget(CivicYear23(name="civic23"))
        sm.add_widget(CivicYear22(name="civic22"))
        sm.add_widget(CivicYear21(name="civic21"))
        sm.add_widget(CivicYear20(name="civic20"))
        sm.add_widget(CivicYear19(name="civic19"))
        sm.add_widget(CivicYear18(name="civic18"))
        sm.add_widget(CivicYear17(name="civic17"))
        sm.add_widget(CivicYear16(name="civic16"))
        sm.add_widget(CivicYear15(name="civic15"))

        sm.add_widget(MarketingYear(name='waec market year'))
        sm.add_widget(MarketingYear2023(name='waec market 23'))
        sm.add_widget(MarketingYear2022(name='waec market 22'))
        sm.add_widget(MarketingYear2021(name='waec market 21'))
        sm.add_widget(MarketingYear2020(name='waec market 20'))
        sm.add_widget(MarketingYear2019(name='waec market 19'))
        sm.add_widget(MarketingYear2018(name='waec market 18'))
        sm.add_widget(MarketingYear2017(name='waec market 17'))
        sm.add_widget(MarketingYear2016(name='waec market 16'))
        sm.add_widget(MarketingYear2015(name='waec market 15'))

        sm.add_widget(AccountingYear(name='waec accounts year'))
        sm.add_widget(AccountingYear2023(name='waec accounts 23'))
        sm.add_widget(AccountingYear2022(name='waec accounts 22'))
        sm.add_widget(AccountingYear2021(name='waec accounts 21'))
        sm.add_widget(AccountingYear2020(name='waec accounts 20'))
        sm.add_widget(AccountingYear2019(name='waec accounts 19'))
        sm.add_widget(AccountingYear2018(name='waec accounts 18'))
        sm.add_widget(AccountingYear2017(name='waec accounts 17'))
        sm.add_widget(AccountingYear2016(name='waec accounts 16'))
        sm.add_widget(AccountingYear2016(name='waec accounts 15'))

        sm.add_widget(LiteratureYear(name='waec literature year'))
        sm.add_widget(LiteratureYear2023(name='waec literature 23'))
        sm.add_widget(LiteratureYear2022(name='waec literature 22'))
        sm.add_widget(LiteratureYear2021(name='waec literature 21'))
        sm.add_widget(LiteratureYear2020(name='waec literature 20'))
        sm.add_widget(LiteratureYear2019(name='waec literature 19'))
        sm.add_widget(LiteratureYear2018(name='waec literature 18'))
        sm.add_widget(LiteratureYear2017(name='waec literature 17'))
        sm.add_widget(LiteratureYear2016(name='waec literature 16'))
        sm.add_widget(LiteratureYear2015(name='waec literature 15'))

        sm.add_widget(FurtherMathYear(name='waec further maths year'))
        sm.add_widget(FurtherMathYear2023(name='waec further maths 23'))
        sm.add_widget(FurtherMathYear2022(name='waec further maths 22'))
        sm.add_widget(FurtherMathYear2021(name='waec further maths 21'))
        sm.add_widget(FurtherMathYear2020(name='waec further maths 20'))
        sm.add_widget(FurtherMathYear2019(name='waec further maths 19'))
        sm.add_widget(FurtherMathYear2018(name='waec further maths 18'))
        sm.add_widget(FurtherMathYear2017(name='waec further maths 17'))
        sm.add_widget(FurtherMathYear2016(name='waec further maths 16'))
        sm.add_widget(FurtherMathYear2015(name='waec further maths 15'))

        sm.add_widget(ChristianReligionStudiesYear(name='waec crs year'))
        sm.add_widget(ChristianReligionStudies2023(name='waec crs 23'))
        sm.add_widget(ChristianReligionStudies2022(name='waec crs 22'))
        sm.add_widget(ChristianReligionStudies2021(name='waec crs 21'))
        sm.add_widget(ChristianReligionStudies2020(name='waec crs 20'))
        sm.add_widget(ChristianReligionStudies2019(name='waec crs 19'))
        sm.add_widget(ChristianReligionStudies2018(name='waec crs 18'))
        sm.add_widget(ChristianReligionStudies2017(name='waec crs 17'))
        sm.add_widget(ChristianReligionStudies2016(name='waec crs 16'))
        sm.add_widget(ChristianReligionStudies2015(name='waec crs 15'))

        sm.add_widget(GeographyYear(name='waec geography year'))
        sm.add_widget(GeographyYear2023(name='waec geography 23'))
        sm.add_widget(GeographyYear2022(name='waec geography 22'))
        sm.add_widget(GeographyYear2021(name='waec geography 21'))
        sm.add_widget(GeographyYear2020(name='waec geography 20'))
        sm.add_widget(GeographyYear2019(name='waec geography 19'))
        sm.add_widget(GeographyYear2018(name='waec geography 18'))
        sm.add_widget(GeographyYear2017(name='waec geography 17'))
        sm.add_widget(GeographyYear2016(name='waec geography 16'))
        sm.add_widget(GeographyYear2015(name='waec geography 15'))

        sm.add_widget(CommerceYear(name='waec commerce year'))
        sm.add_widget(CommerceYear2023(name='waec commerce 23'))
        sm.add_widget(CommerceYear2022(name='waec commerce 22'))
        sm.add_widget(CommerceYear2021(name='waec commerce 21'))
        sm.add_widget(CommerceYear2020(name='waec commerce 20'))
        sm.add_widget(CommerceYear2019(name='waec commerce 19'))
        sm.add_widget(CommerceYear2018(name='waec commerce 18'))
        sm.add_widget(CommerceYear2017(name='waec commerce 17'))
        sm.add_widget(CommerceYear2016(name='waec commerce 16'))
        sm.add_widget(CommerceYear2015(name='waec commerce 15'))

        # Setting JAMB subjects and year screen
        sm.add_widget(jMathematicsYear(name='j math year'))
        sm.add_widget(JMath2023(name='jmath23'))
        sm.add_widget(JMath2022(name='jmath22'))
        sm.add_widget(JMath2021(name='jmath21'))
        sm.add_widget(JMath2020(name='jmath20'))
        sm.add_widget(JMath2019(name='jmath19'))
        sm.add_widget(JMath2018(name='jmath18'))
        sm.add_widget(JMath2017(name='jmath17'))
        sm.add_widget(JMath2016(name='jmath16'))
        sm.add_widget(JMath2015(name='jmath15'))

        sm.add_widget(jEnglishYear(name='j english year'))
        sm.add_widget(JEnglish2023(name='jenglish23'))
        sm.add_widget(JEnglish2022(name='jenglish22'))
        sm.add_widget(JEnglish2021(name='jenglish21'))
        sm.add_widget(JEnglish2020(name='jenglish20'))
        sm.add_widget(JEnglish2019(name='jenglish19'))
        sm.add_widget(JEnglish2018(name='jenglish18'))
        sm.add_widget(JEnglish2017(name='jenglish17'))
        sm.add_widget(JEnglish2016(name='jenglish16'))
        sm.add_widget(JEnglish2015(name='jenglish15'))

        sm.add_widget(jPhysicsYear(name='j physics year'))
        sm.add_widget(JPhysics2023(name='jphysics23'))
        sm.add_widget(JPhysics2022(name='jphysics22'))
        sm.add_widget(JPhysics2021(name='jphysics21'))
        sm.add_widget(JPhysics2020(name='jphysics20'))
        sm.add_widget(JPhysics2019(name='jphysics19'))
        sm.add_widget(JPhysics2018(name='jphysics18'))
        sm.add_widget(JPhysics2017(name='jphysics17'))
        sm.add_widget(JPhysics2016(name='jphysics16'))
        sm.add_widget(JPhysics2015(name='jphysics15'))

        sm.add_widget(jChemistryYear(name='j chemistry year'))
        sm.add_widget(JChemistry2023(name='jchemistry23'))
        sm.add_widget(JChemistry2022(name='jchemistry22'))
        sm.add_widget(JChemistry2021(name='jchemistry21'))
        sm.add_widget(JChemistry2020(name='jchemistry20'))
        sm.add_widget(JChemistry2019(name='jchemistry19'))
        sm.add_widget(JChemistry2018(name='jchemistry18'))
        sm.add_widget(JChemistry2017(name='jchemistry17'))
        sm.add_widget(JChemistry2016(name='jchemistry16'))
        sm.add_widget(JChemistry2015(name='jchemistry15'))

        sm.add_widget(jBY(name='jby'))
        sm.add_widget(JB23(name="jb23"))
        sm.add_widget(JB22(name="jb22"))
        sm.add_widget(JB21(name="jb21"))
        sm.add_widget(JB20(name="jb20"))
        sm.add_widget(JB19(name="jb19"))
        sm.add_widget(JB23(name="jb18"))
        sm.add_widget(JB22(name="jb17"))
        sm.add_widget(JB21(name="jb16"))
        sm.add_widget(JB20(name="jb15"))

        sm.add_widget(jEconomicsYear(name='j economics year'))
        sm.add_widget(JEc23(name="jec23"))
        sm.add_widget(JEc22(name="jec22"))
        sm.add_widget(JEc21(name="jec21"))
        sm.add_widget(JEc20(name="jec20"))
        sm.add_widget(JEc19(name="jec19"))
        sm.add_widget(JEc18(name="jec18"))
        sm.add_widget(JEc17(name="jec17"))
        sm.add_widget(JEc16(name="jec16"))
        sm.add_widget(JEc15(name="jec15"))

        sm.add_widget(jCivicYear(name='j civic year'))
        sm.add_widget(JCivicYear23(name="jcivic23"))
        sm.add_widget(JCivicYear22(name="jcivic22"))
        sm.add_widget(JCivicYear21(name="jcivic21"))
        sm.add_widget(JCivicYear20(name="jcivic20"))
        sm.add_widget(JCivicYear19(name="jcivic19"))
        sm.add_widget(JCivicYear18(name="jcivic18"))
        sm.add_widget(JCivicYear17(name="jcivic17"))
        sm.add_widget(JCivicYear16(name="jcivic16"))
        sm.add_widget(JCivicYear15(name="jcivic15"))

        sm.add_widget(jMarketingYear(name='j market year'))
        sm.add_widget(JMarketingYear2023(name='j market 23'))
        sm.add_widget(JMarketingYear2022(name='j market 22'))
        sm.add_widget(JMarketingYear2021(name='j market 21'))
        sm.add_widget(JMarketingYear2020(name='j market 20'))
        sm.add_widget(JMarketingYear2019(name='j market 19'))
        sm.add_widget(JMarketingYear2018(name='j market 18'))
        sm.add_widget(JMarketingYear2017(name='j market 17'))
        sm.add_widget(JMarketingYear2016(name='j market 16'))
        sm.add_widget(JMarketingYear2015(name='j market 15'))

        sm.add_widget(jAccountingYear(name='j accounts year'))
        sm.add_widget(JAccountingYear2023(name='j accounts 23'))
        sm.add_widget(JAccountingYear2022(name='j accounts 22'))
        sm.add_widget(JAccountingYear2021(name='j accounts 21'))
        sm.add_widget(JAccountingYear2020(name='j accounts 20'))
        sm.add_widget(JAccountingYear2019(name='j accounts 19'))
        sm.add_widget(JAccountingYear2018(name='j accounts 18'))
        sm.add_widget(JAccountingYear2017(name='j accounts 17'))
        sm.add_widget(JAccountingYear2016(name='j accounts 16'))
        sm.add_widget(JAccountingYear2016(name='j accounts 15'))

        sm.add_widget(jLiteratureYear(name='j literature year'))
        sm.add_widget(JLiteratureYear2023(name='j literature 23'))
        sm.add_widget(JLiteratureYear2022(name='j literature 22'))
        sm.add_widget(JLiteratureYear2021(name='j literature 21'))
        sm.add_widget(JLiteratureYear2020(name='j literature 20'))
        sm.add_widget(JLiteratureYear2019(name='j literature 19'))
        sm.add_widget(JLiteratureYear2018(name='j literature 18'))
        sm.add_widget(JLiteratureYear2017(name='j literature 17'))
        sm.add_widget(JLiteratureYear2016(name='j literature 16'))
        sm.add_widget(JLiteratureYear2015(name='j literature 15'))

        sm.add_widget(jFurtherMathYear(name='j further maths year'))
        sm.add_widget(JFurtherMathYear2023(name='j further maths 23'))
        sm.add_widget(JFurtherMathYear2022(name='j further maths 22'))
        sm.add_widget(JFurtherMathYear2021(name='j further maths 21'))
        sm.add_widget(JFurtherMathYear2020(name='j further maths 20'))
        sm.add_widget(JFurtherMathYear2019(name='j further maths 19'))
        sm.add_widget(JFurtherMathYear2018(name='j further maths 18'))
        sm.add_widget(JFurtherMathYear2017(name='j further maths 17'))
        sm.add_widget(JFurtherMathYear2016(name='j further maths 16'))
        sm.add_widget(JFurtherMathYear2015(name='j further maths 15'))

        sm.add_widget(jChristianReligionStudiesYear(name='j crs year'))
        sm.add_widget(JChristianReligionStudies2023(name='j crs 23'))
        sm.add_widget(JChristianReligionStudies2022(name='j crs 22'))
        sm.add_widget(JChristianReligionStudies2021(name='j crs 21'))
        sm.add_widget(JChristianReligionStudies2020(name='j crs 20'))
        sm.add_widget(JChristianReligionStudies2019(name='j crs 19'))
        sm.add_widget(JChristianReligionStudies2018(name='j crs 18'))
        sm.add_widget(JChristianReligionStudies2017(name='j crs 17'))
        sm.add_widget(JChristianReligionStudies2016(name='j crs 16'))
        sm.add_widget(JChristianReligionStudies2015(name='j crs 15'))

        sm.add_widget(jGeographyYear(name='j geography year'))
        sm.add_widget(JGeographyYear2023(name='j geography 23'))
        sm.add_widget(JGeographyYear2022(name='j geography 22'))
        sm.add_widget(JGeographyYear2021(name='j geography 21'))
        sm.add_widget(JGeographyYear2020(name='j geography 20'))
        sm.add_widget(JGeographyYear2019(name='j geography 19'))
        sm.add_widget(JGeographyYear2018(name='j geography 18'))
        sm.add_widget(JGeographyYear2017(name='j geography 17'))
        sm.add_widget(JGeographyYear2016(name='j geography 16'))
        sm.add_widget(JGeographyYear2015(name='j geography 15'))

        sm.add_widget(jCommerceYear(name='j commerce year'))
        sm.add_widget(JCommerceYear2023(name='j commerce 23'))
        sm.add_widget(JCommerceYear2022(name='j commerce 22'))
        sm.add_widget(JCommerceYear2021(name='j commerce 21'))
        sm.add_widget(JCommerceYear2020(name='j commerce 20'))
        sm.add_widget(JCommerceYear2019(name='j commerce 19'))
        sm.add_widget(JCommerceYear2018(name='j commerce 18'))
        sm.add_widget(JCommerceYear2017(name='j commerce 17'))
        sm.add_widget(JCommerceYear2016(name='j commerce 16'))
        sm.add_widget(JCommerceYear2015(name='j commerce 15'))

        # Setting NECO subject and year screen
        sm.add_widget(NecoSubject(name="necosubject"))
        sm.add_widget(NMathematicsYear(name='n math year'))
        sm.add_widget(NEnglishYear(name='n english year'))
        sm.add_widget(NPhysicsYear(name='n physics year'))
        sm.add_widget(NChemistryYear(name='n chemistry year'))
        sm.add_widget(NBY(name='nby'))
        sm.add_widget(NEconomicsYear(name='n economics year'))
        sm.add_widget(NCivicYear(name='n civic year'))
        sm.add_widget(NMarketingYear(name='n market year'))
        sm.add_widget(NAccountingYear(name='n accounts year'))
        sm.add_widget(NLiteratureYear(name='n literature year'))
        sm.add_widget(NFurtherMathYear(name='n further maths year'))
        sm.add_widget(NChristianReligionStudiesYear(name='j crs year'))
        sm.add_widget(NGeographyYear(name='n geography year'))
        sm.add_widget(NCommerceYear(name='n commerce year'))'''


        # returning screen manager set with a variable of sm
        return screen_manager

    def on_start(self):
        Clock.schedule_once(self.change_screen, 2.095)

    def change_screen(self, dt):
        screen_manager.current = "home"


# returning the main app class
MainApp().run()
