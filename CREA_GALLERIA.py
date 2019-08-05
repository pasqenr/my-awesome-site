#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import os

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((547, 330))
        self.text_ctrl_GalleryName = wx.TextCtrl(self, wx.ID_ANY, "")
        self.buttonSend = wx.Button(self, wx.ID_ANY, "Crea")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.create_gallery, self.buttonSend)
        
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("frame")
        self.text_ctrl_GalleryName.SetMinSize((160, 23))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 2, 0, 0)
        labelGalleryName = wx.StaticText(self, wx.ID_ANY, "Nome galleria:")
        grid_sizer_1.Add(labelGalleryName, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_GalleryName, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.buttonSend, 0, wx.ALIGN_CENTER, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade
    

    def OnClose(self, event):
        event.Skip()
        self.Destroy()
    

    def create_gallery(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        gallery_name = self.text_ctrl_GalleryName.GetValue()
        md_file_path = f"./_details/{gallery_name}.md"
        dir_path = f"./assets/images/galleries/{gallery_name}"

        if not gallery_name:
            errorDialog = ErrorDialog(None)
            errorDialog.Show()
        else:
            if os.path.isfile(md_file_path):
                dialog = ErrorDialogFileExists(None)
                dialog.Show()
                return
            
            if os.path.isdir(dir_path):
                dialog = ErrorDialogDirExists(None)
                dialog.Show()
                return

            with open(md_file_path, 'w') as md_file:
                md_file.write(f"---\nlayout: detail\nname: {gallery_name}\n---\n\nWRITE_DESCRIPTION_HERE")
            
            os.mkdir(dir_path)

            successDialog = SuccessDialog(None)
            successDialog.Show()
        

# end of class MainFrame


class ErrorDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ErrorDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ErrorDialog.__set_properties
        self.SetTitle("Errore")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SuccessDialog.__do_layout
        grid_sizer_3 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Errore! Nome della galleria vuoto!", style=wx.ALIGN_CENTER)
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_3.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class ErrorDialog


class ErrorDialogFileExists(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ErrorDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ErrorDialog.__set_properties
        self.SetTitle("Errore")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SuccessDialog.__do_layout
        grid_sizer_3 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Errore! La scheda della galleria esiste già!", style=wx.ALIGN_CENTER)
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_3.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class ErrorDialog


class ErrorDialogDirExists(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ErrorDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ErrorDialog.__set_properties
        self.SetTitle("Errore")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SuccessDialog.__do_layout
        grid_sizer_3 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Errore! La cartella della galleria esiste già!", style=wx.ALIGN_CENTER)
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_3.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class ErrorDialog


class SuccessDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SuccessDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SuccessDialog.__set_properties
        self.SetTitle("Successo")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SuccessDialog.__do_layout
        grid_sizer_3 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Galleria creata correttamente!", style=wx.ALIGN_CENTER)
        label_3.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_3.Add(label_3, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add((0, 0), 0, 0, 0)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.Fit(self)
        self.Layout()
        # end wxGlade

# end of class SuccessDialog


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
