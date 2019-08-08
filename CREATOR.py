#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import os
from slugify import slugify

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
       # begin wxGlade: MainFram.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((691, 256))
        self.combo_box_world = wx.ComboBox(self, wx.ID_ANY, choices=['New'], style=wx.CB_DROPDOWN)
        self.text_ctrl_world = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_world = wx.Button(self, wx.ID_ANY, "Crea")
        self.combo_box_gallery = wx.ComboBox(self, wx.ID_ANY, choices=['New'], style=wx.CB_DROPDOWN)
        self.text_ctrl_gallery = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_gallery = wx.Button(self, wx.ID_ANY, "Crea")
        self.text_ctrl_character = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_character = wx.Button(self, wx.ID_ANY, "Crea")

        self.__load_combo_box_world()

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.combo_box_world_changed, self.combo_box_world)
        self.Bind(wx.EVT_TEXT, self.text_ctrl_world_changed, self.text_ctrl_world)
        self.Bind(wx.EVT_BUTTON, self.create_world, self.button_world)
        self.Bind(wx.EVT_COMBOBOX, self.combo_box_gallery_changed, self.combo_box_gallery)
        self.Bind(wx.EVT_TEXT, self.text_ctrl_gallery_changed, self.text_ctrl_gallery)
        self.Bind(wx.EVT_BUTTON, self.create_gallery, self.button_gallery)
        self.Bind(wx.EVT_TEXT, self.text_ctrl_character_changed, self.text_ctrl_character)
        self.Bind(wx.EVT_BUTTON, self.create_character, self.button_character)
        # end wxGlade

        self.selected_world = None
        self.selected_gallery = None
    
    def __load_combo_box_world(self):
        world_path = './assets/images/worlds/'

        for root, folders, files in os.walk(world_path):
            for folder in folders:
                if root == world_path:
                    self.combo_box_world.Append(folder)
    
    def __load_combo_box_gallery(self):
        galleries_path = f"./assets/images/worlds/{self.selected_world}/"

        for root, folders, files in os.walk(galleries_path):
            for folder in folders:
                print(folder)
                if root == galleries_path:
                    self.combo_box_gallery.Append(folder)

    def __set_properties(self):
       # begin wxGlade: MainFram.__set_properties
        self.SetTitle("Crea")
        self.combo_box_world.SetMinSize((160, 23))
        self.text_ctrl_world.SetMinSize((160, 23))
        self.text_ctrl_world.Enable(False)
        self.button_world.SetMinSize((90, 26))
        self.button_world.Enable(False)
        self.combo_box_gallery.SetMinSize((160, 23))
        self.combo_box_gallery.Enable(False)
        self.text_ctrl_gallery.SetMinSize((160, 23))
        self.text_ctrl_gallery.Enable(False)
        self.button_gallery.SetMinSize((90, 26))
        self.button_gallery.Enable(False)
        self.text_ctrl_character.SetMinSize((160, 23))
        self.text_ctrl_character.Enable(False)
        self.button_character.SetMinSize((90, 26))
        self.button_character.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFram.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 4, 0, 0)
        label_NameWorld = wx.StaticText(self, wx.ID_ANY, "World:")
        grid_sizer_1.Add(label_NameWorld, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.combo_box_world, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_world, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_world, 0, wx.ALIGN_CENTER, 0)
        label_gallery = wx.StaticText(self, wx.ID_ANY, "Gallery:")
        grid_sizer_1.Add(label_gallery, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.combo_box_gallery, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_gallery, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_gallery, 0, wx.ALIGN_CENTER, 0)
        label_character = wx.StaticText(self, wx.ID_ANY, "Character:")
        grid_sizer_1.Add(label_character, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_character, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_character, 0, wx.ALIGN_CENTER, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnClose(self, event):
        event.Skip()
        self.Destroy()

    def combo_box_world_changed(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        self.text_ctrl_world.Clear()
        selection = self.combo_box_world.GetStringSelection()
        self.selected_world = selection
        self.button_world.Disable()

        if selection == 'New':
            self.combo_box_gallery.Clear()
            self.combo_box_gallery.Append('New')
            self.text_ctrl_world.Enable()
        else:
            self.__load_combo_box_gallery()
            self.text_ctrl_world.Disable()
            self.combo_box_gallery.Enable()

    def combo_box_gallery_changed(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        self.text_ctrl_gallery.Clear()
        selection = self.combo_box_gallery.GetStringSelection()
        self.selected_gallery = selection
        self.button_gallery.Disable()

        if selection == 'New':
            self.text_ctrl_gallery.Enable()
        else:
            self.text_ctrl_gallery.Disable()

    def text_ctrl_world_changed(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        if self.selected_world == 'New' and self.text_ctrl_world.IsEmpty():
            self.button_world.Disable()
        else:
            self.button_world.Enable()
            self.combo_box_gallery.Enable()

    def text_ctrl_gallery_changed(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        self.text_ctrl_character.Enable()
        self.button_character.Enable()

        if self.selected_gallery == 'New':
            if self.text_ctrl_gallery.IsEmpty():
                self.button_gallery.Disable()
            else:
                self.button_gallery.Enable()
        else:
            self.text_ctrl_gallery.Disable()
    
    def text_ctrl_character_changed(self, event):  # wxGlade: MainFram.<event_handler>
        print("Event handler 'text_ctrl_character_changed' not implemented!")
        event.Skip()
    
    def create_world(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        selection = self.combo_box_world.GetStringSelection()

        if selection == 'New':
            new_name = self.text_ctrl_world.GetValue()
            self.selected_world = new_name

            md_path = f"./_worlds/{new_name}.md"
            dir_path = f"./assets/images/worlds/{new_name}"

            if new_name is None:
                wx.MessageBox(parent=self, message='Please add new world name', 
                    caption='Error', style=wx.OK|wx.ICON_ERROR)
                return
        
            if os.path.isfile(md_path):
                wx.MessageBox(parent=self, message='World file already exists, please choose a different name', 
                    caption='Error', style=wx.OK|wx.ICON_ERROR)
                return
            
            if os.path.isdir(dir_path):
                wx.MessageBox(parent=self, message='World already exists, please choose a different name', 
                    caption='Error', style=wx.OK|wx.ICON_ERROR)
                return

            with open(md_path, 'w') as md_file:
                md_file.write(f"---\nlayout: worlds\npermalink: /:name/\nname: {slugify(new_name)}\n---")
                
            os.mkdir(dir_path)
            wx.MessageBox(parent=self, message=f"World {new_name} created successfully", 
                    caption='Success', style=wx.OK|wx.ICON_INFORMATION)
            self.selected_world = new_name
            self.__load_combo_box_gallery()
        else:
            self.selected_world = selection
            self.__load_combo_box_gallery()

    def create_gallery(self, event):  # wxGlade: MainFram.<event_handler>
        event.Skip()
        gallery_name = self.text_ctrl_gallery.GetValue()
        md_path = f"./_galleries/{gallery_name}.md"
        dir_path = f"./assets/images/worlds/{self.selected_world}/{gallery_name}"

        if not gallery_name:
            wx.MessageBox(parent=self, message='Please add new gallery name', 
                caption='Error', style=wx.OK|wx.ICON_ERROR)
            return
        
        if os.path.isfile(md_path):
            wx.MessageBox(parent=self, message='Gallery file already exists, please choose a different name', 
                caption='Error', style=wx.OK|wx.ICON_ERROR)
            return
            
        if os.path.isdir(dir_path):
            wx.MessageBox(parent=self, message='Gallery directory already exists, please choose a different name', 
                caption='Error', style=wx.OK|wx.ICON_ERROR)
            return

        with open(md_path, 'w') as md_file:
            md_file.write(f"---\nlayout: detail\nname: {gallery_name}\n---\n\nWRITE_DESCRIPTION_HERE")
            
        os.mkdir(dir_path)

        wx.MessageBox(parent=self, message=f"Gallery {gallery_name} created successfully", 
            caption='Success', style=wx.OK|wx.ICON_INFORMATION)
    
    def create_character(self, event):  # wxGlade: MainFram.<event_handler>
        print("Event handler 'create_character' not implemented!")
        event.Skip()


# end of class MainFrame


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
