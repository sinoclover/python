import easygui

easygui.msgbox('Record your information')
name = easygui.enterbox('Enter your name ')
address = easygui.enterbox('Enter your address ')
town = easygui.enterbox('Enter your town ')
postcode = easygui.enterbox('Enter your postcode ')
easygui.msgbox(name + '\n' + address + '\n'+ town + '\n'+ postcode)