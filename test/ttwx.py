#!/usr/bin/python2
#coding:utf8
import wx

def open_file(evt):
    file_read=open(file_path.GetValue(),'r').read()
    file1_content.SetValue(file_read)
def save_file(evt):
    file_write=open(file_path.GetValue(),'w')
    file_write.write(file1_content.GetValue())
    file_write.close()

app=wx.App()
win=wx.Frame(None,title="记事本",size=(420,340))
bkg=wx.Panel(win)

open_button=wx.Button(bkg,label="打开")
save_button=wx.Button(bkg,label="保存")
file_path=wx.TextCtrl(bkg)
file1_content=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)


open_button.Bind(wx.EVT_BUTTON,open_file)
save_button.Bind(wx.EVT_BUTTON,save_file)

top_box=wx.BoxSizer(wx.HORIZONTAL)
top_box.Add(file_path,proportion=1,flag=wx.EXPAND)
top_box.Add(open_button,proportion=0,flag=wx.RIGHT,border=5)
top_box.Add(save_button,proportion=0,flag=wx.RIGHT,border=5)
all_box=wx.BoxSizer(wx.VERTICAL)
all_box.Add(top_box,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
all_box.Add(file1_content,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM,border=5)
bkg.SetSizer(all_box)
win.Show()
app.MainLoop()