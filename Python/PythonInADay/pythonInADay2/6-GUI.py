import wx

class Frame(wx.Frame):
    # Added title parameter
    def __init__(self, title):
        # title = title variable
        wx.Frame.__init__(self, None,\
          title=title, size=(300,200))
        panel = wx.Panel(self)
        button = wx.Button(panel,label="Exit",size=(100,40),pos=(100,30))
        # Bind button event to the function self.exit
        button.Bind(wx.EVT_BUTTON, self.exit)

        # Create menu bar
        menuBar = wx.MenuBar()
        # Create wx menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()

        # Add items to fileMenu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")

        #add items to editMenu
        editMenu.Append(wx.NewId(), "Cut          Ctrl+X")
        editMenu.Append(wx.NewId(), "Copy       Ctrl+C")        
        editMenu.Append(wx.NewId(), "Paste       Ctrl+V")

        # Bind exit menu item to exit function
        self.Bind(wx.EVT_MENU, self.exit, exitItem)
        
        # Add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()
    
    def exit(self, event):
        self.Destroy()
        
app = wx.App()
# Pass in the frame title
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()
