import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)

##        #square frame
##        wx.StaticBox(panel, label='Static Box Title', pos=(10,10), size=(280,200))
##        wx.StaticText(panel, label='Single line', pos=(100,100))

##        #simpsons dropdown
##        simpsons = ['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']
##        cb = wx.ComboBox(panel, pos=(100, 50), choices=simpsons, style=wx.CB_READONLY)

##        #chekboxes
##        wx.CheckBox(panel, label='Male', pos=(100, 50))
##        wx.CheckBox(panel, label='Female', pos=(100, 80))

##        #circle options, exclusive
##        wx.RadioButton(panel, label='Male', pos=(100, 50), style=wx.RB_GROUP)
##        wx.RadioButton(panel, label='Female', pos=(100, 80))

##        #text boxes
##        wx.TextCtrl(panel, size=(200, -1), pos=(50,30))
##        wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(200, 100), pos=(50,80))

##        #positive number selector scroller
##        wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70, 25))

        #same thing but with error: "No attribute GetPosition"
        sc = wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70, 25))
        self.valueText = wx.StaticText(panel, label='', pos=(130,80))

        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)
        
    def spinControl(self, event):
        # Get spin control value
        value = event.GetPosition()
        # Update static text
        self.valueText.SetLabel(str(value))


app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
