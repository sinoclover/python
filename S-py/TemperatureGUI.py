import easygui

f = float(easygui.enterbox('Enter the Fahrenheit '))
c = 5.0 / 9 * (f - 32)
easygui.msgbox('The Centigrade is {0}℃ when Fahrenheit is {1}℉.'.format(c, f))


