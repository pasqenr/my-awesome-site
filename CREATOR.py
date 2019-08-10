#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import wx
import os
from slugify import slugify
from shutil import copyfile

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainFramee(wx.Frame):
    def __init__(self, *args, **kwds):
       # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((691, 256))
        self.combo_box_world = wx.ComboBox(self, wx.ID_ANY, choices=['New'], style=wx.CB_DROPDOWN)
        self.text_ctrl_world = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_world = wx.Button(self, wx.ID_ANY, "Create")
        self.text_ctrl_character = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_character = wx.Button(self, wx.ID_ANY, "Create")

        self.__load_combo_box_world()

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.combo_box_world_changed, self.combo_box_world)
        self.Bind(wx.EVT_TEXT, self.text_ctrl_world_changed, self.text_ctrl_world)
        self.Bind(wx.EVT_BUTTON, self.create_world, self.button_world)
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

    def __set_properties(self):
       # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Create")
        self.combo_box_world.SetMinSize((160, 23))
        self.text_ctrl_world.SetMinSize((160, 23))
        self.text_ctrl_world.Enable(False)
        self.button_world.SetMinSize((90, 26))
        self.button_world.Enable(False)
        self.text_ctrl_character.SetMinSize((160, 23))
        self.text_ctrl_character.Enable(False)
        self.button_character.SetMinSize((90, 26))
        self.button_character.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 4, 0, 0)
        label_NameWorld = wx.StaticText(self, wx.ID_ANY, "World:")
        grid_sizer_1.Add(label_NameWorld, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.combo_box_world, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_world, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_world, 0, wx.ALIGN_CENTER, 0)
        label_character = wx.StaticText(self, wx.ID_ANY, "Character:")
        grid_sizer_1.Add(label_character, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.text_ctrl_character, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_1.Add(self.button_character, 0, wx.ALIGN_CENTER, 0)
        self.SetSizer(grid_sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnClose(self, event):
        self.Destroy()

    def combo_box_world_changed(self, event):  # wxGlade: MainFrame.<event_handler>
        self.text_ctrl_world.Clear()
        selection = self.combo_box_world.GetStringSelection()
        self.selected_world = selection
        self.button_world.Disable()

        if selection == 'New':
            self.text_ctrl_world.Enable()
            self.text_ctrl_character.Disable()
            self.text_ctrl_character.Clear()
        else:
            self.text_ctrl_character.Enable()
            self.text_ctrl_world.Disable()

    def text_ctrl_world_changed(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.selected_world == 'New' and self.text_ctrl_world.IsEmpty():
            self.button_world.Disable()
        else:
            self.button_world.Enable()
    
    def text_ctrl_character_changed(self, event):  # wxGlade: MainFrame.<event_handler>
        if not self.text_ctrl_character.IsEmpty():
            self.button_character.Enable()
        else:
            self.button_character.Disable()
    
    def create_world(self, event):  # wxGlade: MainFrame.<event_handler>
        selection = self.combo_box_world.GetStringSelection()

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
            md_file.write(f"---\nlayout: worlds\npermalink: /:name/\nname: {new_name}\n---")
                
        os.mkdir(dir_path)
        wx.MessageBox(parent=self, message=f"World {new_name} created successfully", 
            caption='Success', style=wx.OK|wx.ICON_INFORMATION)
        self.selected_world = new_name
        self.text_ctrl_character.Enable()
        self.__load_combo_box_world()
    
    def create_character(self, event):  # wxGlade: MainFrame.<event_handler>
        new_name = self.text_ctrl_character.GetValue()
        md_path = f"./_characters/{new_name}.md"
        dir_path = f"./assets/images/worlds/{self.selected_world}/{new_name}"
        skel_path = f"./assets/images/skeletons/gallery.png"
        image_path = f"{dir_path}/{new_name}.png"

        if new_name is None:
            wx.MessageBox(parent=self, message='Please add new character name', 
                caption='Error', style=wx.OK|wx.ICON_ERROR)
            return
    
        if os.path.isfile(md_path):
            wx.MessageBox(parent=self, message='Character file already exists, please choose a different name', 
                caption='Error', style=wx.OK|wx.ICON_ERROR)
            return
        
        if os.path.isdir(dir_path):
            wx.MessageBox(parent=self, message='Character directory already exists, please choose a different name', 
                caption='Error', style=wx.OK|wx.ICON_ERROR)
            return
    
        with open(md_path, 'w') as md_file:
            md_file.write(f"---\nlayout: character\npermalink: /{slugify(self.selected_world)}/:name\nname: {new_name}\nworld_name: {self.selected_world}\n---\n\nDESCRIPTION HERE (MARKDOWN ALLOWED)")
        
        os.mkdir(dir_path)
        copyfile(skel_path, image_path)
        self.selected_character = new_name
        
        wx.MessageBox(parent=self, message=f"Character {new_name} created successfully", 
            caption='Success', style=wx.OK|wx.ICON_INFORMATION)


# end of class MainFramee


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFramee(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
