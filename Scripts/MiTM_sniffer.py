# by error434
# copyrighted © 2020
# This is script is to be used for ethical purposes only

import os
import wx


class Frame(wx.Frame):
    def __init__(self):
        super(Frame, self).__init__(None)
        self.SetTitle('Client IP and Browser')
        panel = wx.Panel(self)

        os.system("touch ./Modules/Logs/sniffer/MiTM_data.txt")
        os.system('python ./Modules/mitm_sniffer_core.py &')

        style = wx.TE_MULTILINE | wx.TE_READONLY
        self.text = wx.TextCtrl(panel, value="", style=style, size=(850, 900))

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.AddStretchSpacer(1)
        sizer.Add(self.text, 0, wx.EXPAND)
        sizer.AddStretchSpacer(1)
        panel.SetSizer(sizer)
        self.on_timer()

    def on_timer(self):
        client_list = open("./Modules/Logs/sniffer/MiTM_data.txt", 'r').read()

        self.text.SetValue(str(client_list))

        wx.CallLater(2000, self.on_timer)


# ~ if __name__ == '__main__':
def startSniff():
    app = wx.App()
    frame = Frame()
    frame.Show()
    frame.SetSize((850, 600))
    app.MainLoop()
    os.system("rm ./Modules/Logs/sniffer/MiTM_data.txt")
    os.system("kill  `ps aux | grep mitm_sniffer_core.py | head -1 | awk '{print $2}'`")
    os.system("kill  `ps aux | grep MiTM_sniffer.py | head -1 | awk '{print $2}'`")


startSniff()
